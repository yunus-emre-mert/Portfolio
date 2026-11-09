# Yunus Emre Mert

**Backend Engineer**

[🇹🇷 Türkçe (README.tr.md)](README.tr.md)

[LinkedIn](https://www.linkedin.com/in/yunus-emre-mert) · [GitHub](https://github.com/yunus-emre-mert)

---

## Summary

**Backend Engineer** with domain expertise in Medical AI and scalable data pipelines. I design service boundaries, data contracts, and the infrastructure that keeps multi-tenant clinical systems isolated and fast under load.

At **Clinovatech** I owned the architecture of a multi-tenant B2B SaaS backend for clinics: **PostgreSQL row-level security (RLS)** for tenant isolation, a package-and-module authorization model, **FastAPI** request contracts, **Redis** on read-heavy paths, and **RabbitMQ / Celery** for work that stays off the request path. At **Cormetry Health** (2024 – November 2026) I designed the platform API and the device-to-cloud path for a wearable 12-lead ECG: BLE ingestion, real-time signal validation pipelines, and clinical data workflows that feed both product features and model evaluation. Commercial **source code is not in this repo** under **IP and NDA**.

| Focus (2024 – present) | Summary |
|------------------------|---------|
| **Clinovatech — system design** | Software Engineer (Backend & Systems), Contract. Multi-tenant B2B SaaS: RLS tenant isolation, package/module authorization, FastAPI + Pydantic contracts, SQLAlchemy/Alembic, Redis, RabbitMQ, Celery, pytest — [case study](projects/2026/saas/clinovatech-platform/README.md) |
| **Cormetry Health — API & data path** | Software Engineer (2024 – November 2026). Platform API, BLE device ingestion, real-time signal pipelines, and clinical cohort pipelines — [platform](projects/2024-2025/medical/cormetry-ecg-platform/README.md) · [labeling](projects/2026/medical/ecg-coronary-stenosis/README.md) |
| **Data engineering & ML integration** | High-volume time-series pipelines and model integration (PTB-XL, clinical cohorts), arXiv [2609.12803](https://arxiv.org/abs/2609.12803) — [details](#data-engineering-ml-integration) |

---

## Backend experience (2023 – present)

#### Clinovatech — Software Engineer (Backend & Systems), Contract (2025 – 2026)

- Architected the multi-tenant B2B SaaS **backend for clinics** as explicit boundaries: API contracts, database isolation, cache, and asynchronous work.
- Chose **database-level tenant isolation (RLS)** so a missing application filter cannot expose another clinic's rows, and completed the security layer with an immutable audit log and isolated serverless privileged operations.
- Designed the authorization model around users, roles, packages, and modules: **3 subscription packages** and **~20 modules portable across packages**.
- Made **clinic-specific packages** and per-clinic parameters a data change, through package–module and user–module structures, without a code change.
- Defined the clinic microservice on **FastAPI and Pydantic** as a resource-oriented **RESTful** HTTP interface: collection and item paths, standard HTTP methods, and a typed JSON contract.
- Built the operations **CMS** on a **RESTful Flask API**, so clinics, packages, modules, and per-clinic parameters are managed from one panel.
- Owned the persistence layer with **SQLAlchemy** models and **Alembic** schema migrations on PostgreSQL (Supabase).
- Placed **Redis** in front of read-heavy endpoints to cut database load and API latency.
- Moved email and heavy work onto **RabbitMQ and Celery** so the request path stays short.
- Locked service behavior with **pytest**.
- Delivered the dental-clinic domain modules on that platform: appointments, clinic-specific treatment lists, a selectable treatment flow (Plan → Treatment → Payment or Plan → Payment), patient list, earnings, stock, and lab.
- Stack: **FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Redis, RabbitMQ, Celery, pytest, Flask (RESTful CMS)**, Supabase Edge Functions, Docker, and CI/CD.

[Case study](projects/2026/saas/clinovatech-platform/README.md)

#### Cormetry Health Teknoloji A.Ş. — Software Engineer (2024 – November 2026)

- **Platform API:** Designed the FastAPI service for the wearable ECG platform. Request and response contracts are **Pydantic** models; behavior is checked with **pytest**.
- **Access model:** Patients record on their own device; a doctor reads only assigned patients and their recordings. Isolation is enforced **at the database (RLS)**.
- **Device-to-cloud data path:** The API serves a mobile client that ingests device data over **Bluetooth Low Energy**, a cloud backend, and a doctor web panel (React Native / Expo, React + Vite, Supabase). Explainable, rule-based ECG analysis is delivered through that panel as a product feature.
- **IoT ingestion:** Specified **BLE transmission protocols** and **real-time signal validation pipelines** with the hardware team, and verified firmware integration on the physical device against the software contract — [case study](projects/2024-2025/medical/cormetry-ecg-platform/README.md).
- **Clinical data pipeline:** Ran collection and processing for an ECG–angiography cohort of **~1000 patients**: raw device samples read at the correct scale and timing, filters checked against the device's official viewer, and records gated into usable / review / excluded sets by quality and pairing.
- **Model integration:** Adapted pretrained ECG foundation models into a supervised evaluation pipeline and compared them on a locked test set under a **precision-first** decision rule, so model output is a system decision with a fixed contract.
- **PTB-XL evaluation pipeline:** Built the shared data and scoring path used to compare model families and heterogeneous ensembles — [project](projects/2026/medical/ecg-ptbxl-ensemble/README.md).
- **Labeling workstation:** Built a local desktop app (PySide6) so clinicians view one patient's **ECG and angiography report together** and write labels back into the cohort pipeline — [case study](projects/2026/medical/ecg-coronary-stenosis/README.md).
- **TÜBİTAK BİGG 1512 delivery:** Ran the wearable **12-lead ECG** project end to end (work plan, budget, period reports), including technical presentations to investors and TÜBİTAK reviewers and live prototype demos. **500 Hz** prototype build and validation under a **900,000 TRY** grant.

#### CorPal Dijital Sağlık Teknolojileri A.Ş. — Software Developer, Part-Time (March 2023 – August 2023)

- Developed the Firebase cloud data infrastructure integration, patient audio data processing pipelines, and the Flutter-based mobile application for a chronic patient management platform.

> **Confidentiality & NDA:** Commercial project source code is **not** in this public repository due to **intellectual property (IP)** and **NDA** obligations. Architecture details can be shared during interviews.

---

<a id="data-engineering-ml-integration"></a>

## Data Engineering & ML Integration

Pipelines for high-volume time-series and imaging data, with model output behind a contract the rest of the system can call. The notes below are the projects. The papers sit directly under them as the written record of the Python and data-manipulation work.

**PTB-XL ECG pipeline (2026).** Official `strat_fold` split on PTB-XL v1.0.3, SCP codes mapped to five diagnostic superclasses, 100 Hz and 500 Hz tensor caches, and one scoring interface per record. Test fold 10: stacking reached Macro AUROC **0.936**, AUPRC **0.836**, Macro F1 **0.763**. [Project](projects/2026/medical/ecg-ptbxl-ensemble/README.md)

**BreaKHis histopathology pipeline.** Preprocessing across magnifications and a Python path from raw images to model-ready inputs: **89% accuracy**, **0.90 Macro F1**. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)

**ECG image pipeline.** Labeling, denoising, and image-level preparation of ECG signals before they enter a detector.

### Publications (arXiv)

| Paper | arXiv | Data work |
|-------|-------|-----------|
| **Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** — Yunus Emre Mert, Ece Akdoğan, Hüseyin Üvet (Yıldız Technical University) | [2609.12803](https://arxiv.org/abs/2609.12803) · [PDF](projects/2026/medical/ecg-ptbxl-ensemble/paper/2609.12803v1.pdf) | SCP label mapping, official fold split, 100 Hz / 500 Hz tensor caches, one scoring interface. |
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Magnification-wise preprocessing and a pipeline from raw histopathology images to model-ready inputs. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | Labeling, denoising, and image-level preparation of ECG signals. |

---

<a id="undergraduate-open-source-practice-2022-2023"></a>

<details>
<summary>Undergraduate Open-Source Practice (2022-2023)</summary>

Bachelor’s-era **personal / academic practice** in computer vision, machine learning, and medical imaging/signals under **`projects/`** (**year → domain → project**). Raw datasets and model weights are not in the repo; code and sample pipeline outputs are shared.

- **ASIL LAB (Yıldız Technical University):** Led the technical onboarding of junior laboratory members by delivering structured training sessions on Python, AI architectures, and SolidWorks.

| Area | Work | Link |
|------|------|------|
| Medical imaging / pipeline | Mammography model training | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Medical imaging / pipeline | Breast cancer data pipeline | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Medical imaging / pipeline | DICOM → JPG, utilities, MIT-BIH arrhythmia | [DICOM](projects/2023/medical/dicom-to-jpg.ipynb) · [utilities](projects/2023/medical/medical-image-utilities.ipynb) · [2022 DICOM](projects/2022/medical/dcm-convert.ipynb) · [MIT-BIH](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Classification | Pneumonia (chest X-ray), breast cancer (Inception) | [pneumonia](projects/2023/classification/pneumonia-classification.ipynb) · [Inception](projects/2023/classification/inception-breast-cancer.ipynb) |
| Classification | Histopathology (VGG16, Xception); dataset prep | [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb) · [binary Xception](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) · [dataset prep](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Object detection | Abdominal CT (Teknofest / Faster R-CNN), dermatology (YOLOv5, SAHI) | [2022 Teknofest](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) · [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Object detection | Airplane detection (R-CNN → Faster R-CNN / Detectron2); annotation tool | [R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) · [XML→CSV](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |
| Segmentation | scikit-image; ResNet50 semantic segmentation (Keras) | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/resnet50-semantic-segmentation.ipynb) |
| Generative models | Autoencoder, GAN (incl. MURA) | [autoencoder](projects/2022/generative/autoencoders.ipynb) · [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| LLM | LLM work | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

`projects/` folders: `classification/`, `object-detection/`, `medical/`, `segmentation/`, `generative/`, `llm/`. Colab templates: [`templates/`](templates/).

</details>

---

## Tech stack

| Area | Tools & topics |
|------|----------------|
| **Backend & API** | Python, FastAPI, Pydantic, pytest, Flask (RESTful CMS); API clients: React (Vite), React Native (Expo), TypeScript |
| **Databases & Caching** | PostgreSQL, SQLAlchemy, Alembic, Redis, Supabase, SQL schema design |
| **Asynchronous & Messaging** | RabbitMQ, Celery |
| **Infrastructure & Cloud** | AWS (EC2), Docker, GitHub Actions CI/CD, PostgreSQL RLS, Supabase Edge Functions (Deno), RPC |
| **AI & ML** | PyTorch, TensorFlow, Scikit-learn, NumPy, Pandas, OpenCV; 12-lead ECG signal processing, BLE real-time signal pipelines, clinical cohort pipelines (ECG–angiography pairing, de-identification), PTB-XL / WFDB, DICOM; foundation-model fine-tuning and ensemble scoring (ECGFounder, ECG-FM, HuBERT-ECG); YOLOv5/v7, Detectron2, SAHI; PySide6 clinical labeling app; Jupyter, Google Colab |

---

## Contact & license

- [LinkedIn](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub](https://github.com/yunus-emre-mert)
- License: **MIT** — [LICENSE](LICENSE)

Built with open-source libraries (Mask R-CNN, Detectron2, Ultralytics YOLOv5, and others). Third-party datasets and vendored tutorial code are not included in this repository.
