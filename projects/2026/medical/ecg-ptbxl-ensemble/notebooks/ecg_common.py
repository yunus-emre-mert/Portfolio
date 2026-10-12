"""Shared PTB-XL experiment protocol for Colab notebooks 01-06.

Model architectures stay in notebooks. This module owns split constants,
metrics, thresholds, prediction schema, reproducibility, and the Trainer.
"""
from __future__ import annotations

import json
import os
import random
import shutil
from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    f1_score,
    hamming_loss,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
)

# ---------------------------------------------------------------------------
# Shared experiment config
# ---------------------------------------------------------------------------

CLASSES: List[str] = ["NORM", "MI", "STTC", "CD", "HYP"]
TRAIN_FOLDS: Tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8)
VAL_FOLDS: Tuple[int, ...] = (9,)
TEST_FOLDS: Tuple[int, ...] = (10,)
SEEDS: List[int] = [42, 52, 62]
MAX_EPOCHS: int = 50
EARLY_STOPPING_PATIENCE: int = 7
PRIMARY_METRIC: str = "macro_auprc"
PRIMARY_MONITOR: str = "val_macro_auprc"
EVALUATE_TEST: bool = True
SAMPLING_RATE: int = 100
N_LEADS: int = 12
SIGNAL_SECONDS: int = 10
DATASET_VERSION: str = "1.0.3"
RAW_DATASET_DIRNAME: str = (
    "ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3"
)

# Canonical result keys -> experiments/ folder names used by existing notebooks.
# ECGFounder trains native 500 Hz tensors from processed/sr500 (notebook 04).
MODEL_KEYS: Dict[str, str] = {
    "resnet18": "resnet18_1d",
    "xlstm": "xlstm",
    "mamba": "bidirectional_mamba",
    "cwt_vit_kan": "wavelet_kan_cwt_vit",
    "ecgfounder": "ecgfounder_500",
}
MODEL_DISPLAY_NAMES: Dict[str, str] = {
    "resnet18": "ResNet18-1D",
    "xlstm": "xLSTM",
    "mamba": "Bidirectional Mamba",
    "cwt_vit_kan": "CWT-ViT-KAN",
    "ecgfounder": "ECGFounder",
    "equal_soft_voting": "Equal Soft Voting",
    "weighted_soft_voting": "Weighted Soft Voting",
    "stacking": "Stacking Ensemble",
}
ENSEMBLE_MEMBERS: Tuple[str, ...] = (
    "resnet18",
    "xlstm",
    "mamba",
    "cwt_vit_kan",
    "ecgfounder",
)

PathLike = Union[str, Path]


def canonical_model_key(name: str) -> str:
    """Map experiments folder name or alias to canonical results/ key."""
    lowered = str(name).strip().lower().replace("-", "_")
    if lowered in MODEL_KEYS:
        return lowered
    inverse = {v: k for k, v in MODEL_KEYS.items()}
    if lowered in inverse:
        return inverse[lowered]
    aliases = {
        "resnet18_1d": "resnet18",
        "resnet": "resnet18",
        "bidirectional_mamba": "mamba",
        "mamba_ssm": "mamba",
        "wavelet_kan_cwt_vit": "cwt_vit_kan",
        "wavelet_kan": "cwt_vit_kan",
        "cwt_vit": "cwt_vit_kan",
        "ecgfounder_500": "ecgfounder",
        "ecg_foundation_finetune": "ecgfounder",  # leftover interpolate runs
        "ecg_founder": "ecgfounder",
        "foundation": "ecgfounder",
    }
    if lowered in aliases:
        return aliases[lowered]
    return lowered


def experiment_model_name(key: str) -> str:
    canon = canonical_model_key(key)
    return MODEL_KEYS.get(canon, key)


def display_model_name(key: str) -> str:
    canon = canonical_model_key(key)
    return MODEL_DISPLAY_NAMES.get(canon, key)


# ---------------------------------------------------------------------------
# Paths / JSON helpers
# ---------------------------------------------------------------------------

def ensure_dir(path: PathLike) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target


def dump_json(data: Any, path: PathLike) -> None:
    serializable = asdict(data) if is_dataclass(data) else data
    Path(path).write_text(json.dumps(serializable, indent=2, default=_json_default), encoding="utf-8")


def load_json(path: PathLike) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _json_default(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, (np.floating, np.integer)):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    raise TypeError(f"Not JSON serializable: {type(value)}")


def expected_n_samples(sampling_rate: int) -> int:
    """10 s PTB-XL record length at 100 Hz (1000) or 500 Hz (5000)."""
    rate = int(sampling_rate)
    if rate == 100:
        return SIGNAL_SECONDS * 100
    if rate == 500:
        return SIGNAL_SECONDS * 500
    raise ValueError(f"Unsupported sampling_rate={sampling_rate}; expected 100 or 500.")


def project_paths(project_dir: PathLike, sampling_rate: int = SAMPLING_RATE) -> Dict[str, Any]:
    root = Path(project_dir)
    fs = int(sampling_rate)
    processed = root / "processed" / f"sr{fs}"
    return {
        "project_dir": root,
        "processed_dir": processed,
        "experiments_dir": root / "experiments",
        "results_dir": root / "results",
        "data_dir": root / "data",
        "sampling_rate": fs,
    }


def seed_run_dir(experiments_dir: PathLike, model_name: str, seed: int) -> Path:
    return Path(experiments_dir) / experiment_model_name(model_name) / f"seed_{int(seed)}"


def seed_results_dir(results_dir: PathLike, model_key: str, seed: int) -> Path:
    return Path(results_dir) / canonical_model_key(model_key) / f"seed_{int(seed)}"


# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------

def set_seed(seed: int) -> None:
    """Python / NumPy / PyTorch / CUDA seeds and deterministic flags."""
    seed = int(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        try:
            torch.use_deterministic_algorithms(True, warn_only=True)
        except Exception:
            pass
    except ImportError:
        pass


# ---------------------------------------------------------------------------
# Split / leakage / manifest checks
# ---------------------------------------------------------------------------

def assert_patient_disjoint(
    train_patients: Iterable[Any],
    val_patients: Iterable[Any],
    test_patients: Iterable[Any],
) -> None:
    train_p = set(train_patients)
    val_p = set(val_patients)
    test_p = set(test_patients)
    assert train_p.isdisjoint(val_p), "Patient leakage: train overlaps val"
    assert train_p.isdisjoint(test_p), "Patient leakage: train overlaps test"
    assert val_p.isdisjoint(test_p), "Patient leakage: val overlaps test"


def find_ptbxl_data_root(start: PathLike) -> Path:
    """Resolve the raw PTB-XL 1.0.3 folder under data/."""
    start = Path(start)
    preferred = start / RAW_DATASET_DIRNAME
    if (preferred / "ptbxl_database.csv").exists():
        return preferred.resolve()

    matches = sorted(start.rglob("ptbxl_database.csv"), key=lambda p: len(p.parts))
    versioned = [p.parent for p in matches if DATASET_VERSION in p.parent.name]
    if versioned:
        return versioned[0].resolve()
    raise FileNotFoundError(
        f"PTB-XL {DATASET_VERSION} not found under {start}. "
        f"Expected {preferred} with ptbxl_database.csv."
    )


def assert_ptbxl_version(data_root: PathLike, expected: str = DATASET_VERSION) -> str:
    root = Path(data_root)
    if expected not in root.name:
        raise ValueError(
            f"DATA_ROOT must be PTB-XL {expected}, got {root.name}. "
            f"Expected {RAW_DATASET_DIRNAME}."
        )
    if not (root / "ptbxl_database.csv").exists():
        raise FileNotFoundError(f"ptbxl_database.csv missing under {root}")
    return expected


def assert_dataset_version_manifest(manifest: Mapping[str, Any]) -> None:
    version = str(manifest.get("dataset_version") or manifest.get("raw_root_name") or "")
    if DATASET_VERSION not in version:
        raise ValueError(
            f"processed tensors are not PTB-XL {DATASET_VERSION} (got {version!r}). "
            "Re-run 00_ptbxl_colab_process with FORCE_REBUILD=True using the 1.0.3 folder."
        )


def assert_official_strat_fold_manifest(manifest: Mapping[str, Any]) -> None:
    split_by = manifest.get("split_by")
    train_folds = tuple(manifest.get("train_folds") or ())
    val_folds = tuple(manifest.get("val_folds") or ())
    test_folds = tuple(manifest.get("test_folds") or ())
    classes = list(manifest.get("classes") or [])
    if (
        split_by != "strat_fold"
        or train_folds != TRAIN_FOLDS
        or val_folds != VAL_FOLDS
        or test_folds != TEST_FOLDS
    ):
        raise ValueError(
            "Processed cache is not official strat_fold 1-8 / 9 / 10. "
            "Re-run 00_ptbxl_colab_process with FORCE_REBUILD=True."
        )
    if classes and classes != CLASSES:
        raise ValueError(f"Label order mismatch. Expected {CLASSES}, got {classes}")


def assert_processed_sampling_rate(manifest: Mapping[str, Any]) -> None:
    """If the manifest records fs / length, require 100 Hz → 1000 or 500 Hz → 5000."""
    if "sampling_rate" not in manifest and "n_samples" not in manifest:
        return
    fs = int(manifest.get("sampling_rate") or 0)
    n_samples = int(manifest.get("n_samples") or 0)
    if fs not in (100, 500):
        raise ValueError(
            f"Processed sampling_rate must be 100 or 500, got {manifest.get('sampling_rate')!r}."
        )
    expected = expected_n_samples(fs)
    if n_samples and n_samples != expected:
        raise ValueError(
            f"Need n_samples={expected} at {fs} Hz, got {n_samples}."
        )


def load_processed_manifest(processed_dir: PathLike) -> dict:
    processed_dir = Path(processed_dir)
    manifest_path = processed_dir / "manifest.json"
    required = [manifest_path] + [
        processed_dir / f"{kind}_{split}.npy"
        for split in ("train", "val", "test")
        for kind in ("X", "y", "ids")
    ]
    missing = [p for p in required if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing processed PTB-XL tensors. "
            "Run notebooks/00_ptbxl_colab_process.ipynb through the "
            "memmap export cell first.\n"
            f"Expected under: {processed_dir}\n"
            "Missing:\n  - " + "\n  - ".join(str(p) for p in missing)
        )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert_official_strat_fold_manifest(manifest)
    assert_dataset_version_manifest(manifest)
    assert_processed_sampling_rate(manifest)
    return manifest


def load_split_index(processed_dir: PathLike) -> pd.DataFrame:
    path = Path(processed_dir) / "split_index.parquet"
    if not path.exists():
        raise FileNotFoundError(
            f"split_index.parquet not found: {path}. Re-run notebook 00 export."
        )
    return pd.read_parquet(path)


# ---------------------------------------------------------------------------
# Loss helpers
# ---------------------------------------------------------------------------

def pos_weight_from_train(y_train: np.ndarray) -> np.ndarray:
    """Class pos_weight = neg/pos from TRAIN labels only."""
    y = np.asarray(y_train, dtype=np.float64)
    if y.ndim != 2:
        raise ValueError(f"y_train must be (N, C), got {y.shape}")
    positives = np.maximum(y.sum(axis=0), 1.0)
    negatives = np.maximum(y.shape[0] - positives, 1.0)
    return (negatives / positives).astype(np.float32)


# ---------------------------------------------------------------------------
# Metrics / thresholds / 2x2 CM
# ---------------------------------------------------------------------------

def _safe_metric(func, *args, **kwargs) -> float:
    try:
        value = func(*args, **kwargs)
        return float(value)
    except Exception:
        return float("nan")


def _as_threshold_vector(thresholds: Union[float, Sequence[float], None], n_classes: int) -> np.ndarray:
    if thresholds is None:
        return np.full(n_classes, 0.5, dtype=np.float64)
    array = np.asarray(thresholds, dtype=np.float64)
    if array.ndim == 0:
        return np.full(n_classes, float(array), dtype=np.float64)
    if array.shape[0] != n_classes:
        raise ValueError(f"Need {n_classes} thresholds, got {array.shape}")
    return array


def apply_thresholds(y_prob: np.ndarray, thresholds: Union[float, Sequence[float], None]) -> np.ndarray:
    y_prob = np.asarray(y_prob, dtype=np.float64)
    thr = _as_threshold_vector(thresholds, y_prob.shape[1])
    return (y_prob >= thr[None, :]).astype(np.int32)


def _binary_counts(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[int, int, int, int]:
    tp = int(np.logical_and(y_true == 1, y_pred == 1).sum())
    tn = int(np.logical_and(y_true == 0, y_pred == 0).sum())
    fp = int(np.logical_and(y_true == 0, y_pred == 1).sum())
    fn = int(np.logical_and(y_true == 1, y_pred == 0).sum())
    return tn, fp, fn, tp


def per_class_confusion_2x2(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: Sequence[str] = CLASSES,
) -> Dict[str, Dict[str, int]]:
    """One 2x2 confusion matrix per label. Do not collapse to 5x5 multiclass."""
    y_true = np.asarray(y_true).astype(int)
    y_pred = np.asarray(y_pred).astype(int)
    out: Dict[str, Dict[str, int]] = {}
    for idx, name in enumerate(class_names):
        tn, fp, fn, tp = _binary_counts(y_true[:, idx], y_pred[:, idx])
        out[name] = {"tn": tn, "fp": fp, "fn": fn, "tp": tp}
    return out


def compute_multilabel_metrics(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: Sequence[str] = CLASSES,
    thresholds: Union[float, Sequence[float], None] = None,
) -> Dict[str, float]:
    """Shared multi-label metrics. Thresholded scores use per-class thresholds."""
    y_true = np.asarray(y_true, dtype=np.int32)
    y_prob = np.asarray(y_prob, dtype=np.float64)
    names = list(class_names)
    y_pred = apply_thresholds(y_prob, thresholds)
    cms = per_class_confusion_2x2(y_true, y_pred, names)

    specificities = []
    sensitivities = []
    precisions = []
    f1s = []
    for name in names:
        tn, fp, fn, tp = cms[name]["tn"], cms[name]["fp"], cms[name]["fn"], cms[name]["tp"]
        spec = tn / (tn + fp) if (tn + fp) else float("nan")
        sens = tp / (tp + fn) if (tp + fn) else float("nan")
        prec = tp / (tp + fp) if (tp + fp) else float("nan")
        f1 = (2 * prec * sens / (prec + sens)) if (prec + sens) and np.isfinite(prec) and np.isfinite(sens) else 0.0
        specificities.append(spec)
        sensitivities.append(sens)
        precisions.append(prec)
        f1s.append(f1)

    metrics: Dict[str, float] = {
        "macro_auroc": _safe_metric(roc_auc_score, y_true, y_prob, average="macro"),
        "macro_auprc": _safe_metric(average_precision_score, y_true, y_prob, average="macro"),
        "macro_f1": _safe_metric(f1_score, y_true, y_pred, average="macro", zero_division=0),
        "micro_f1": _safe_metric(f1_score, y_true, y_pred, average="micro", zero_division=0),
        "macro_precision": _safe_metric(precision_score, y_true, y_pred, average="macro", zero_division=0),
        "macro_recall": _safe_metric(recall_score, y_true, y_pred, average="macro", zero_division=0),
        "macro_specificity": float(np.nanmean(specificities)),
        "hamming_loss": _safe_metric(hamming_loss, y_true, y_pred),
        "subset_accuracy": float((y_true == y_pred).all(axis=1).mean()),
    }
    # Aliases used in comparison tables.
    metrics["precision"] = metrics["macro_precision"]
    metrics["recall"] = metrics["macro_recall"]
    metrics["specificity"] = metrics["macro_specificity"]

    for idx, name in enumerate(names):
        metrics[f"auroc_{name}"] = _safe_metric(roc_auc_score, y_true[:, idx], y_prob[:, idx])
        metrics[f"auprc_{name}"] = _safe_metric(average_precision_score, y_true[:, idx], y_prob[:, idx])
        metrics[f"f1_{name}"] = float(f1s[idx])
        metrics[f"precision_{name}"] = float(precisions[idx]) if np.isfinite(precisions[idx]) else float("nan")
        metrics[f"recall_{name}"] = float(sensitivities[idx]) if np.isfinite(sensitivities[idx]) else float("nan")
        metrics[f"sensitivity_{name}"] = metrics[f"recall_{name}"]
        metrics[f"specificity_{name}"] = float(specificities[idx]) if np.isfinite(specificities[idx]) else float("nan")
        for key, value in cms[name].items():
            metrics[f"cm_{name}_{key}"] = float(value)
    return metrics


def optimize_thresholds_f1(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: Sequence[str] = CLASSES,
    grid: Optional[np.ndarray] = None,
) -> Dict[str, float]:
    """Per-class F1-max thresholds on validation only. Never fit on test."""
    y_true = np.asarray(y_true, dtype=np.int32)
    y_prob = np.asarray(y_prob, dtype=np.float64)
    if grid is None:
        grid = np.linspace(0.05, 0.95, 91)
    thresholds: Dict[str, float] = {}
    for idx, name in enumerate(class_names):
        best_t = 0.5
        best_f1 = -1.0
        col_true = y_true[:, idx]
        col_prob = y_prob[:, idx]
        if col_true.max() == col_true.min():
            thresholds[name] = 0.5
            continue
        for t in grid:
            pred = (col_prob >= t).astype(int)
            score = f1_score(col_true, pred, zero_division=0)
            if score > best_f1:
                best_f1 = float(score)
                best_t = float(t)
        thresholds[name] = best_t
    return thresholds


def threshold_vector(thresholds: Mapping[str, float], class_names: Sequence[str] = CLASSES) -> np.ndarray:
    return np.array([float(thresholds[name]) for name in class_names], dtype=np.float64)


# ---------------------------------------------------------------------------
# Prediction CSV schema
# ---------------------------------------------------------------------------

PREDICTION_TRUE_COLS = [f"true_{c}" for c in CLASSES]
PREDICTION_PROB_COLS = [f"prob_{c}" for c in CLASSES]
PREDICTION_PRED_COLS = [f"pred_{c}" for c in CLASSES]


def build_prediction_frame(
    ecg_id: np.ndarray,
    patient_id: np.ndarray,
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: Sequence[str] = CLASSES,
    y_pred: Optional[np.ndarray] = None,
    thresholds: Union[float, Sequence[float], Mapping[str, float], None] = None,
) -> pd.DataFrame:
    names = list(class_names)
    y_true = np.asarray(y_true)
    y_prob = np.asarray(y_prob)
    if y_pred is None:
        if isinstance(thresholds, Mapping):
            thr = threshold_vector(thresholds, names)
        else:
            thr = thresholds
        y_pred = apply_thresholds(y_prob, thr)
    frame = pd.DataFrame(
        {
            "ecg_id": np.asarray(ecg_id).astype(np.int64),
            "patient_id": np.asarray(patient_id).astype(np.int64),
        }
    )
    for idx, name in enumerate(names):
        frame[f"true_{name}"] = y_true[:, idx].astype(np.int32)
    for idx, name in enumerate(names):
        frame[f"prob_{name}"] = y_prob[:, idx].astype(np.float32)
    for idx, name in enumerate(names):
        frame[f"pred_{name}"] = y_pred[:, idx].astype(np.int32)
    return frame


def save_prediction_csv(frame: pd.DataFrame, path: PathLike) -> Path:
    path = Path(path)
    ensure_dir(path.parent)
    frame.to_csv(path, index=False)
    return path


def load_predictions(path: PathLike, class_names: Sequence[str] = CLASSES) -> Tuple[pd.DataFrame, np.ndarray, np.ndarray, np.ndarray]:
    """Load standard or legacy prediction CSV."""
    frame = pd.read_csv(path)
    names = list(class_names)
    true_cols = [f"true_{c}" for c in names]
    if not all(c in frame.columns for c in true_cols):
        legacy = [f"target_{c}" for c in names]
        if all(c in frame.columns for c in legacy):
            for src, dst in zip(legacy, true_cols):
                frame[dst] = frame[src]
    if "patient_id" not in frame.columns:
        frame["patient_id"] = -1
    y_true = frame[true_cols].to_numpy(dtype=np.int32)
    y_prob = frame[[f"prob_{c}" for c in names]].to_numpy(dtype=np.float64)
    pred_cols = [f"pred_{c}" for c in names]
    if all(c in frame.columns for c in pred_cols):
        y_pred = frame[pred_cols].to_numpy(dtype=np.int32)
    else:
        y_pred = apply_thresholds(y_prob, 0.5)
    return frame, y_true, y_prob, y_pred


def summary_table_row(model_label: str, metrics: Mapping[str, float]) -> Dict[str, Any]:
    return {
        "Model": model_label,
        "Macro_AUROC": metrics.get("macro_auroc"),
        "Macro_AUPRC": metrics.get("macro_auprc"),
        "Macro_F1": metrics.get("macro_f1"),
        "Micro_F1": metrics.get("micro_f1"),
        "Precision": metrics.get("precision", metrics.get("macro_precision")),
        "Recall": metrics.get("recall", metrics.get("macro_recall")),
        "Specificity": metrics.get("specificity", metrics.get("macro_specificity")),
    }


def per_class_metrics_table(metrics: Mapping[str, float], class_names: Sequence[str] = CLASSES) -> pd.DataFrame:
    rows = []
    for name in class_names:
        rows.append(
            {
                "class": name,
                "AUROC": metrics.get(f"auroc_{name}"),
                "AUPRC": metrics.get(f"auprc_{name}"),
                "F1": metrics.get(f"f1_{name}"),
                "Precision": metrics.get(f"precision_{name}"),
                "Sensitivity": metrics.get(f"sensitivity_{name}", metrics.get(f"recall_{name}")),
                "Specificity": metrics.get(f"specificity_{name}"),
            }
        )
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Run config JSON
# ---------------------------------------------------------------------------

def save_run_config(path: PathLike, payload: Mapping[str, Any]) -> None:
    dump_json(dict(payload), path)


def default_run_config(**kwargs: Any) -> Dict[str, Any]:
    config = {
        "classes": list(CLASSES),
        "train_folds": list(TRAIN_FOLDS),
        "val_fold": list(VAL_FOLDS),
        "test_fold": list(TEST_FOLDS),
        "seeds": list(SEEDS),
        "max_epochs": MAX_EPOCHS,
        "early_stopping_patience": EARLY_STOPPING_PATIENCE,
        "primary_metric": PRIMARY_METRIC,
        "monitor": PRIMARY_MONITOR,
        "loss": "BCEWithLogitsLoss",
        "optimizer": "AdamW",
        "evaluate_test": EVALUATE_TEST,
        "sampling_rate": SAMPLING_RATE,
    }
    config.update(kwargs)
    return config


def sync_standard_results(
    run_dir: PathLike,
    results_dir: PathLike,
    model_key: str,
    seed: int,
) -> Path:
    """Copy canonical prediction/metric files into results/<model>/seed_<seed>/."""
    src = Path(run_dir)
    dst = ensure_dir(seed_results_dir(results_dir, model_key, seed))
    names = [
        "val_predictions.csv",
        "test_predictions.csv",
        "thresholds.json",
        "config.json",
        "metrics.json",
        "val_metrics.json",
        "test_metrics.json",
    ]
    pred_dir = src / "predictions"
    metrics_dir = src / "metrics"
    mapping = {
        "val_predictions.csv": pred_dir / "val_predictions.csv",
        "test_predictions.csv": pred_dir / "test_predictions.csv",
        "thresholds.json": src / "thresholds.json",
        "config.json": src / "config.json",
        "metrics.json": metrics_dir / "summary.json",
        "val_metrics.json": metrics_dir / "val_summary.json",
        "test_metrics.json": metrics_dir / "test_summary.json",
    }
    for name, source in mapping.items():
        if source.exists():
            shutil.copy2(source, dst / name)
    return dst


# ---------------------------------------------------------------------------
# Ensemble helpers
# ---------------------------------------------------------------------------

def align_prediction_frames(
    frames: Mapping[str, pd.DataFrame],
    class_names: Sequence[str] = CLASSES,
) -> Tuple[pd.DataFrame, Dict[str, np.ndarray], np.ndarray]:
    """Inner-join member prediction tables on ecg_id."""
    names = list(class_names)
    ordered = list(frames.keys())
    merged: Optional[pd.DataFrame] = None
    for key in ordered:
        frame = frames[key].copy()
        if "true_NORM" not in frame.columns and "target_NORM" in frame.columns:
            for c in names:
                frame[f"true_{c}"] = frame[f"target_{c}"]
        keep = ["ecg_id"]
        if "patient_id" in frame.columns:
            keep.append("patient_id")
        keep.extend([f"true_{c}" for c in names])
        keep.extend([f"prob_{c}" for c in names])
        slim = frame[keep].copy()
        rename = {f"prob_{c}": f"prob_{key}_{c}" for c in names}
        slim = slim.rename(columns=rename)
        if merged is None:
            merged = slim
        else:
            cols = ["ecg_id"] + [f"prob_{key}_{c}" for c in names]
            merged = merged.merge(slim[cols], on="ecg_id", how="inner")
    if merged is None or merged.empty:
        raise ValueError("No overlapping ecg_id across ensemble members.")
    merged = merged.sort_values("ecg_id").reset_index(drop=True)
    y_true = merged[[f"true_{c}" for c in names]].to_numpy(dtype=np.int32)
    probs = {
        key: merged[[f"prob_{key}_{c}" for c in names]].to_numpy(dtype=np.float64)
        for key in ordered
    }
    return merged, probs, y_true


def equal_soft_vote(probs: Mapping[str, np.ndarray], member_order: Sequence[str]) -> np.ndarray:
    stacked = np.stack([probs[m] for m in member_order], axis=0)
    return stacked.mean(axis=0)


def class_auprc_weights(
    val_probs: Mapping[str, np.ndarray],
    y_true: np.ndarray,
    member_order: Sequence[str],
    class_names: Sequence[str] = CLASSES,
) -> np.ndarray:
    """w[model, class] from validation AUPRC only; columns sum to 1."""
    weights = np.zeros((len(member_order), len(class_names)), dtype=np.float64)
    for i, member in enumerate(member_order):
        for c, _name in enumerate(class_names):
            weights[i, c] = _safe_metric(average_precision_score, y_true[:, c], val_probs[member][:, c])
    weights = np.maximum(weights, 1e-8)
    weights = weights / weights.sum(axis=0, keepdims=True)
    return weights


def weighted_soft_vote(
    probs: Mapping[str, np.ndarray],
    weights: np.ndarray,
    member_order: Sequence[str],
) -> np.ndarray:
    stacked = np.stack([probs[m] for m in member_order], axis=0)
    return (stacked * weights[:, None, :]).sum(axis=0)


def fit_stacker(
    member_probs: Mapping[str, np.ndarray],
    y_true: np.ndarray,
    member_order: Sequence[str],
    class_names: Sequence[str] = CLASSES,
) -> Dict[str, LogisticRegression]:
    """Independent logistic regression per label. Fit on val (or OOF) only — never test."""
    y_true = np.asarray(y_true, dtype=np.int32)
    stackers: Dict[str, LogisticRegression] = {}
    for c, name in enumerate(class_names):
        x = np.column_stack([member_probs[m][:, c] for m in member_order])
        model = LogisticRegression(max_iter=2000, solver="lbfgs")
        model.fit(x, y_true[:, c])
        stackers[name] = model
    return stackers


def predict_stacker(
    stackers: Mapping[str, LogisticRegression],
    member_probs: Mapping[str, np.ndarray],
    member_order: Sequence[str],
    class_names: Sequence[str] = CLASSES,
) -> np.ndarray:
    cols = []
    for c, name in enumerate(class_names):
        x = np.column_stack([member_probs[m][:, c] for m in member_order])
        cols.append(stackers[name].predict_proba(x)[:, 1])
    return np.column_stack(cols)


def pairwise_prediction_correlation(probs: Mapping[str, np.ndarray], member_order: Sequence[str]) -> pd.DataFrame:
    mats = []
    labels = []
    for member in member_order:
        mats.append(probs[member].reshape(probs[member].shape[0], -1).mean(axis=1))
        labels.append(member)
    data = np.column_stack(mats)
    corr = np.corrcoef(data, rowvar=False)
    return pd.DataFrame(corr, index=labels, columns=labels)


def disagreement_rate(
    pred_by_model: Mapping[str, np.ndarray],
    member_order: Sequence[str],
) -> pd.DataFrame:
    n = next(iter(pred_by_model.values())).shape[0]
    labels = list(member_order)
    out = np.zeros((len(labels), len(labels)), dtype=np.float64)
    for i, a in enumerate(labels):
        for j, b in enumerate(labels):
            if i == j:
                continue
            out[i, j] = float((pred_by_model[a] != pred_by_model[b]).any(axis=1).mean())
    return pd.DataFrame(out, index=labels, columns=labels)


def error_overlap(
    y_true: np.ndarray,
    pred_by_model: Mapping[str, np.ndarray],
    member_order: Sequence[str],
) -> pd.DataFrame:
    """Jaccard of sample-level errors (any-class mismatch)."""
    errors = {m: (pred_by_model[m] != y_true).any(axis=1) for m in member_order}
    labels = list(member_order)
    out = np.zeros((len(labels), len(labels)), dtype=np.float64)
    for i, a in enumerate(labels):
        for j, b in enumerate(labels):
            union = np.logical_or(errors[a], errors[b]).sum()
            inter = np.logical_and(errors[a], errors[b]).sum()
            out[i, j] = float(inter / union) if union else 0.0
    return pd.DataFrame(out, index=labels, columns=labels)


def plot_per_class_confusion_2x2(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: Sequence[str] = CLASSES,
    title: str = "",
    save_path: Optional[PathLike] = None,
):
    """Five 2x2 confusion matrices (one per superclass)."""
    import matplotlib.pyplot as plt

    cms = per_class_confusion_2x2(y_true, y_pred, class_names)
    fig, axes = plt.subplots(1, len(class_names), figsize=(3.2 * len(class_names), 3.2))
    if len(class_names) == 1:
        axes = [axes]
    for ax, name in zip(axes, class_names):
        mat = np.array([[cms[name]["tn"], cms[name]["fp"]], [cms[name]["fn"], cms[name]["tp"]]], dtype=int)
        ax.imshow(mat, cmap="Blues")
        ax.set_xticks([0, 1], ["Pred 0", "Pred 1"])
        ax.set_yticks([0, 1], ["True 0", "True 1"])
        ax.set_title(name)
        for (i, j), value in np.ndenumerate(mat):
            ax.text(j, i, str(value), ha="center", va="center", color="black")
    if title:
        fig.suptitle(title)
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")
    return fig


# ---------------------------------------------------------------------------
# PyTorch dataset / trainer (imported by training notebooks)
# ---------------------------------------------------------------------------

def _require_torch():
    import torch
    from torch import nn
    from torch.utils.data import DataLoader, Dataset

    return torch, nn, DataLoader, Dataset


class ProcessedPTBXLDataset:
    """100 Hz processed tensors. Architecture-agnostic."""

    def __init__(
        self,
        X: np.ndarray,
        y: np.ndarray,
        ids: np.ndarray,
        patient_ids: Optional[np.ndarray] = None,
        transform: Optional[Callable[[np.ndarray], np.ndarray]] = None,
    ) -> None:
        torch, *_ = _require_torch()
        self.X = X
        self.y = y
        self.ids = ids
        if patient_ids is None:
            patient_ids = np.full(len(ids), -1, dtype=np.int64)
        self.patient_ids = np.asarray(patient_ids)
        self.transform = transform
        self._torch = torch

    def __len__(self) -> int:
        return int(self.y.shape[0])

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        torch = self._torch
        signal = np.asarray(self.X[idx], dtype=np.float32)
        if self.transform is not None:
            signal = self.transform(signal)
        return {
            "signal": torch.tensor(np.asarray(signal), dtype=torch.float32),
            "target": torch.tensor(np.asarray(self.y[idx]), dtype=torch.float32),
            "ecg_id": torch.tensor(int(self.ids[idx]), dtype=torch.long),
            "patient_id": torch.tensor(int(self.patient_ids[idx]), dtype=torch.long),
        }


def _load_patient_ids(processed_dir: Path, split: str, ecg_ids: np.ndarray) -> np.ndarray:
    npy_path = processed_dir / f"patient_ids_{split}.npy"
    if npy_path.exists():
        return np.load(npy_path, mmap_mode="r")
    index_path = processed_dir / "split_index.parquet"
    if index_path.exists():
        index = pd.read_parquet(index_path)
        lookup = dict(zip(index["ecg_id"].astype(int), index["patient_id"].astype(int)))
        return np.array([lookup.get(int(i), -1) for i in np.asarray(ecg_ids)], dtype=np.int64)
    return np.full(len(ecg_ids), -1, dtype=np.int64)


class ProcessedPTBXLDataModule:
    def __init__(
        self,
        processed_dir: PathLike,
        batch_size: int,
        num_workers: int = 2,
        transform: Optional[Callable[[np.ndarray], np.ndarray]] = None,
    ) -> None:
        torch, nn, DataLoader, Dataset = _require_torch()
        self._torch = torch
        self._DataLoader = DataLoader
        self.processed_dir = Path(processed_dir)
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.pin_memory = torch.cuda.is_available()
        self.transform = transform
        self.manifest = load_processed_manifest(self.processed_dir)
        self.classes = list(self.manifest.get("classes") or CLASSES)
        if self.classes != CLASSES:
            raise ValueError(f"Expected classes {CLASSES}, got {self.classes}")
        self.arrays: Dict[str, Dict[str, np.ndarray]] = {}
        for split in ("train", "val", "test"):
            info = self.manifest["splits"][split]
            ids = np.load(self.processed_dir / info["ids"], mmap_mode="r")
            self.arrays[split] = {
                "X": np.load(self.processed_dir / info["X"], mmap_mode="r"),
                "y": np.load(self.processed_dir / info["y"], mmap_mode="r"),
                "ids": ids,
                "patient_ids": _load_patient_ids(self.processed_dir, split, ids),
            }
        y_train = np.asarray(self.arrays["train"]["y"])
        self.pos_weight = torch.tensor(pos_weight_from_train(y_train), dtype=torch.float32)

    def _loader(self, split: str, shuffle: bool):
        data = self.arrays[split]
        dataset = ProcessedPTBXLDataset(
            data["X"],
            data["y"],
            data["ids"],
            patient_ids=data["patient_ids"],
            transform=self.transform,
        )
        return self._DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=shuffle,
            num_workers=self.num_workers,
            pin_memory=self.pin_memory,
        )

    def train_dataloader(self):
        return self._loader("train", True)

    def val_dataloader(self):
        return self._loader("val", False)

    def test_dataloader(self):
        return self._loader("test", False)


@dataclass
class EarlyStopping:
    patience: int = EARLY_STOPPING_PATIENCE
    mode: str = "max"
    monitor: str = PRIMARY_MONITOR
    min_delta: float = 0.0
    best_score: Optional[float] = None
    num_bad_epochs: int = 0
    stopped: bool = False

    def step(self, metrics: Dict[str, float]) -> bool:
        current = metrics[self.monitor]
        if self.best_score is None:
            self.best_score = current
            return False
        improvement = current - self.best_score if self.mode == "max" else self.best_score - current
        if improvement > self.min_delta:
            self.best_score = current
            self.num_bad_epochs = 0
        else:
            self.num_bad_epochs += 1
            if self.num_bad_epochs >= self.patience:
                self.stopped = True
        return self.stopped


@dataclass
class ModelCheckpoint:
    dirpath: str
    monitor: str = PRIMARY_MONITOR
    mode: str = "max"
    best_score: Optional[float] = None
    best_path: Optional[str] = None
    best_epoch: Optional[int] = None

    def _write(self, payload: dict, filename: str) -> str:
        import torch

        ensure_dir(self.dirpath)
        path = Path(self.dirpath) / filename
        torch.save(payload, path)
        return str(path)

    def save(self, model, optimizer, epoch, metrics, scheduler=None) -> str:
        payload = {
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "metrics": metrics,
        }
        if scheduler is not None:
            payload["scheduler_state_dict"] = scheduler.state_dict()
        last_path = self._write(payload, "last.pt")
        score = metrics[self.monitor]
        is_better = self.best_score is None
        if self.mode == "max":
            is_better = is_better or score > self.best_score
        else:
            is_better = is_better or score < self.best_score
        if is_better:
            self.best_score = score
            self.best_epoch = int(epoch)
            self.best_path = self._write(payload, "best.pt")
        return last_path


@dataclass
class ExperimentTracker:
    model_name: str
    output_root: str
    config: Dict[str, object]
    results_root: Optional[str] = None
    run_name: str = field(init=False)
    run_dir: Path = field(init=False)
    checkpoints_dir: Path = field(init=False)
    metrics_dir: Path = field(init=False)
    plots_dir: Path = field(init=False)
    predictions_dir: Path = field(init=False)
    history: List[Dict[str, float]] = field(default_factory=list)

    def __post_init__(self) -> None:
        seed = int(self.config.get("seed", 42))
        self.run_name = f"seed_{seed}"
        self.run_dir = ensure_dir(Path(self.output_root) / experiment_model_name(self.model_name) / self.run_name)
        self.checkpoints_dir = ensure_dir(self.run_dir / "checkpoints")
        self.metrics_dir = ensure_dir(self.run_dir / "metrics")
        self.plots_dir = ensure_dir(self.run_dir / "plots")
        self.predictions_dir = ensure_dir(self.run_dir / "predictions")
        dump_json(self.config, self.run_dir / "config.json")
        print("run_dir:", self.run_dir)

    def log_epoch(self, row: Dict[str, float]) -> None:
        self.history.append(row)

    def save_history(self) -> pd.DataFrame:
        history_df = pd.DataFrame(self.history)
        history_df.to_csv(self.metrics_dir / "history.csv", index=False)
        try:
            history_df.to_excel(self.metrics_dir / "history.xlsx", index=False)
        except Exception:
            pass
        return history_df

    def save_epoch_metrics(self, metrics: Dict[str, float], filename: str) -> None:
        dump_json(metrics, self.metrics_dir / filename)

    def save_predictions_standard(
        self,
        split: str,
        ecg_ids,
        patient_ids,
        y_true,
        y_prob,
        class_names,
        thresholds,
    ) -> pd.DataFrame:
        frame = build_prediction_frame(
            ecg_ids, patient_ids, y_true, y_prob, class_names=class_names, thresholds=thresholds
        )
        save_prediction_csv(frame, self.predictions_dir / f"{split}_predictions.csv")
        return frame

    def save_summary(self, summary: Dict[str, float]) -> None:
        dump_json(summary, self.metrics_dir / "summary.json")

    def plot_history(self) -> None:
        import matplotlib.pyplot as plt

        history_df = pd.DataFrame(self.history)
        if history_df.empty:
            return
        plots = [
            ("loss", ["train_loss", "val_loss"]),
            ("macro_auprc", ["train_macro_auprc", "val_macro_auprc"]),
            ("macro_auroc", ["train_macro_auroc", "val_macro_auroc"]),
        ]
        for stem, columns in plots:
            available = [col for col in columns if col in history_df.columns]
            if not available:
                continue
            plt.figure(figsize=(8, 5))
            for column in available:
                plt.plot(history_df["epoch"], history_df[column], label=column)
            plt.xlabel("Epoch")
            plt.ylabel(stem)
            plt.title(f"{self.model_name} {stem}")
            plt.legend()
            plt.tight_layout()
            plt.savefig(self.plots_dir / f"{stem}.png", dpi=150)
            plt.close()


class Trainer:
    def __init__(
        self,
        model,
        optimizer,
        criterion,
        device,
        class_names,
        tracker,
        checkpoint,
        early_stopping=None,
        scheduler=None,
        grad_clip_norm=None,
    ):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.class_names = list(class_names)
        self.tracker = tracker
        self.checkpoint = checkpoint
        self.early_stopping = early_stopping
        self.scheduler = scheduler
        self.grad_clip_norm = None if grad_clip_norm is None else float(grad_clip_norm)
        self.model.to(self.device)

    def _param_group_lrs(self) -> Dict[str, float]:
        groups = list(self.optimizer.param_groups)
        payload = {"lr": float(groups[0]["lr"])}
        if len(groups) > 1:
            payload["lr_backbone"] = float(groups[0]["lr"])
            payload["lr_head"] = float(groups[1]["lr"])
        return payload

    def _step_scheduler(self, metrics: Dict[str, float]) -> None:
        if self.scheduler is None:
            return
        import torch

        if isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
            self.scheduler.step(metrics[self.checkpoint.monitor])
        else:
            self.scheduler.step()

    def _run_epoch(self, dataloader, train: bool):
        import torch

        self.model.train(mode=train)
        losses, probs, targets, ecg_ids, patient_ids = [], [], [], [], []
        from tqdm.auto import tqdm

        for batch in tqdm(dataloader, leave=False):
            signals = batch["signal"].to(self.device)
            labels = batch["target"].to(self.device)
            ids = batch["ecg_id"].cpu().numpy()
            pids = batch.get("patient_id")
            pids = pids.cpu().numpy() if pids is not None else np.full(len(ids), -1)
            with torch.set_grad_enabled(train):
                logits = self.model(signals)
                loss = self.criterion(logits, labels)
                if train:
                    self.optimizer.zero_grad()
                    loss.backward()
                    if self.grad_clip_norm is not None:
                        torch.nn.utils.clip_grad_norm_(
                            [p for p in self.model.parameters() if p.requires_grad],
                            self.grad_clip_norm,
                        )
                    self.optimizer.step()
            losses.append(float(loss.item()))
            probs.append(torch.sigmoid(logits).detach().cpu().numpy())
            targets.append(labels.detach().cpu().numpy())
            ecg_ids.append(ids)
            patient_ids.append(pids)
        return (
            float(np.mean(losses)),
            np.concatenate(targets),
            np.concatenate(probs),
            np.concatenate(ecg_ids),
            np.concatenate(patient_ids),
        )

    def attach_run_dir(self, run_dir) -> None:
        run_dir = Path(run_dir)
        checkpoints_dir = run_dir / "checkpoints"
        last_path = checkpoints_dir / "last.pt"
        if not last_path.exists():
            raise FileNotFoundError(f"last.pt not found: {last_path}")
        self.tracker.run_dir = run_dir
        self.tracker.run_name = run_dir.name
        self.tracker.checkpoints_dir = ensure_dir(checkpoints_dir)
        self.tracker.metrics_dir = ensure_dir(run_dir / "metrics")
        self.tracker.plots_dir = ensure_dir(run_dir / "plots")
        self.tracker.predictions_dir = ensure_dir(run_dir / "predictions")
        self.checkpoint.dirpath = str(self.tracker.checkpoints_dir)
        print("attached run_dir:", run_dir)

    def _resolve_resume_run_dir(self, resume_run_dir=None) -> Path:
        if resume_run_dir:
            return Path(resume_run_dir)
        current_last = Path(self.checkpoint.dirpath) / "last.pt"
        if current_last.exists():
            return Path(self.tracker.run_dir)
        model_root = Path(self.tracker.output_root) / experiment_model_name(self.tracker.model_name)
        candidates = [p for p in model_root.glob("*/checkpoints/last.pt") if p.is_file()]
        if not candidates:
            raise FileNotFoundError(
                f"last.pt not found. run_dir={self.tracker.run_dir}  model_root={model_root}\n"
                "Pass the interrupted run path as RESUME_RUN_DIR."
            )
        newest = max(candidates, key=lambda p: p.stat().st_mtime)
        found = newest.parent.parent
        print("No last.pt in the current run folder; using the newest last.pt:", found)
        return found

    def _restore_history_and_monitors(self, last_epoch: int) -> None:
        import torch

        rows = []
        for epoch in range(1, last_epoch + 1):
            path = self.tracker.metrics_dir / f"epoch_{epoch:03d}.json"
            if path.exists():
                rows.append(json.loads(path.read_text(encoding="utf-8")))
        if not rows:
            csv_path = self.tracker.metrics_dir / "history.csv"
            if csv_path.exists():
                history_df = pd.read_csv(csv_path)
                history_df = history_df[history_df["epoch"] <= last_epoch]
                rows = history_df.to_dict("records")
        self.tracker.history = rows
        best_path = Path(self.checkpoint.dirpath) / "best.pt"
        if best_path.exists():
            best_payload = torch.load(best_path, map_location="cpu", weights_only=False)
            self.checkpoint.best_path = str(best_path)
            best_metrics = best_payload.get("metrics") or {}
            if self.checkpoint.monitor in best_metrics:
                self.checkpoint.best_score = best_metrics[self.checkpoint.monitor]
            self.checkpoint.best_epoch = int(best_payload.get("epoch", last_epoch))
        if self.early_stopping:
            self.early_stopping.best_score = None
            self.early_stopping.num_bad_epochs = 0
            self.early_stopping.stopped = False
            for row in self.tracker.history:
                self.early_stopping.step(row)

    def _move_optimizer_to_device(self) -> None:
        import torch

        for state in self.optimizer.state.values():
            for key, value in state.items():
                if torch.is_tensor(value):
                    state[key] = value.to(self.device)

    def load_last(self, last_path=None) -> int:
        import torch

        path = Path(last_path) if last_path else Path(self.checkpoint.dirpath) / "last.pt"
        if not path.exists():
            raise FileNotFoundError(f"last.pt not found: {path}")
        payload = torch.load(path, map_location="cpu", weights_only=False)
        self.model.load_state_dict(payload["model_state_dict"])
        self.model.to(self.device)
        try:
            self.optimizer.load_state_dict(payload["optimizer_state_dict"])
        except (ValueError, RuntimeError) as exc:
            raise ValueError(
                "last.pt optimizer state does not match this trainer. "
                "Do not resume an incompatible checkpoint; start fit from scratch."
            ) from exc
        self._move_optimizer_to_device()
        if self.scheduler is not None and payload.get("scheduler_state_dict"):
            self.scheduler.load_state_dict(payload["scheduler_state_dict"])
        last_epoch = int(payload["epoch"])
        self._restore_history_and_monitors(last_epoch)
        metrics = payload.get("metrics") or {}
        if metrics and (not self.tracker.history or int(self.tracker.history[-1].get("epoch", -1)) < last_epoch):
            self.tracker.history.append(metrics)
            if self.early_stopping:
                self.early_stopping.step(metrics)
        print(
            f"resume last.pt epoch={last_epoch}  next={last_epoch + 1}  "
            f"run_dir={self.tracker.run_dir}"
        )
        return last_epoch + 1

    def _load_best_weights(self) -> None:
        import torch

        ckpt_dir = Path(self.checkpoint.dirpath)
        if self.checkpoint.best_path and Path(self.checkpoint.best_path).exists():
            best_path = Path(self.checkpoint.best_path)
        elif (ckpt_dir / "best.pt").exists():
            best_path = ckpt_dir / "best.pt"
        else:
            best_path = ckpt_dir / "last.pt"
        if not best_path.exists():
            raise FileNotFoundError(f"best.pt/last.pt not found: {ckpt_dir}")
        payload = torch.load(best_path, map_location="cpu", weights_only=False)
        self.model.load_state_dict(payload["model_state_dict"])
        self.model.to(self.device)
        print(f"loaded weights from {best_path} epoch={payload.get('epoch')}")

    def fit(
        self,
        train_loader,
        val_loader,
        epochs: int = MAX_EPOCHS,
        resume_from_last: bool = False,
        resume_run_dir=None,
    ) -> pd.DataFrame:
        start_epoch = 1
        if resume_from_last:
            self.attach_run_dir(self._resolve_resume_run_dir(resume_run_dir))
            start_epoch = self.load_last()
            if start_epoch > epochs or (self.early_stopping and self.early_stopping.stopped):
                if start_epoch > epochs:
                    print(f"already finished: last epoch {start_epoch - 1} >= epochs {epochs}")
                else:
                    print("early stopping already triggered; nothing to resume")
                history_df = self.tracker.save_history()
                self.tracker.plot_history()
                self._load_best_weights()
                return history_df
        import time

        for epoch in range(start_epoch, epochs + 1):
            t0 = time.perf_counter()
            train_loss, y_train, p_train, _, _ = self._run_epoch(train_loader, train=True)
            val_loss, y_val, p_val, _, _ = self._run_epoch(val_loader, train=False)
            epoch_duration = float(time.perf_counter() - t0)
            # Checkpoint metric is probability-based (AUPRC); 0.5 F1 is logged only.
            train_metrics = compute_multilabel_metrics(y_train, p_train, self.class_names, thresholds=0.5)
            val_metrics = compute_multilabel_metrics(y_val, p_val, self.class_names, thresholds=0.5)
            epoch_row = {
                "epoch": epoch,
                "train_loss": train_loss,
                "val_loss": val_loss,
                "epoch_duration": epoch_duration,
                **self._param_group_lrs(),
                **{f"train_{k}": v for k, v in train_metrics.items()},
                **{f"val_{k}": v for k, v in val_metrics.items()},
            }
            self.tracker.log_epoch(epoch_row)
            self._step_scheduler(epoch_row)
            self.checkpoint.save(
                self.model, self.optimizer, epoch, epoch_row, scheduler=self.scheduler
            )
            self.tracker.save_epoch_metrics(epoch_row, f"epoch_{epoch:03d}.json")
            self.tracker.save_history()
            lr = float(self._param_group_lrs()["lr"])
            print(
                f"epoch {epoch:03d}  train_loss={train_loss:.4f}  val_loss={val_loss:.4f}  "
                f"train_macro_auprc={epoch_row['train_macro_auprc']:.4f}  "
                f"val_macro_auprc={epoch_row['val_macro_auprc']:.4f}  "
                f"lr={lr:.2e}  epoch_duration={epoch_duration:.1f}s"
            )
            if self.early_stopping and self.early_stopping.step(epoch_row):
                print("early stopping")
                break
        history_df = self.tracker.save_history()
        self.tracker.plot_history()
        self._load_best_weights()  # restore best val macro-AUPRC checkpoint
        return history_df

    def predict_split(self, dataloader):
        loss, y_true, y_prob, ecg_ids, patient_ids = self._run_epoch(dataloader, train=False)
        return {
            "loss": loss,
            "y_true": y_true,
            "y_prob": y_prob,
            "ecg_id": ecg_ids,
            "patient_id": patient_ids,
        }

    def evaluate_with_protocol(
        self,
        val_loader,
        test_loader=None,
        evaluate_test: bool = EVALUATE_TEST,
        results_root: Optional[PathLike] = None,
    ) -> Dict[str, Any]:
        """Val thresholds; reported metrics on test when evaluate_test=True. Test is never used for threshold/checkpoint selection."""
        val_out = self.predict_split(val_loader)
        thresholds = optimize_thresholds_f1(val_out["y_true"], val_out["y_prob"], self.class_names)
        dump_json(thresholds, self.tracker.run_dir / "thresholds.json")
        val_metrics = compute_multilabel_metrics(
            val_out["y_true"],
            val_out["y_prob"],
            self.class_names,
            thresholds=threshold_vector(thresholds, self.class_names),
        )
        val_metrics["val_loss"] = val_out["loss"]
        self.tracker.save_predictions_standard(
            "val",
            val_out["ecg_id"],
            val_out["patient_id"],
            val_out["y_true"],
            val_out["y_prob"],
            self.class_names,
            thresholds,
        )
        self.tracker.save_epoch_metrics(val_metrics, "val_summary.json")

        summary = {
            "best_epoch": self.checkpoint.best_epoch,
            "best_validation_macro_auprc": self.checkpoint.best_score,
            "class_thresholds": thresholds,
            "val": val_metrics,
        }
        if evaluate_test:
            if test_loader is None:
                raise ValueError("EVALUATE_TEST=True but test_loader is None")
            test_out = self.predict_split(test_loader)
            test_metrics = compute_multilabel_metrics(
                test_out["y_true"],
                test_out["y_prob"],
                self.class_names,
                thresholds=threshold_vector(thresholds, self.class_names),
            )
            test_metrics["test_loss"] = test_out["loss"]
            self.tracker.save_predictions_standard(
                "test",
                test_out["ecg_id"],
                test_out["patient_id"],
                test_out["y_true"],
                test_out["y_prob"],
                self.class_names,
                thresholds,
            )
            self.tracker.save_epoch_metrics(test_metrics, "test_summary.json")
            self.tracker.save_summary(test_metrics)
            summary["test"] = test_metrics
        else:
            self.tracker.save_summary(val_metrics)
            print("EVALUATE_TEST=False — test fold 10 was not scored.")

        dump_json(summary, self.tracker.metrics_dir / "protocol_summary.json")
        if results_root is None:
            results_root = self.tracker.results_root
        if results_root:
            sync_standard_results(
                self.tracker.run_dir,
                results_root,
                self.tracker.model_name,
                int(self.tracker.config.get("seed", 42)),
            )
        return summary


@dataclass
class ExperimentConfig:
    model_name: str
    processed_dir: str
    output_root: str
    learning_rate: float = 1e-3
    weight_decay: float = 1e-4
    epochs: int = MAX_EPOCHS
    batch_size: int = 64
    sampling_rate: int = SAMPLING_RATE
    num_workers: int = 2
    seed: int = 42
    patience: int = EARLY_STOPPING_PATIENCE
    monitor: str = PRIMARY_MONITOR
    evaluate_test: bool = EVALUATE_TEST
    results_root: Optional[str] = None
    extra: Dict[str, object] = field(default_factory=dict)

    def flat_dict(self) -> Dict[str, object]:
        payload = {
            "model_name": self.model_name,
            "processed_dir": self.processed_dir,
            "output_root": self.output_root,
            "results_root": self.results_root,
            "learning_rate": self.learning_rate,
            "weight_decay": self.weight_decay,
            "epochs": self.epochs,
            "batch_size": self.batch_size,
            "sampling_rate": self.sampling_rate,
            "num_workers": self.num_workers,
            "seed": self.seed,
            "patience": self.patience,
            "monitor": self.monitor,
            "evaluate_test": self.evaluate_test,
            "loss": "BCEWithLogitsLoss",
            "optimizer": "AdamW",
            "train_folds": list(TRAIN_FOLDS),
            "val_fold": list(VAL_FOLDS),
            "test_fold": list(TEST_FOLDS),
            "classes": list(CLASSES),
            "primary_metric": PRIMARY_METRIC,
            **self.extra,
        }
        return payload


def load_standard_predictions(
    results_dir: PathLike,
    model_key: str,
    seed: int,
    split: str = "val",
) -> Tuple[pd.DataFrame, np.ndarray, np.ndarray, np.ndarray]:
    path = seed_results_dir(results_dir, model_key, seed) / f"{split}_predictions.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing {split} predictions: {path}")
    return load_predictions(path)


def _is_head_param(name: str, head_key: str) -> bool:
    return name == head_key or name.startswith(f"{head_key}.")


def _adamw_param_groups(model, learning_rate: float, extra: Mapping[str, Any]):
    """Single group, or backbone/head groups when extra['backbone_lr'] is set."""
    head_key = str(extra.get("head_param_key") or "dense")
    backbone_lr = extra.get("backbone_lr")
    head_params = []
    backbone_params = []
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        if _is_head_param(name, head_key):
            head_params.append(param)
        else:
            backbone_params.append(param)
    if backbone_lr is not None and backbone_params and head_params:
        return [
            {"params": backbone_params, "lr": float(backbone_lr)},
            {"params": head_params, "lr": float(learning_rate)},
        ]
    trainable = backbone_params + head_params
    if not trainable:
        raise ValueError("No trainable parameters")
    return [{"params": trainable, "lr": float(learning_rate)}]


def _maybe_plateau_scheduler(optimizer, experiment_config: ExperimentConfig):
    extra = dict(experiment_config.extra or {})
    if str(extra.get("scheduler") or "").lower() != "plateau":
        return None
    import torch

    mode = str(extra.get("scheduler_mode") or "max")
    monitor = str(experiment_config.monitor)
    if "scheduler_mode" not in extra and "loss" in monitor and "auprc" not in monitor and "auroc" not in monitor:
        mode = "min"
    min_lr = extra.get("scheduler_min_lr", 1e-6)
    if isinstance(min_lr, (list, tuple)):
        min_lr = [float(v) for v in min_lr]
    else:
        min_lr = float(min_lr)
    return torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,
        mode=mode,
        factor=float(extra.get("scheduler_factor", 0.1)),
        patience=int(extra.get("scheduler_patience", 3)),
        min_lr=min_lr,
    )


def build_trainer(
    experiment_config: ExperimentConfig,
    model_factory: Callable[[int], Any],
    data_module: Optional[ProcessedPTBXLDataModule] = None,
):
    import torch
    from torch import nn

    set_seed(experiment_config.seed)
    if data_module is None:
        data_module = ProcessedPTBXLDataModule(
            processed_dir=Path(experiment_config.processed_dir),
            batch_size=experiment_config.batch_size,
            num_workers=experiment_config.num_workers,
        )
    manifest_fs = data_module.manifest.get("sampling_rate") if getattr(data_module, "manifest", None) else None
    if manifest_fs is not None and int(manifest_fs) != int(experiment_config.sampling_rate):
        raise ValueError(
            f"Manifest fs={manifest_fs} != config fs={experiment_config.sampling_rate}"
        )
    extra = dict(experiment_config.extra or {})
    model = model_factory(len(data_module.classes))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    criterion = nn.BCEWithLogitsLoss(pos_weight=data_module.pos_weight.to(device))
    optimizer = torch.optim.AdamW(
        _adamw_param_groups(model, experiment_config.learning_rate, extra),
        lr=experiment_config.learning_rate,
        weight_decay=experiment_config.weight_decay,
    )
    scheduler = _maybe_plateau_scheduler(optimizer, experiment_config)
    grad_clip_norm = extra.get("grad_clip_norm")
    tracker = ExperimentTracker(
        model_name=experiment_config.model_name,
        output_root=experiment_config.output_root,
        results_root=experiment_config.results_root,
        config=experiment_config.flat_dict(),
    )
    checkpoint = ModelCheckpoint(dirpath=str(tracker.checkpoints_dir), monitor=experiment_config.monitor)
    early_stopping = EarlyStopping(patience=experiment_config.patience, monitor=experiment_config.monitor)
    trainer = Trainer(
        model=model,
        optimizer=optimizer,
        criterion=criterion,
        device=device,
        class_names=data_module.classes,
        tracker=tracker,
        checkpoint=checkpoint,
        early_stopping=early_stopping,
        scheduler=scheduler,
        grad_clip_norm=grad_clip_norm,
    )
    return trainer, data_module


def finalize_run_config(trainer: Trainer, extra: Optional[Mapping[str, Any]] = None) -> Dict[str, Any]:
    cfg = dict(trainer.tracker.config)
    cfg.update(
        {
            "best_epoch": trainer.checkpoint.best_epoch,
            "best_validation_macro_auprc": trainer.checkpoint.best_score,
        }
    )
    thresholds_path = trainer.tracker.run_dir / "thresholds.json"
    if thresholds_path.exists():
        cfg["class_thresholds"] = load_json(thresholds_path)
    if extra:
        cfg.update(dict(extra))
    dump_json(cfg, trainer.tracker.run_dir / "config.json")
    return cfg


# ---------------------------------------------------------------------------
# Standalone best.pt analysis (notebooks 01-04, no cells above required)
# ---------------------------------------------------------------------------

ARCHITECTURE_CELL_MARKER = "# MODEL_ARCHITECTURE"
ANALYZE_CELL_MARKER = "ANALYZE_FROM_BEST_PT"


def extra_from_run_config(cfg: Mapping[str, Any]) -> Dict[str, Any]:
    """Hyperparams live in config['extra'] or flattened at the top level (ExperimentConfig.flat_dict)."""
    nested = cfg.get("extra")
    if isinstance(nested, Mapping) and nested:
        return dict(nested)
    return dict(cfg)


def best_pt_path(run_dir: PathLike) -> Path:
    path = Path(run_dir) / "checkpoints" / "best.pt"
    if not path.exists():
        raise FileNotFoundError(f"best.pt not found: {path}")
    return path


def load_best_pt(run_dir: PathLike, map_location="cpu") -> Dict[str, Any]:
    import torch

    path = best_pt_path(run_dir)
    return torch.load(path, map_location=map_location, weights_only=False)


def exec_notebook_cells(nb_path: PathLike, marker: str, namespace: Optional[dict] = None) -> int:
    """Execute code cells in an .ipynb whose source contains `marker`."""
    path = Path(nb_path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    ns = namespace if namespace is not None else {}
    executed = 0
    for idx, cell in enumerate(payload.get("cells") or []):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source") or ""
        if isinstance(src, list):
            src = "".join(src)
        if marker not in src or ANALYZE_CELL_MARKER in src:
            continue
        exec(compile(src, f"{path.name}:cell{idx}", "exec"), ns)
        executed += 1
    if executed == 0:
        raise RuntimeError(f"No code cell with {marker!r} in {path}")
    return executed


def predict_model_split(model, dataloader, device, criterion=None) -> Dict[str, Any]:
    """Eval-mode inference. Returns loss / y_true / y_prob / ecg_id / patient_id."""
    import torch
    from tqdm.auto import tqdm

    model.eval()
    losses, probs, targets, ecg_ids, patient_ids = [], [], [], [], []
    with torch.no_grad():
        for batch in tqdm(dataloader, leave=False):
            signals = batch["signal"].to(device)
            labels = batch["target"].to(device)
            ids = batch["ecg_id"].cpu().numpy()
            pids = batch.get("patient_id")
            pids = pids.cpu().numpy() if pids is not None else np.full(len(ids), -1)
            logits = model(signals)
            if criterion is not None:
                losses.append(float(criterion(logits, labels).item()))
            probs.append(torch.sigmoid(logits).detach().cpu().numpy())
            targets.append(labels.detach().cpu().numpy())
            ecg_ids.append(ids)
            patient_ids.append(pids)
    return {
        "loss": float(np.mean(losses)) if losses else float("nan"),
        "y_true": np.concatenate(targets),
        "y_prob": np.concatenate(probs),
        "ecg_id": np.concatenate(ecg_ids),
        "patient_id": np.concatenate(patient_ids),
    }


def _display_split_analysis(
    split: str,
    model_name: str,
    seed: int,
    y_true: np.ndarray,
    y_prob: np.ndarray,
    class_names: Sequence[str],
    thresholds: Mapping[str, float],
    results_seed: Path,
) -> Dict[str, float]:
    from IPython.display import Markdown, display
    import matplotlib.pyplot as plt

    names = list(class_names)
    thr = threshold_vector(thresholds, names)
    metrics = compute_multilabel_metrics(y_true, y_prob, names, thresholds=thr)
    y_pred = apply_thresholds(y_prob, thr)
    if split == "val":
        title_split = "Validation fold 9 (threshold fit, not reported)"
    else:
        title_split = "Test fold 10 (reported)"
    display(Markdown(f"#### {title_split} | seed={seed} | best.pt"))
    display(pd.DataFrame([summary_table_row(model_name, metrics)]))
    display(Markdown(f"#### Per-class {split}"))
    display(per_class_metrics_table(metrics, names))
    fig = plot_per_class_confusion_2x2(
        y_true,
        y_pred,
        names,
        title=f"{title_split} 2x2 CM | {model_name} seed={seed} (best.pt)",
        save_path=results_seed / f"{split}_cm_2x2.png",
    )
    plt.show()
    plt.close(fig)
    return metrics


def evaluate_and_display_best_pt(
    model_factory: Callable[[int], Any],
    run_dir: PathLike,
    processed_dir: Optional[PathLike] = None,
    results_root: Optional[PathLike] = None,
    evaluate_test: bool = EVALUATE_TEST,
    batch_size: Optional[int] = None,
    num_workers: int = 2,
) -> Dict[str, Any]:
    """Load checkpoints/best.pt, fit F1 thresholds on val, report tables/CM on test when evaluate_test=True."""
    import torch
    from torch import nn

    run_dir = Path(run_dir)
    ckpt_path = best_pt_path(run_dir)
    cfg_path = run_dir / "config.json"
    cfg = load_json(cfg_path) if cfg_path.exists() else {}
    model_name = str(cfg.get("model_name") or run_dir.parent.name)
    seed = int(cfg.get("seed") or int(str(run_dir.name).split("_")[-1]))
    processed = Path(processed_dir or cfg.get("processed_dir") or "")
    if not processed.exists():
        raise FileNotFoundError(f"processed_dir not found: {processed}")
    fallback_results = run_dir.parents[2] / "results" if len(run_dir.parents) >= 3 else Path("results")
    results_root = Path(results_root or cfg.get("results_root") or fallback_results)
    batch_size = int(batch_size or cfg.get("batch_size") or 64)
    num_workers = int(cfg.get("num_workers") or num_workers)

    set_seed(seed)
    data_module = ProcessedPTBXLDataModule(
        processed_dir=processed,
        batch_size=batch_size,
        num_workers=num_workers,
    )
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model_factory(len(data_module.classes))
    payload = torch.load(ckpt_path, map_location="cpu", weights_only=False)
    model.load_state_dict(payload["model_state_dict"])
    model.to(device)
    model.eval()
    best_epoch = payload.get("epoch")
    best_monitor = (payload.get("metrics") or {}).get(PRIMARY_MONITOR)
    print(
        f"best.pt={ckpt_path} | epoch={best_epoch} | {PRIMARY_MONITOR}={best_monitor} | device={device}"
    )

    criterion = nn.BCEWithLogitsLoss(pos_weight=data_module.pos_weight.to(device))
    val_out = predict_model_split(model, data_module.val_dataloader(), device, criterion)
    thresholds = optimize_thresholds_f1(val_out["y_true"], val_out["y_prob"], data_module.classes)
    dump_json(thresholds, run_dir / "thresholds.json")
    pred_dir = ensure_dir(run_dir / "predictions")
    metrics_dir = ensure_dir(run_dir / "metrics")
    save_prediction_csv(
        build_prediction_frame(
            val_out["ecg_id"],
            val_out["patient_id"],
            val_out["y_true"],
            val_out["y_prob"],
            class_names=data_module.classes,
            thresholds=thresholds,
        ),
        pred_dir / "val_predictions.csv",
    )
    val_metrics = compute_multilabel_metrics(
        val_out["y_true"],
        val_out["y_prob"],
        data_module.classes,
        thresholds=threshold_vector(thresholds, data_module.classes),
    )
    val_metrics["val_loss"] = val_out["loss"]
    dump_json(val_metrics, metrics_dir / "val_summary.json")

    results_seed = ensure_dir(seed_results_dir(results_root, model_name, seed))
    _display_split_analysis(
        "val",
        model_name,
        seed,
        val_out["y_true"],
        val_out["y_prob"],
        data_module.classes,
        thresholds,
        results_seed,
    )

    summary: Dict[str, Any] = {
        "best_epoch": best_epoch,
        "best_validation_macro_auprc": best_monitor,
        "checkpoint": str(ckpt_path),
        "class_thresholds": thresholds,
        "val": val_metrics,
    }
    if evaluate_test:
        test_out = predict_model_split(model, data_module.test_dataloader(), device, criterion)
        test_metrics = compute_multilabel_metrics(
            test_out["y_true"],
            test_out["y_prob"],
            data_module.classes,
            thresholds=threshold_vector(thresholds, data_module.classes),
        )
        test_metrics["test_loss"] = test_out["loss"]
        save_prediction_csv(
            build_prediction_frame(
                test_out["ecg_id"],
                test_out["patient_id"],
                test_out["y_true"],
                test_out["y_prob"],
                class_names=data_module.classes,
                thresholds=thresholds,
            ),
            pred_dir / "test_predictions.csv",
        )
        dump_json(test_metrics, metrics_dir / "test_summary.json")
        dump_json(test_metrics, metrics_dir / "summary.json")
        summary["test"] = test_metrics
        _display_split_analysis(
            "test",
            model_name,
            seed,
            test_out["y_true"],
            test_out["y_prob"],
            data_module.classes,
            thresholds,
            results_seed,
        )
    else:
        dump_json(val_metrics, metrics_dir / "summary.json")

    dump_json(summary, metrics_dir / "protocol_summary.json")
    synced = sync_standard_results(run_dir, results_root, model_name, seed)
    print("wrote predictions:")
    print(" ", pred_dir / "val_predictions.csv")
    print(" ", synced / "val_predictions.csv")
    if evaluate_test:
        print(" ", pred_dir / "test_predictions.csv")
        print(" ", synced / "test_predictions.csv")
    else:
        print("EVALUATE_TEST=False — fold 10 test metrics/predictions are not written.")
    return summary
