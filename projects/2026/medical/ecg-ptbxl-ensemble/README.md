# Multi-Label 12-Lead ECG Classification on PTB-XL

**Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative
Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches**

Yunus Emre Mert, Ece Akdoğan, Hüseyin Üvet — Yıldız Technical University

- arXiv: [2609.12803](https://arxiv.org/abs/2609.12803) (eess.SP, Sep 2026)
- PDF: [`2609.12803v1.pdf`](paper/2609.12803v1.pdf)
- Context: R&D work carried out at **Cormetry Health** (wearable 12-lead ECG).

> **Türkçe özet:** PTB-XL v1.0.3 üzerinde 5 tanısal üst sınıf (`NORM`, `MI`, `STTC`, `CD`, `HYP`) için çok etiketli 12 derivasyon EKG sınıflandırması. 1D-ResNet18, Bidirectional Mamba, xLSTM, CWT-ViT-KAN ve ECGFounder karşılaştırıldı; heterojen ensemble (soft voting, stacking) uygulandı. En iyi sonuç stacking ile Macro AUROC **0.936**, AUPRC **0.836**. Veri seti rehberi: [ptbxl-dataset-guide.md](docs/ptbxl-dataset-guide.md).

## Results (PTB-XL test fold 10)

| Model | Macro AUROC | Macro AUPRC | Macro F1 | Subset Acc. | Hamming Loss |
|---|---|---|---|---|---|
| 1D-ResNet18 | 0.922 | 0.797 | 0.738 | 0.573 | 0.128 |
| Bidirectional Mamba | 0.923 | 0.816 | 0.739 | 0.583 | 0.126 |
| xLSTM | 0.910 | 0.782 | 0.718 | 0.574 | 0.130 |
| CWT-ViT-KAN | 0.874 | 0.709 | 0.664 | 0.497 | 0.165 |
| ECGFounder (fine-tune, 500 Hz) | 0.930 | 0.823 | 0.749 | 0.602 | 0.116 |
| Equal-Weight Soft Voting | 0.933 | 0.829 | 0.759 | 0.625 | 0.112 |
| Validation-Weighted Soft Voting | 0.933 | 0.830 | 0.760 | **0.630** | 0.111 |
| Stacking Ensemble | **0.936** | **0.836** | **0.763** | 0.625 | **0.110** |

Protocol: official `strat_fold` split (train 1–8, val 9, test 10), macro-AUPRC
model selection, val-only F1-max thresholds, seed 42.

## Folder layout

```
ecg-ptbxl-ensemble/
  README.md
  notebooks/   00–06 Colab notebooks + ecg_common.py (shared protocol)
  paper/       arXiv PDF
  docs/        PTB-XL dataset guide
```

# Notebooks 00–06

Colab pipeline for multi-label PTB-XL diagnostic superclass classification
(`NORM`, `MI`, `STTC`, `CD`, `HYP`). Run these notebooks in order. Shared
protocol lives in [`ecg_common.py`](notebooks/ecg_common.py). Dataset details (WFDB paths,
SCP codes, folds) are in the PTB-XL guide [ptbxl-dataset-guide.md](docs/ptbxl-dataset-guide.md).

## Run order

```
00 process  →  01 / 02 / 02.1 / 03 / 04 train  →  05 ensemble  →  06 figures
```

| Notebook | Role | Reads | Writes |
|---|---|---|---|
| [`00_ptbxl_colab_process.ipynb`](notebooks/00_ptbxl_colab_process.ipynb) | Unzip PTB-XL 1.0.3, map SCP → superclasses, export tensors | `PTB-XL.zip`, Drive `data/` | `processed/sr100/`, `processed/sr500/` |
| [`01_resnet18_1d_baseline.ipynb`](notebooks/01_resnet18_1d_baseline.ipynb) | 1D-ResNet18 baseline | `processed/sr100` | `experiments/resnet18_1d/`, `results/resnet18/` |
| [`02_bidirectional_mamba_ssm.ipynb`](notebooks/02_bidirectional_mamba_ssm.ipynb) | Bidirectional Mamba | `processed/sr100` | `experiments/bidirectional_mamba/`, `results/mamba/` |
| [`02.1_xlstm.ipynb`](notebooks/02.1_xlstm.ipynb) | xLSTM (sLSTM / mLSTM) | `processed/sr100` | `experiments/xlstm/`, `results/xlstm/` |
| [`03_wavelet_kan_cwt_vit.ipynb`](notebooks/03_wavelet_kan_cwt_vit.ipynb) | CWT + ViT + KAN | `processed/sr100` | `experiments/wavelet_kan_cwt_vit/`, `results/cwt_vit_kan/` |
| [`04_ecgfounder_500.ipynb`](notebooks/04_ecgfounder_500.ipynb) | ECGFounder native 500 Hz fine-tune | `processed/sr500` | `experiments/ecgfounder_500/`, `results/ecgfounder/` |
| [`05_heterogeneous_ensemble.ipynb`](notebooks/05_heterogeneous_ensemble.ipynb) | Equal / weighted vote + stacking | `results/<member>/` | `results/equal_soft_voting/` (and siblings) |
| [`06_visualize_experiment_results.ipynb`](notebooks/06_visualize_experiment_results.ipynb) | Paper tables and figures | `results/` | `paper/results_figures/`, `paper/results_tables/` |

Keep **02.1**. It is a first-class ensemble member; 05/06 expect all five models.

## Dual cache (notebook 00)

Notebook 00 writes **both** caches from the same official `strat_fold` split
(train 1–8, val 9, test 10), the same Butterworth band-pass 0.5–40 Hz, and the
same train-only lead-wise mean/std:

| Cache | Source | Shape | Used by |
|---|---|---|---|
| `processed/sr100/` | `filename_lr` / `records100` | `(N, 12, 1000)` | 01, 02, 02.1, 03 |
| `processed/sr500/` | `filename_hr` / `records500` | `(N, 12, 5000)` | 04 ECGFounder |

ECGFounder is pretrained at 5000 samples. This pipeline feeds it **native**
500 Hz tensors. Training notebooks do **not** interpolate and do **not**
re-read WFDB. For speed, 00 copies `records100` / `records500` once to Colab
SSD (`/content/ptbxl_local`) and exports with a process pool; training always
reads the Drive memmaps.

Skip a rate when its `manifest.json` is valid. Rebuild with `FORCE_REBUILD=True`
or `FORCE_REBUILD_RATES = (500,)`.

## Shared protocol (`ecg_common.py`)

Architectures stay in the notebooks. This module owns:

- Official folds, patient-disjoint asserts, PTB-XL 1.0.3 checks
- `ProcessedPTBXLDataModule` over the memmap caches (100 Hz or 500 Hz)
- Trainer, early stopping, `best.pt` / `last.pt`
- Primary metric **macro-AUPRC** on val fold 9 (`val_macro_auprc`)
- Val-only F1-max thresholds; reported scores on **test fold 10**
- Standard prediction CSVs and `results/<canonical>/seed_<seed>/` layout
- Ensemble helpers (soft vote, AUPRC weights, per-label stacking)

Canonical keys used by 05/06:

```
resnet18, xlstm, mamba, cwt_vit_kan, ecgfounder
equal_soft_voting, weighted_soft_voting, stacking
```

`ecgfounder` maps to experiments folder `ecgfounder_500` and results folder
`results/ecgfounder/`.

## Training notebook skeleton (01–04)

Same cell order in every training notebook:

1. Title + GPU note
2. `pip install`
3. Drive mount + `load_processed_manifest`
4. Shared protocol import (`ExperimentConfig`, `build_trainer`, …)
5. Model (`# MODEL_ARCHITECTURE`)
6. Training hyperparameters
7. `fit` (fresh run)
8. Resume from `last.pt`
9. Performance analysis (`# ANALYZE_FROM_BEST_PT`)

Notebook 04 adds an ECGFounder setup cell (clone PKU repo + HuggingFace
`12_lead_ECGFounder.pth`) and wraps Net1D with `ECGFounder500HzWrapper`
(per-record global z-score, no interpolate).

### Resume

If Colab disconnects, skip the `fit` cell. Re-run install / paths / protocol /
model / `ExperimentConfig`, then the resume cell. It loads `last.pt` (weights +
optimizer) into the same `experiments/<model>/seed_<seed>/` folder. Notebook 04
refuses interpolate checkpoints (`sr100_linear_interpolate_1000_to_5000`).

### Standalone analysis

The last section is marked `# ANALYZE_FROM_BEST_PT`. Restart the runtime and
run **only that cell**: it installs deps, mounts Drive, rebuilds the architecture
from the notebook, loads `best.pt`, fits thresholds on val fold 9, and writes
test-fold metrics plus `results/<canonical>/seed_42/`.

## Colab paths

```
/content/drive/MyDrive/ECG AI/
  PTB-XL.zip
  data/ptb-xl-...-dataset-1.0.3/     # unzipped by 00
  processed/sr100/                   # 01–03 / 02.1
  processed/sr500/                   # 04
  experiments/<model>/seed_<seed>/
  results/<canonical>/seed_<seed>/
  notebooks/ecg_common.py
```

Runnable cells use `/content/drive/MyDrive/ECG AI` only (no Windows paths).
Colab cwd is `/content`, so notebooks do `sys.path.insert(0, str(PROJECT_DIR / 'notebooks'))`.

## Typical Colab session

1. GPU runtime for 01–04 (A100 preferred for 04; T4 is enough for ResNet18).
   CPU is enough for 00 (export), 05, and 06.
2. Run 00 through **Verify**. Confirm both `processed/sr100` and
   `processed/sr500` manifests exist.
3. Train 01, 02, 02.1, 03, 04. After each `fit`, run **Performance analysis**
   with `EVALUATE_TEST=True` so `test_predictions.csv` exists.
4. Run 05 (needs all five member prediction files for the same seed).
5. Run 06 for paper tables/figures.
