# Yunus Emre Mert

**Mekatronik Mühendisi | Medikal Yapay Zeka (Sinyal / Görüntü İşleme) & SaaS Ürün Geliştirme**

*Mechatronics Engineer | Medical AI (Signal / Image Processing) & SaaS Product Engineering*

[Türkçe](#türkçe) · [English](#english)

[LinkedIn](https://www.linkedin.com/in/yunus-emre-mert) · [GitHub](https://github.com/yunus-emre-mert)

---

## Türkçe

### Yönetici özeti

**2024’ten bu yana** ticari R&D ve ürün geliştirmede odaklandığım alanlar: **giyilebilir 12-lead EKG** (donanım–yazılım, regülasyon) ve **multi-tenant SaaS** altyapısı. Lisans döneminde (2022–2023) bilgisayarlı görü ve medikal yapay zeka üzerine açık kaynak öğrenme pratikleri yaptım; bu çalışmaların kodu **`projects/`** altında paylaşılmıştır. Ticari projelerin kaynak kodu **NDA / fikri mülkiyet** nedeniyle bu depoda yer almaz.

| Odak (2024 – güncel) | Özet |
|----------------------|------|
| **Cormetry Health** | TÜBİTAK BİGG 1512 destekli giyilebilir 12-lead EKG, 500 Hz prototip, SolidWorks/DFM, gerçek zamanlı sinyal işleme, CE-MDR |
| **Clinovatech & SaaS** | Multi-tenant veri izolasyonu, RLS & RPC yetkilendirme, Supabase (PostgreSQL), Flask API, ürün yönetimi süreçleri |
| **Açık kaynak portföy (2022–2023)** | Sınıflandırma, nesne tespiti, medikal pipeline’lar — [detay tablo](#lisans-dönemi-açık-kaynak-pratikleri-20222023) |

---

### Ticari R&D ve ürün geliştirme (2024 – güncel)

#### Cormetry Health Teknoloji A.Ş. — Co-Founder & Product Engineer (2024 – güncel)

- **TÜBİTAK BİGG 1512** (900.000 TL) destekli **giyilebilir 12-lead EKG** projesinde **500 Hz** pre-MVP prototip üretimi ve validasyon testleri.
- **SolidWorks** ile mekanik muhafaza tasarımı, **DFM** (Design for Manufacturing), hızlı **3D prototipleme** ve tedarik yönetimi.
- Gerçek zamanlı biyomedikal veri işleme hatları, **CE-MDR** regülasyon uyum süreçleri ve **cross-platform mobil / web dashboard** entegrasyonu.

#### Clinovatech & SaaS mimari çalışmaları

- Ürün yönetimi gereksinimlerine uygun **multi-tenant veri izolasyonu**, **parametrik yetkilendirme** (**RLS & RPC** mimarisi) ve ilişkisel veritabanı (**Supabase / PostgreSQL**, **Flask API**) kurguları.

> **Gizlilik notu:** Ticari ve girişim seviyesindeki projelerin kaynak kodları, **fikri mülkiyet (IP)** hakları ve **NDA** gizlilik anlaşmaları gereği bu kamuya açık depoda yer almamaktadır. Mimari detaylar ve teknik süreçler mülakat aşamasında paylaşılabilir.

---

### Akademik yayınlar (arXiv)

| Yayın | arXiv | Özet |
|-------|-------|------|
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Histopatoloji görüntülerinde çoklu büyütme oranlarına göre ön işleme, veri pipeline mühendisliği ve CNN tabanlı sınıflandırma. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | EKG sinyal görüntülerinin etiketlenmesi, gürültü azaltma ve evrişimli sinir ağları ile kardiyovasküler hastalık tespiti. |

*İlgili notebook’lar:* histopatoloji ve meme kanseri pipeline çalışmaları — [2022–2023 özet tablosu](#lisans-dönemi-açık-kaynak-pratikleri-20222023).

---

### Lisans dönemi: açık kaynak pratikleri (2022–2023)

Lisans sürecinde bilgisayarlı görü, makine öğrenmesi ve medikal görüntü/sinyal konularında **kişisel ve akademik pratik** olarak geliştirdiğim notebook’lar **`projects/`** altında **yıl → alan → proje** düzenindedir. Ham veri setleri ve eğitilmiş model ağırlıkları repoda yoktur; kod, işlenmiş örnek çıktılar ve pipeline adımları paylaşılmıştır.

- **AI mentörlüğü / özel ders:** Lisans döneminde **alt sınıf lisans öğrencilerine** ve **lise seviyesindeki öğrencilere** yapay zeka ve makine öğrenmesi konularında özel ders ve mentörlük verdim — teknik iletişim ve bilgi aktarımı deneyimi.

| Alan | Çalışma | Bağlantı |
|------|---------|----------|
| Medikal görüntü / pipeline | Mamografi model eğitimi | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Medikal görüntü / pipeline | Meme kanseri veri pipeline’ı | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Medikal görüntü / pipeline | DICOM → JPG, yardımcı araçlar, MIT-BIH aritmi | [DICOM](projects/2023/medical/dicom-to-jpg.ipynb) · [utilities](projects/2023/medical/medical-image-utilities.ipynb) · [2022 DICOM](projects/2022/medical/dcm-convert.ipynb) · [MIT-BIH](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Sınıflandırma | Pnömoni (göğüs röntgeni), meme kanseri (Inception) | [pnömoni](projects/2023/classification/pneumonia-classification.ipynb) · [Inception](projects/2023/classification/inception-breast-cancer.ipynb) |
| Sınıflandırma | Histopatoloji (VGG16, Xception); veri hazırlığı | [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb) · [ikili Xception](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) · [veri hazırlığı](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Nesne tespiti | Karın BT (Teknofest / Faster R-CNN), dermatoloji (YOLOv5, SAHI) | [2022 Teknofest](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) · [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Nesne tespiti | Uçak tespiti (R-CNN → Faster R-CNN / Detectron2); etiket aracı | [R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) · [XML→CSV](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |
| Segmentasyon | scikit-image ve demo | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |
| Üretken modeller | Autoencoder, GAN denemeleri (MURA dahil) | [autoencoder](projects/2022/generative/autoencoders.ipynb) · [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| LLM | Erken LLM denemesi | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

`projects/` klasörleri: `classification/`, `object-detection/`, `medical/`, `segmentation/`, `generative/`, `llm/`. Colab şablonları: [`templates/`](templates/) (portföy teslimi değil). Notebook’ları GitHub’da açıp kaydırarak grafik ve örnek çıktıları inceleyebilir; yerel çalıştırma için Jupyter veya Colab kullanılabilir (bazı hücreler repoda olmayan veri seti bekler).

---

### Teknik yetkinlikler

| Alan | Araçlar & konular |
|------|-------------------|
| **Programlama & altyapı** | Python, SQL şema tasarımı, Supabase (PostgreSQL), RLS & RPC mimarisi, Flask API |
| **AI & veri bilimi** | TensorFlow, PyTorch, YOLOv5/v7, Detectron2, OpenCV, SAHI, Scikit-learn, NumPy, Pandas |
| **Donanım & prototipleme** | SolidWorks, 3D prototipleme, DFM, donanım–yazılım entegrasyonu, gerçek zamanlı sinyal pipeline |
| **Medikal & regülasyon** | DICOM, 12-lead ECG sinyal işleme, CE-MDR uyum süreçleri |
| **Geliştirme ortamı (açık kaynak dönemi)** | Jupyter, Google Colab, scikit-image |

---

### İletişim & lisans

- [LinkedIn profilim](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub profilim](https://github.com/yunus-emre-mert)
- Lisans: **MIT** — [LICENSE](LICENSE)

Projeler açık kaynak kütüphanelerden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.

---

## English

### Executive summary

Since **2024**, my primary focus is **commercial R&D and product engineering**: **wearable 12-lead ECG** (hardware–software, regulation) and **multi-tenant SaaS** infrastructure. During my bachelor’s (**2022–2023**), I built **open-source learning exercises** in computer vision and medical AI; code is under **`projects/`**. Commercial project **source code is not published** here due to **NDA and IP** obligations.

| Focus (2024 – present) | Summary |
|------------------------|---------|
| **Cormetry Health** | TÜBİTAK BİGG 1512 wearable 12-lead ECG, 500 Hz prototype, SolidWorks/DFM, real-time signal processing, CE-MDR |
| **Clinovatech & SaaS** | Multi-tenant isolation, RLS & RPC authorization, Supabase (PostgreSQL), Flask API, product management |
| **Open-source portfolio (2022–2023)** | Classification, detection, medical pipelines — [summary table](#undergraduate-open-source-practice-20222023) |

---

### Commercial R&D & product development (2024 – present)

#### Cormetry Health Teknoloji A.Ş. — Co-Founder & Product Engineer (2024 – present)

- **TÜBİTAK BİGG 1512** (900,000 TRY) supported **wearable 12-lead ECG**: **500 Hz** pre-MVP prototype build and validation testing.
- Mechanical enclosure design in **SolidWorks**, **DFM**, rapid **3D prototyping**, and supply management.
- Real-time biomedical data processing pipelines, **CE-MDR** regulatory alignment, and **cross-platform mobile / web dashboard** integration.

#### Clinovatech & SaaS architecture

- **Multi-tenant data isolation**, **parameterized authorization** (**RLS & RPC**), and relational backends (**Supabase / PostgreSQL**, **Flask API**) aligned with product management requirements.

> **Confidentiality notice:** Source code for these commercial and venture-stage projects is **not** in this public repository due to **intellectual property (IP)** rights and **NDA** agreements. Architecture and implementation details can be discussed during interviews.

---

### Academic publications (arXiv)

| Paper | arXiv | Summary |
|-------|-------|---------|
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Preprocessing across histopathology magnifications, data pipeline engineering, and CNN-based classification. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | ECG signal image labeling, denoising, and convolutional neural networks for cardiovascular disease detection. |

*Related notebooks:* histopathology and breast cancer pipeline work — [2022–2023 summary table](#undergraduate-open-source-practice-20222023).

---

### Undergraduate open-source practice (2022–2023)

During my bachelor’s degree, these **personal and academic practice** notebooks cover computer vision, machine learning, and medical imaging/signals. Layout: **`projects/`** as **year → domain → project**. Raw datasets and trained weights are not in the repo; shared artifacts are code, sample outputs, and pipeline steps.

- **AI tutoring & mentoring:** Delivered **private lessons and mentoring** in artificial intelligence and machine learning to **junior undergraduate students** and **high-school learners** — demonstrates technical communication and knowledge transfer.

| Area | Work | Link |
|------|------|------|
| Medical imaging / pipeline | Mammography model training | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Medical imaging / pipeline | Breast cancer data pipeline | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Medical imaging / pipeline | DICOM → JPG, utilities, MIT-BIH arrhythmia | [DICOM](projects/2023/medical/dicom-to-jpg.ipynb) · [utilities](projects/2023/medical/medical-image-utilities.ipynb) · [2022 DICOM](projects/2022/medical/dcm-convert.ipynb) · [MIT-BIH](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Classification | Pneumonia (chest X-ray), breast cancer (Inception) | [pneumonia](projects/2023/classification/pneumonia-classification.ipynb) · [Inception](projects/2023/classification/inception-breast-cancer.ipynb) |
| Classification | Histopathology (VGG16, Xception); dataset prep | [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb) · [binary Xception](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) · [dataset prep](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Object detection | Abdominal CT (Teknofest / Faster R-CNN), dermatology (YOLOv5, SAHI) | [2022 Teknofest](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) · [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Object detection | Airplane detection (R-CNN → Faster R-CNN / Detectron2); annotation tool | [R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) · [XML→CSV](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |
| Segmentation | scikit-image and demo | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |
| Generative models | Autoencoder, GAN experiments (incl. MURA) | [autoencoder](projects/2022/generative/autoencoders.ipynb) · [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| LLM | Early LLM experiment | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

`projects/` folders: `classification/`, `object-detection/`, `medical/`, `segmentation/`, `generative/`, `llm/`. Colab starters: [`templates/`](templates/) (not portfolio deliverables). Open notebooks on GitHub and scroll for plots and sample outputs; run locally with Jupyter or Colab where needed (some cells expect datasets not shipped in this repo).

---

### Tech stack

| Area | Tools & topics |
|------|----------------|
| **Programming & infrastructure** | Python, SQL schema design, Supabase (PostgreSQL), RLS & RPC architecture, Flask API |
| **AI & data science** | TensorFlow, PyTorch, YOLOv5/v7, Detectron2, OpenCV, SAHI, Scikit-learn, NumPy, Pandas |
| **Hardware & prototyping** | SolidWorks, 3D prototyping, DFM, hardware–software integration, real-time signal pipelines |
| **Medical & regulatory** | DICOM, 12-lead ECG signal processing, CE-MDR compliance workflows |
| **Dev environment (open-source era)** | Jupyter, Google Colab, scikit-image |

---

### Contact & license

- [LinkedIn profile](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub profile](https://github.com/yunus-emre-mert)
- License: **MIT** — [LICENSE](LICENSE)

Built with open-source libraries (Mask R-CNN, Detectron2, Ultralytics YOLOv5, and others). Third-party datasets and vendored tutorial code are not included in this repository.

**Suggested GitHub repo topics:** `machine-learning`, `computer-vision`, `medical-imaging`, `jupyter-notebook`, `healthcare-ai`, `ecg`, `saas`
