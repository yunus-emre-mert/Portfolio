# Yunus Emre Mert

**Mekatronik Mühendisi | Medikal Yapay Zeka (Sinyal / Görüntü İşleme) & SaaS Ürün Geliştirme**

*Mechatronics Engineer | Medical AI (Signal / Image Processing) & SaaS Product Engineering*

[Türkçe](#türkçe) · [English](#english)

---

## Türkçe

### Yönetici özeti

Biyomedikal veri işleme hatları (**12-lead EKG**, **mamografi**, **BT**, **göğüs röntgeni**, **histopatoloji**), **çoklu kiracılı (multi-tenant)** veri mimarileri ve **donanım–yazılım entegrasyonu** üzerine çalışan bir mühendisim. Bu depo; **2022–2023** dönemindeki açık kaynak bilgisayarlı görü ve medikal yapay zeka portföyünü barındırır. **2024 ve sonrası** ticari R&D ve ürün geliştirme deneyimim (Cormetry Health Teknoloji, Clinovatech SaaS) aşağıda özetlenmiştir — kaynak kodları NDA/IP nedeniyle burada yer almaz.

| Odak | Özet |
|------|------|
| Medikal AI | Görüntü sınıflandırma, nesne tespiti, segmentasyon, EKG / DICOM pipeline’ları |
| Ürün & altyapı | Multi-tenant izolasyon, RLS/RPC, PostgreSQL (Supabase), Flask API |
| Donanım & prototip | Giyilebilir 12-lead EKG pre-MVP, SolidWorks, DFM, gerçek zamanlı sinyal işleme |

---

### Akademik ön basımlar & yayınlar

| Yayın | arXiv | Özet |
|-------|-------|------|
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Histopatoloji görüntülerinde çoklu büyütme oranlarına göre ön işleme, veri pipeline mühendisliği ve CNN tabanlı sınıflandırma. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | EKG sinyal görüntülerinin etiketlenmesi, gürültü azaltma ve evrişimli sinir ağları ile kardiyovasküler hastalık tespiti. |

*İlgili açık kaynak notebook’lar:* meme kanseri pipeline ve histopatoloji çalışmaları — [aşağıdaki portföy tabloları](#açık-kaynak-portföy-projeleri-20222023).

---

### Ticari R&D ve ürün geliştirme (2024 – güncel)

#### Cormetry Health Teknoloji A.Ş. — Co-Founder & Product Engineer (2024 – güncel)

- **TÜBİTAK BİGG 1512** (900.000 TL) destekli **giyilebilir 12-lead EKG** projesinde **500 Hz** pre-MVP prototip üretimi ve validasyon testleri.
- **SolidWorks** ile mekanik muhafaza tasarımı, **DFM** (Design for Manufacturing), hızlı **3D prototipleme** ve tedarik yönetimi.
- Gerçek zamanlı biyomedikal veri işleme hatları, **CE-MDR** regülasyon uyum süreçleri ve **cross-platform mobil / web dashboard** entegrasyonu.

#### Clinovatech & SaaS mimari çalışmaları

- Ürün yönetimi (PM) gereksinimlerine uygun **multi-tenant veri izolasyonu**, **parametrik yetkilendirme** (**RLS & RPC** mimarisi) ve ilişkisel veritabanı (**Supabase / PostgreSQL**, **Flask API**) kurguları.

> **Gizlilik notu:** Ticari ve girişim seviyesindeki bu projelerin kaynak kodları, fikri mülkiyet koruması (IP) ve NDA gizlilik anlaşmaları gereği kamuya açık bu depoda yer almamaktadır. Teknik detaylar ve mimari süreçler mülakat aşamasında aktarılabilir.

---

### Açık kaynak portföy projeleri (2022–2023)

Bu bölümdeki kodlar **`projects/`** altında **yıl → alan → (proje klasörü)** düzenindedir. **Ham veri setleri ve eğitilmiş model ağırlıkları repoda yoktur**; Jupyter notebook’lar, işlenmiş örnek çıktılar ve pipeline kodları paylaşılmıştır.

#### Öne çıkan çalışmalar

1. **Mammografi analizi (mezuniyet projesi)** — Mamografi görüntülerinde uçtan uca model eğitimi ve analiz. [Notebook](projects/2023/medical/mammography-training.ipynb)
2. **Meme kanseri veri pipeline’ı** — Görüntü ve etiketlerin modele hazırlanması için uçtan uca veri akışı. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)
3. **Pnömoni tespiti (göğüs röntgeni)** — Göğüs röntgenlerinde pnömoni / normal ayrımı. [Notebook](projects/2023/classification/pneumonia-classification.ipynb)
4. **Teknofest — karın BT bulgu tespiti** — BT kesitlerinde çok sınıflı bulgu tespiti. [Notebook (2022)](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb)
5. **Dermatoloji lezyon tespiti** — YOLOv5 ve büyük görüntüler için SAHI dilimli inference. [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [YOLOv5 + SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb)
6. **Histopatoloji sınıflandırma** — Transfer learning (VGG16, Xception). [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb)

#### Projeler — kategori bazlı özet

**Görüntü sınıflandırma**

| Proje | Yıl | Kısa açıklama | Detay |
|-------|-----|---------------|--------|
| Pnömoni sınıflandırma | 2023 | Göğüs röntgeni — pnömoni tespiti | [notebook](projects/2023/classification/pneumonia-classification.ipynb) |
| Meme kanseri sınıflandırma | 2023 | Inception tabanlı sınıflandırma | [notebook](projects/2023/classification/inception-breast-cancer.ipynb) |
| Histopatoloji — VGG16 | 2022 | Transfer learning ile doku sınıflandırma | [notebook](projects/2022/classification/vgg16-histopathology-classifier.ipynb) |
| Histopatoloji — Xception (çok sınıflı) | 2022 | Xception ile çok sınıflı sınıflandırma | [notebook](projects/2022/classification/xception-histopathology-classifier.ipynb) |
| Histopatoloji — Xception (ikili) | 2022 | İkili (kanser / normal) sınıflandırma | [notebook](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) |

**Nesne tespiti**

| Proje | Yıl | Kısa açıklama | Detay |
|-------|-----|---------------|--------|
| Karın BT bulgu tespiti | 2022–2023 | Teknofest (2022) ve Faster R-CNN (2023) | [2022](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) |
| Dermatoloji lezyon tespiti | 2023 | YOLOv5 ve SAHI | [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Uçak tespiti | 2022–2023 | R-CNN → Faster R-CNN / Detectron2 | [2022 R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) |

**Segmentasyon**

| Proje | Yıl | Kısa açıklama | Detay |
|-------|-----|---------------|--------|
| Görüntü segmentasyonu | 2022–2023 | scikit-image örneği ve segmentasyon demosu | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |

**Tıbbi sinyal / görüntü & veri pipeline**

| Proje | Yıl | Kısa açıklama | Detay |
|-------|-----|---------------|--------|
| Mammografi eğitimi | 2023 | Mezuniyet projesi — mamografi model eğitimi | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Meme kanseri veri pipeline’ı | 2023 | Etiket ve görüntü ön işleme akışı | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| DICOM → JPG dönüşümü | 2023 | DICOM formatından görüntü üretimi | [notebook](projects/2023/medical/dicom-to-jpg.ipynb) |
| Tıbbi veri işleme yardımcıları | 2023 | Genel tıbbi görüntü işleme | [notebook](projects/2023/medical/medical-image-utilities.ipynb) |
| DICOM dönüşüm (2022) | 2022 | Erken DICOM dönüşüm denemeleri | [notebook](projects/2022/medical/dcm-convert.ipynb) |
| MIT-BIH aritmi analizi | 2022 | EKG kayıtlarında aritmi veri analizi | [notebook](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Histopatoloji veri hazırlığı | 2022 | Çoklu büyütme (40×–400×) veri seti düzenleme | [notebook](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Etiket dönüştürücü (XML → CSV) | 2022 | Nesne tespiti etiketlerini CSV’ye çevirme | [script](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |

**Diğer (üretken modeller, LLM)**

| Proje | Yıl | Kısa açıklama | Detay |
|-------|-----|---------------|--------|
| Autoencoder | 2022 | Autoencoder eğitimi | [notebook](projects/2022/generative/autoencoders.ipynb) |
| GAN denemeleri | 2022 | GAN modelleri (genel ve MURA dirsek verisi) | [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| Erken LLM / AI denemesi | 2023 | Büyük dil modelleri ile erken deneme | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

#### Klasör yapısı (`projects/`)

| Klasör | Ne tür iş? |
|--------|------------|
| `classification/` | Görüntü sınıflandırma |
| `object-detection/` | Kutu ile bulgu / nesne tespiti |
| `medical/` | Tıbbi görüntü ve sinyal, veri pipeline |
| `segmentation/` | Piksel düzeyinde segmentasyon |
| `generative/` | Autoencoder, GAN |
| `llm/` | Büyük dil modeli denemeleri |

Nesne tespiti alt klasörleri: `airplane-detection/`, `teknofest-abdominal-ct/`, `abdominal-ct-detection/`, `dermatology-detection/`, `tools/` (script’ler). Colab şablonları portföye dahil değildir — [`templates/`](templates/).

#### Nasıl inceleyebilirsiniz?

1. Tablodaki linke tıklayın.
2. GitHub’da notebook açıldığında aşağı kaydırın — eğitim grafikleri ve örnek çıktılar hücrelerde görünür.
3. Kodu çalıştırmak için notebook’u indirip Jupyter veya Google Colab kullanın (veri setleri repoda olmadığı için bazı hücreler yerel veri gerektirir).

---

### Teknik yetkinlikler

| Alan | Araçlar & konular |
|------|-------------------|
| **Programlama & altyapı** | Python, SQL şema tasarımı, Supabase (PostgreSQL), RLS & RPC mimarisi, Flask API |
| **AI & veri bilimi** | TensorFlow, PyTorch, YOLOv5/v7, Detectron2, OpenCV, SAHI (Sliced Inference), Scikit-learn, NumPy, Pandas |
| **Donanım & prototipleme** | SolidWorks, 3D prototipleme, DFM, donanım–yazılım entegrasyonu, gerçek zamanlı sinyal pipeline |
| **Medikal & regülasyon** | DICOM, 12-lead ECG sinyal işleme, CE-MDR uyum süreçleri |
| **Geliştirme ortamı (açık kaynak dönemi)** | Jupyter, Google Colab, scikit-image |

---

### İletişim & lisans

- [LinkedIn profilim](https://linkedin.com/in/YOUR-PROFILE) *(URL’yi kendi profilinizle güncelleyin)*
- Lisans: **MIT** — [LICENSE](LICENSE)

Projeler açık kaynak kütüphanelerden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.

---

## English

### Executive summary

I engineer **biomedical data pipelines** ( **12-lead ECG**, **mammography**, **CT**, **chest X-ray**, **histopathology** ), **multi-tenant** data architectures, and **hardware–software integration**. This repository hosts my **2022–2023** open-source computer vision and medical AI portfolio. **Commercial R&D and product work from 2024 onward** (Cormetry Health Teknoloji, Clinovatech SaaS) is summarized below — source code is not published here due to NDA/IP.

| Focus | Summary |
|-------|---------|
| Medical AI | Classification, object detection, segmentation, ECG / DICOM pipelines |
| Product & infra | Multi-tenant isolation, RLS/RPC, PostgreSQL (Supabase), Flask API |
| Hardware & prototyping | Wearable 12-lead ECG pre-MVP, SolidWorks, DFM, real-time signal processing |

---

### Academic preprints & publications

| Paper | arXiv | Summary |
|-------|-------|---------|
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Preprocessing across histopathology magnifications, data pipeline engineering, and CNN-based classification. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | ECG signal image labeling, denoising, and convolutional neural networks for cardiovascular disease detection. |

*Related open-source notebooks:* breast cancer pipeline and histopathology work — [portfolio tables below](#open-source-portfolio-projects-20222023).

---

### Commercial R&D & product development (2024 – present)

#### Cormetry Health Teknoloji A.Ş. — Co-Founder & Product Engineer (2024 – present)

- **TÜBİTAK BİGG 1512** (900,000 TRY) supported **wearable 12-lead ECG**: **500 Hz** pre-MVP prototype build and validation testing.
- Mechanical enclosure design in **SolidWorks**, **DFM**, rapid **3D prototyping**, and supply management.
- Real-time biomedical data processing pipelines, **CE-MDR** regulatory alignment, and **cross-platform mobile / web dashboard** integration.

#### Clinovatech & SaaS architecture

- **Multi-tenant data isolation**, **parameterized authorization** (**RLS & RPC**), and relational backends (**Supabase / PostgreSQL**, **Flask API**) aligned with product management requirements.

> **Confidentiality notice:** Source code, data architectures, and implementation details for these commercial and venture-stage projects are **not** included in this public repository due to **IP protection** and **NDA** obligations. Technical depth can be shared during interviews.

---

### Open-source portfolio projects (2022–2023)

Code lives under **`projects/`** as **year → domain → (project folder)**. **Raw datasets and trained model weights are not in this repo**; notebooks include code and saved sample outputs.

#### Highlighted work

1. **Mammography analysis (graduation project)** — End-to-end mammography training and analysis. [Notebook](projects/2023/medical/mammography-training.ipynb)
2. **Breast cancer data pipeline** — Full preprocessing workflow for images and labels. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)
3. **Pneumonia detection (chest X-ray)** — Pneumonia vs. normal on chest radiographs. [Notebook](projects/2023/classification/pneumonia-classification.ipynb)
4. **Teknofest — abdominal CT abnormality detection** — Multi-class detection on CT slices. [Notebook (2022)](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb)
5. **Dermatology lesion detection** — YOLOv5 and SAHI sliced inference for large images. [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [YOLOv5 + SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb)
6. **Histopathology classification** — Transfer learning (VGG16, Xception). [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb)

#### Projects by category

**Image classification**

| Project | Year | Summary | Details |
|---------|------|---------|---------|
| Pneumonia classification | 2023 | Chest X-ray pneumonia detection | [notebook](projects/2023/classification/pneumonia-classification.ipynb) |
| Breast cancer classification | 2023 | Inception-based classification | [notebook](projects/2023/classification/inception-breast-cancer.ipynb) |
| Histopathology — VGG16 | 2022 | Transfer learning for tissue classes | [notebook](projects/2022/classification/vgg16-histopathology-classifier.ipynb) |
| Histopathology — Xception (multi-class) | 2022 | Multi-class Xception classifier | [notebook](projects/2022/classification/xception-histopathology-classifier.ipynb) |
| Histopathology — Xception (binary) | 2022 | Binary cancer vs. normal | [notebook](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) |

**Object detection**

| Project | Year | Summary | Details |
|---------|------|---------|---------|
| Abdominal CT detection | 2022–2023 | Teknofest (2022) and Faster R-CNN (2023) | [2022](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) |
| Dermatology lesion detection | 2023 | YOLOv5 and SAHI | [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Airplane detection | 2022–2023 | R-CNN through Faster R-CNN / Detectron2 | [2022 R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) |

**Segmentation**

| Project | Year | Summary | Details |
|---------|------|---------|---------|
| Image segmentation | 2022–2023 | scikit-image example and segmentation demo | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |

**Medical signal / imaging & data pipelines**

| Project | Year | Summary | Details |
|---------|------|---------|---------|
| Mammography training | 2023 | Graduation project — mammography model training | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Breast cancer data pipeline | 2023 | Image and label preprocessing workflow | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| DICOM to JPG | 2023 | Convert medical DICOM to image files | [notebook](projects/2023/medical/dicom-to-jpg.ipynb) |
| Medical image utilities | 2023 | General medical image processing helpers | [notebook](projects/2023/medical/medical-image-utilities.ipynb) |
| DICOM conversion (2022) | 2022 | Early DICOM conversion experiments | [notebook](projects/2022/medical/dcm-convert.ipynb) |
| MIT-BIH arrhythmia analysis | 2022 | ECG arrhythmia dataset analysis | [notebook](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Histopathology dataset prep | 2022 | Multi-magnification (40×–400×) organization | [notebook](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Annotation converter (XML → CSV) | 2022 | Pascal VOC XML to CSV | [script](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |

**Other (generative models, LLM)**

| Project | Year | Summary | Details |
|---------|------|---------|---------|
| Autoencoders | 2022 | Autoencoder training | [notebook](projects/2022/generative/autoencoders.ipynb) |
| GAN experiments | 2022 | GAN models (general and MURA elbow dataset) | [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| Early LLM / AI experiment | 2023 | Early large language model experimentation | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

#### Folder layout (`projects/`)

| Folder | What it covers |
|--------|----------------|
| `classification/` | Image classification |
| `object-detection/` | Bounding-box detection |
| `medical/` | Medical imaging, signals, data pipelines |
| `segmentation/` | Pixel-level segmentation |
| `generative/` | Autoencoders, GANs |
| `llm/` | Large language model experiments |

Object-detection subfolders: `airplane-detection/`, `teknofest-abdominal-ct/`, `abdominal-ct-detection/`, `dermatology-detection/`, `tools/` (scripts). Colab starters are in [`templates/`](templates/) — not portfolio deliverables.

#### How to review

1. Click a link in the tables above.
2. Scroll through the notebook on GitHub for training plots and sample outputs.
3. Download and run with Jupyter or Google Colab where needed (some cells expect datasets not shipped in this repo).

---

### Tech stack

| Area | Tools & topics |
|------|----------------|
| **Programming & infrastructure** | Python, SQL schema design, Supabase (PostgreSQL), RLS & RPC architecture, Flask API |
| **AI & data science** | TensorFlow, PyTorch, YOLOv5/v7, Detectron2, OpenCV, SAHI (Sliced Inference), Scikit-learn, NumPy, Pandas |
| **Hardware & prototyping** | SolidWorks, 3D prototyping, DFM, hardware–software integration, real-time signal pipelines |
| **Medical & regulatory** | DICOM, 12-lead ECG signal processing, CE-MDR compliance workflows |
| **Dev environment (open-source era)** | Jupyter, Google Colab, scikit-image |

---

### Contact & license

- [LinkedIn profile](https://linkedin.com/in/YOUR-PROFILE) *(replace with your profile URL)*
- License: **MIT** — [LICENSE](LICENSE)

Built with open-source libraries (Mask R-CNN, Detectron2, Ultralytics YOLOv5, and others). Third-party datasets and vendored tutorial code are not included in this repository.

**Suggested GitHub repo topics:** `machine-learning`, `computer-vision`, `medical-imaging`, `jupyter-notebook`, `healthcare-ai`, `ecg`, `saas`
