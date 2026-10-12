# Yunus Emre Mert

**R&D Mühendisi | Medikal Yapay Zeka (EKG / Sinyal & Görüntü İşleme) | Mekatronik Mühendisi**

*R&D Engineer | Medical AI (ECG / Signal & Image Processing) | Mechatronics Engineer*

[Türkçe](#türkçe) · [English](#english)

[LinkedIn](https://www.linkedin.com/in/yunus-emre-mert) · [GitHub](https://github.com/yunus-emre-mert)

---

## Türkçe

### Özet

**R&D Engineer** olarak **2024’ten bu yana** medikal yapay zeka ve biyomedikal sistemler üzerinde çalışıyorum: **12-lead EKG için derin öğrenme araştırması** (PTB-XL, arXiv 2609.12803), **giyilebilir 12-lead EKG** donanım–yazılım geliştirme ve regülasyon, ve **RLS tabanlı multi-tenant SaaS backend’inin uçtan uca geliştirilmesi**. Lisans dönemi (2022–2023) bilgisayarlı görü / ML çalışmaları açık kaynak öğrenme pratikleri olarak **`projects/`** altındadır; ticari proje kaynak kodu **IP ve NDA** kapsamında bu depoda değildir.

| Odak (2024 – güncel) | Özet |
|----------------------|------|
| **EKG yapay zeka araştırması (2026)** | PTB-XL çok etiketli sınıflandırma, 5 mimari + heterojen ensemble, arXiv [2609.12803](https://arxiv.org/abs/2609.12803) — [detay](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026) |
| **Cormetry Health** | TÜBİTAK BİGG 1512 giyilebilir 12-lead EKG projesinin uçtan uca yürütülmesi (Ar-Ge Mühendisi / Proje Yürütücüsü), 500 Hz prototip, SolidWorks/DFM, gerçek zamanlı sinyal işleme, CE-MDR; uçtan uca EKG platformu (cihaz + mobil + doktor paneli) — [vaka analizi](projects/2024-2025/medical/cormetry-ecg-platform/README.md); EKG + anjiyo ile koroner darlık araştırması (~1000 hasta, SSL temel modeller) — [vaka analizi](projects/2026/medical/ecg-coronary-stenosis/README.md) |
| **Clinovatech & SaaS** | Multi-tenant B2B SaaS backend’i, veritabanı düzeyinde RLS dahil, tek başıma geliştirildi; kullanıcı / rol / paket / modül bazlı yetkilendirme, klinik bazlı özelleştirme — [vaka analizi](projects/2026/saas/clinovatech-platform/README.md) |
| **Açık kaynak portföy (2022–2023)** | Sınıflandırma, nesne tespiti, medikal pipeline’lar — [detay tablo](#lisans-dönemi-açık-kaynak-pratikleri-20222023) |

---

### R&D ve mühendislik deneyimi (2024 – güncel)

#### Cormetry Health Teknoloji A.Ş. — R&D Engineer / Project Executor, TÜBİTAK 1512 (2024 – güncel)

- **TÜBİTAK BİGG 1512** (900.000 TL hibe) destekli **giyilebilir 12-lead EKG** projesinde **500 Hz** prototip üretimi ve validasyon testleri.
- **TÜBİTAK BİGG 1512 proje yürütmesi:** Projeyi uçtan uca yürüttüm; iş planı, bütçe takibi, dönem raporları, hakem değerlendirmesinde sunum ve canlı prototip demosu.
- **SolidWorks / DFM** ile mekanik muhafaza tasarımı, hızlı **3D prototipleme** ve prototip parçalarının tedariki.
- Gerçek zamanlı biyomedikal veri işleme hatları ve **CE-MDR** regülasyon uyum süreçleri.
- **Uçtan uca 12 derivasyonlu EKG platformu:** Cihazdan Bluetooth ile veri alan cross-platform mobil uygulama, bulut altyapısı ve doktor web panelinden oluşan **yazılım tarafının tamamını tek başıma** geliştirdim (React Native / Expo, React + Vite, Supabase).
- **Hasta / doktor rolleri:** Hasta kaydı kendi cihazıyla alır; doktor yalnızca kendisine atanmış hastaları ve kayıtlarını görür. Veri izolasyonu **veritabanı düzeyinde (RLS)** sağlanır; doktor panelinde **açıklanabilir, kural tabanlı otomatik EKG analizi** bulunur.
- Dış kaynaklı **firmware ve PCB geliştirmesinin** yazılım gereksinimlerine göre entegrasyonu ve gerçek cihazla doğrulanması — [vaka analizi](projects/2024-2025/medical/cormetry-ecg-platform/README.md).
- **12-lead EKG sınıflandırma araştırması:** PTB-XL üzerinde CNN, state-space, rekürrent, transformer ve foundation model yaklaşımlarının karşılaştırması ve heterojen ensemble — [proje](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026).
- **EKG'den koroner darlık tahmini:** **~1000 hastalık** EKG–anjiyo kohortunu topladım ve işledim. Ham cihaz verisini doğru ölçek ve zamanla okudum, filtreleri cihazın resmi görüntüleyicisiyle doğruladım; kayıtları kalite ve eşleşmeye göre kullanılabilir / kontrol / dışlanan gruplara ayırdım.
- **SSL + gözetimli ince ayar:** Öz-denetimli ön-eğitilmiş EKG temel modellerini gözetimli eğitimle kohorta uyarladım ve kilitli test kümesinde **precision öncelikli** karar kuralıyla karşılaştırdım.
- **Klinik EKG görüntüleme ve etiketleme uygulaması:** Hekimler aynı hastanın **EKG'sini ve anjiyo raporunu tek uygulamada** görüp etiketleyebilsin diye yerel bir masaüstü uygulaması (PySide6) geliştirdim — [vaka analizi](projects/2026/medical/ecg-coronary-stenosis/README.md).

#### Clinovatech — Software Engineer, multi-tenant B2B SaaS backend (2025 – 2026)

- Klinikler için multi-tenant B2B SaaS **backend’ini, veritabanı düzeyinde RLS dahil, tek başıma geliştirdim**.
- **Kullanıcı bazlı sistem ve rol yetkilendirmesi;** **3 abonelik paketi** ve paketler arasında **taşınabilir ~20 modül**.
- Paket–modül ve kullanıcı–modül yapısı sayesinde **kliniğe özel paket** ve **klinik parametreleri ile klinik bazlı özelleştirme**, kod değişikliği olmadan.
- Diş klinikleri için iş modülleri: **randevu sistemi**, kliniğe özel **tedavi listeleri**, klinik bazında seçilebilen **tedavi akışı** (Plan → Tedavi → Ödeme veya Plan → Ödeme), **hasta listesi**, personel bazında hesaplama anı seçilebilen **hakediş sistemi**, **stok** ve **lab** modülleri.
- **Veritabanı düzeyinde kiracı izolasyonu** (RLS), değiştirilemez denetim kaydı ve izole serverless ayrıcalıklı işlemler.
- Yığın: **Supabase (PostgreSQL)**, Edge Functions, React / React Native, Docker ve CI/CD.

[Vaka analizi](projects/2026/saas/clinovatech-platform/README.md)

> **Gizlilik ve NDA:** Ticari projelere ait kaynak kodlar, **fikri mülkiyet (IP)** hakları ve **NDA** gizlilik anlaşmaları gereği bu kamuya açık depoda yer almaz. Mimari detaylar mülakat aşamasında aktarılabilir.

---

### Öne çıkan proje: PTB-XL EKG sınıflandırma (2026)

**Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** — Yunus Emre Mert, Ece Akdoğan, Hüseyin Üvet (Yıldız Teknik Üniversitesi). arXiv [2609.12803](https://arxiv.org/abs/2609.12803) · [PDF](projects/2026/medical/ecg-ptbxl-ensemble/paper/2609.12803v1.pdf) · [proje README](projects/2026/medical/ecg-ptbxl-ensemble/README.md)

- **Görev:** PTB-XL v1.0.3 üzerinde 5 tanısal üst sınıf (`NORM`, `MI`, `STTC`, `CD`, `HYP`) için çok etiketli sınıflandırma.
- **Modeller:** 1D-ResNet18, Bidirectional Mamba, xLSTM (sLSTM / mLSTM), CWT-ViT-KAN ve ECGFounder (native 500 Hz fine-tune).
- **Ensemble:** Eşit ağırlıklı soft voting, validasyon ağırlıklı soft voting ve lojistik regresyon tabanlı stacking.
- **Protokol:** Resmi `strat_fold` bölmesi (train 1–8, val 9, test 10), macro-AUPRC ile model seçimi, sadece validasyonda belirlenen sınıf bazlı eşikler.
- **Sonuçlar (test fold 10):** En iyi tekil model ECGFounder (Macro AUROC 0.930, AUPRC 0.823); stacking ile Macro AUROC **0.936**, AUPRC **0.836**, Macro F1 **0.763**; en yüksek subset accuracy **0.630** (validasyon ağırlıklı soft voting).

| Notebook | Rol |
|----------|-----|
| [00 PTB-XL işleme](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/00_ptbxl_colab_process.ipynb) | SCP → üst sınıf etiketleri, 100 Hz / 500 Hz tensör cache |
| [01 1D-ResNet18](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/01_resnet18_1d_baseline.ipynb) | Baseline |
| [02 Bidirectional Mamba](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/02_bidirectional_mamba_ssm.ipynb) · [02.1 xLSTM](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/02.1_xlstm.ipynb) | State-space ve rekürrent modeller |
| [03 CWT-ViT-KAN](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/03_wavelet_kan_cwt_vit.ipynb) | Zaman–frekans + transformer |
| [04 ECGFounder](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/04_ecgfounder_500.ipynb) | Foundation model fine-tune (500 Hz) |
| [05 Heterojen ensemble](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/05_heterogeneous_ensemble.ipynb) | Soft voting + stacking |
| [06 Görselleştirme](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/06_visualize_experiment_results.ipynb) | Makale tablo ve figürleri |
| [`ecg_common.py`](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/ecg_common.py) | Ortak protokol: veri modülü, trainer, metrikler, ensemble yardımcıları |

---

### Akademik yayınlar (arXiv)

| Yayın | arXiv | Özet |
|-------|-------|------|
| **Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** | [2609.12803](https://arxiv.org/abs/2609.12803) | PTB-XL üzerinde 5 derin öğrenme mimarisinin (ResNet, Mamba, xLSTM, CWT-ViT-KAN, ECGFounder) karşılaştırması ve heterojen ensemble; stacking ile Macro AUROC 0.936. |
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Histopatoloji görüntülerinde çoklu büyütme oranlarına göre ön işleme, veri pipeline mühendisliği ve CNN tabanlı sınıflandırma. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | EKG sinyal görüntülerinin etiketlenmesi, gürültü azaltma ve evrişimli sinir ağları ile kardiyovasküler hastalık tespiti. |

*İlgili notebook’lar:* PTB-XL çalışması — [proje](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026); histopatoloji ve meme kanseri pipeline çalışmaları — [2022–2023 özet tablosu](#lisans-dönemi-açık-kaynak-pratikleri-20222023).

---

### Lisans dönemi: açık kaynak pratikleri (2022–2023)

Lisans döneminde bilgisayarlı görü, makine öğrenmesi ve medikal görüntü/sinyal üzerine **kişisel / akademik pratik** notebook’ları **`projects/`** altında (**yıl → alan → proje**). Ham veri setleri ve model ağırlıkları repoda yoktur; kod ve örnek pipeline çıktıları paylaşılmıştır.

- Lisans döneminde alt sınıf öğrencilerine yapay zeka ve makine öğrenmesi pratiklerinde yardımcı oldum.

| Alan | Çalışma | Bağlantı |
|------|---------|----------|
| Medikal görüntü / pipeline | Mamografi model eğitimi | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Medikal görüntü / pipeline | Meme kanseri veri pipeline’ı | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Medikal görüntü / pipeline | DICOM → JPG, yardımcı araçlar, MIT-BIH aritmi | [DICOM](projects/2023/medical/dicom-to-jpg.ipynb) · [utilities](projects/2023/medical/medical-image-utilities.ipynb) · [2022 DICOM](projects/2022/medical/dcm-convert.ipynb) · [MIT-BIH](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Sınıflandırma | Pnömoni (göğüs röntgeni), meme kanseri (Inception) | [pnömoni](projects/2023/classification/pneumonia-classification.ipynb) · [Inception](projects/2023/classification/inception-breast-cancer.ipynb) |
| Sınıflandırma | Histopatoloji (VGG16, Xception); veri hazırlığı | [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb) · [ikili Xception](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) · [veri hazırlığı](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Nesne tespiti | Karın BT (Teknofest / Faster R-CNN), dermatoloji (YOLOv5, SAHI) | [2022 Teknofest](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) · [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Nesne tespiti | Uçak tespiti (R-CNN → Faster R-CNN / Detectron2); etiket aracı | [R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) · [XML→CSV](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |
| Segmentasyon | scikit-image; ResNet50 semantik segmentasyon (Keras) | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/resnet50-semantic-segmentation.ipynb) |
| Üretken modeller | Autoencoder, GAN (MURA dahil) | [autoencoder](projects/2022/generative/autoencoders.ipynb) · [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| LLM | LLM çalışması | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |

`projects/` klasörleri: `classification/`, `object-detection/`, `medical/`, `segmentation/`, `generative/`, `llm/`. Colab şablonları: [`templates/`](templates/).

---

### Teknik yetkinlikler

| Alan | Araçlar & konular |
|------|-------------------|
| **Programlama & altyapı** | Python, SQL şema tasarımı, Supabase (PostgreSQL), RLS & RPC mimarisi, Supabase Edge Functions (Deno), React (Vite) / React Native (Expo), TypeScript, Docker, GitHub Actions CI/CD, Flask API |
| **AI & veri bilimi** | PyTorch, TensorFlow, YOLOv5/v7, Detectron2, OpenCV, SAHI, Scikit-learn, NumPy, Pandas |
| **Derin öğrenme araştırması** | 1D-CNN / ResNet, Mamba (state-space modeller), xLSTM, ViT, KAN, öz-denetimli öğrenme (SSL) EKG temel modelleri, linear probing ve fine-tuning (ECGFounder, ECG-FM, HuBERT-ECG), ensemble learning (soft voting, stacking) |
| **Donanım & prototipleme** | SolidWorks, 3D prototipleme, DFM, donanım–yazılım entegrasyonu, Bluetooth Low Energy cihaz entegrasyonu, gerçek zamanlı sinyal pipeline |
| **Medikal & regülasyon** | 12-lead EKG sinyal işleme, ham cihaz verisi ve filtre doğrulama, klinik veri hattı (EKG–anjiyo eşleme, kimliksizleştirme), PTB-XL / WFDB, DICOM, CE-MDR uyum süreçleri |
| **Masaüstü uygulama** | PySide6, PyInstaller — klinik EKG görüntüleme ve etiketleme uygulaması |
| **Geliştirme ortamı** | Jupyter, Google Colab (GPU eğitimi), scikit-image |

---

### İletişim & lisans

- [LinkedIn](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub](https://github.com/yunus-emre-mert)
- Lisans: **MIT** — [LICENSE](LICENSE)

Projeler açık kaynak kütüphanelerden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.

---

## English

### Summary

**R&D Engineer** since **2024**, working on medical AI and biomedical systems: **deep learning research for 12-lead ECG** (PTB-XL, arXiv 2609.12803), **wearable 12-lead ECG** hardware–software development and regulation, and **end-to-end development of an RLS-based multi-tenant SaaS backend**. Bachelor’s-era (**2022–2023**) computer vision / ML work lives under **`projects/`** as open-source learning practice; commercial **source code is not in this repo** under **IP and NDA**.

| Focus (2024 – present) | Summary |
|------------------------|---------|
| **ECG AI research (2026)** | PTB-XL multi-label classification, 5 architectures + heterogeneous ensemble, arXiv [2609.12803](https://arxiv.org/abs/2609.12803) — [details](#featured-project-ptb-xl-ecg-classification-2026) |
| **Cormetry Health** | End-to-end execution of the TÜBİTAK BİGG 1512 wearable 12-lead ECG project (R&D Engineer / Project Executor), 500 Hz prototype, SolidWorks/DFM, real-time signal processing, CE-MDR; end-to-end ECG platform (device + mobile + doctor panel) — [case study](projects/2024-2025/medical/cormetry-ecg-platform/README.md); ECG + angiography coronary stenosis research (~1000 patients, SSL foundation models) — [case study](projects/2026/medical/ecg-coronary-stenosis/README.md) |
| **Clinovatech & SaaS** | Multi-tenant B2B SaaS backend, including database-level RLS, built single-handedly; user / role / package / module-based authorization, clinic-level customization — [case study](projects/2026/saas/clinovatech-platform/README.md) |
| **Open-source portfolio (2022–2023)** | Classification, detection, medical pipelines — [summary table](#undergraduate-open-source-practice-20222023) |

---

### R&D & engineering experience (2024 – present)

#### Cormetry Health Teknoloji A.Ş. — R&D Engineer / Project Executor, TÜBİTAK 1512 (2024 – present)

- **TÜBİTAK BİGG 1512** (900,000 TRY grant) supported **wearable 12-lead ECG**: **500 Hz** prototype build and validation testing.
- **TÜBİTAK BİGG 1512 project execution:** Executed the project end to end: work plan, budget tracking, period reports, and the presentation and live prototype demo at the TÜBİTAK reviewer evaluation.
- **SolidWorks / DFM** mechanical enclosure design, rapid **3D prototyping**, and procurement of prototype parts.
- Real-time biomedical data processing pipelines and **CE-MDR** regulatory alignment.
- **End-to-end 12-lead ECG platform:** Built **the entire software side on my own**: a cross-platform mobile app that receives data from the device over Bluetooth, the cloud backend, and a doctor web panel (React Native / Expo, React + Vite, Supabase).
- **Patient / doctor roles:** Patients take recordings with their own device; a doctor sees only the patients assigned to them and their recordings. Data isolation is enforced **at the database level (RLS)**, and the doctor panel includes **explainable, rule-based automated ECG analysis**.
- Integration and real-device validation of the **outsourced firmware and PCB development**, driven by software requirements — [case study](projects/2024-2025/medical/cormetry-ecg-platform/README.md).
- **12-lead ECG classification research:** comparison of CNN, state-space, recurrent, transformer and foundation-model approaches plus heterogeneous ensembles on PTB-XL — [project](#featured-project-ptb-xl-ecg-classification-2026).
- **Coronary stenosis prediction from ECG:** Collected and processed an ECG–angiography cohort of **~1000 patients**. Raw device data was read at the correct scale and timing, filters were verified against the device's official viewer, and records were split by quality and pairing into usable / review / excluded groups.
- **SSL + supervised fine-tuning:** I adapted self-supervised pretrained ECG foundation models to the cohort with supervised training and compared them on a locked test set with a **precision-first** decision rule.
- **Clinical ECG viewing and labeling app:** Built a local desktop app (PySide6) so clinicians can view the same patient's **ECG and angiography report in one app** and label the recording — [case study](projects/2026/medical/ecg-coronary-stenosis/README.md).

#### Clinovatech — Software Engineer, multi-tenant B2B SaaS backend (2025 – 2026)

- **Built the multi-tenant B2B SaaS backend for clinics single-handedly, including database-level RLS.**
- **User-based system with role authorization;** **3 subscription packages** and **~20 modules portable across packages**.
- Separate package–module and user–module structures enable **clinic-specific packages** and **per-clinic customization through clinic parameters**, without code changes.
- Business modules for dental clinics: an **appointment system**, clinic-specific **treatment lists**, a per-clinic selectable **treatment flow** (Plan → Treatment → Payment or Plan → Payment), a **patient list**, an **earnings system** with a per-staff calculation trigger, and **stock** and **lab** modules.
- **Database-level tenant isolation** (RLS), immutable audit log, and isolated serverless privileged operations.
- Stack: **Supabase (PostgreSQL)**, Edge Functions, React / React Native, Docker, and CI/CD.

[Case study](projects/2026/saas/clinovatech-platform/README.md)

> **Confidentiality & NDA:** Commercial project source code is **not** in this public repository due to **intellectual property (IP)** and **NDA** obligations. Architecture details can be shared during interviews.

---

### Featured project: PTB-XL ECG classification (2026)

**Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** — Yunus Emre Mert, Ece Akdoğan, Hüseyin Üvet (Yıldız Technical University). arXiv [2609.12803](https://arxiv.org/abs/2609.12803) · [PDF](projects/2026/medical/ecg-ptbxl-ensemble/paper/2609.12803v1.pdf) · [project README](projects/2026/medical/ecg-ptbxl-ensemble/README.md)

- **Task:** multi-label classification of 5 diagnostic superclasses (`NORM`, `MI`, `STTC`, `CD`, `HYP`) on PTB-XL v1.0.3.
- **Models:** 1D-ResNet18, Bidirectional Mamba, xLSTM (sLSTM / mLSTM), CWT-ViT-KAN, and ECGFounder (native 500 Hz fine-tune).
- **Ensembles:** equal-weight soft voting, validation-weighted soft voting, and logistic-regression stacking.
- **Protocol:** official `strat_fold` split (train 1–8, val 9, test 10), macro-AUPRC model selection, class-wise thresholds tuned on validation only.
- **Results (test fold 10):** best single model ECGFounder (Macro AUROC 0.930, AUPRC 0.823); stacking reached Macro AUROC **0.936**, AUPRC **0.836**, Macro F1 **0.763**; best subset accuracy **0.630** (validation-weighted soft voting).

| Notebook | Role |
|----------|------|
| [00 PTB-XL processing](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/00_ptbxl_colab_process.ipynb) | SCP → superclass labels, 100 Hz / 500 Hz tensor caches |
| [01 1D-ResNet18](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/01_resnet18_1d_baseline.ipynb) | Baseline |
| [02 Bidirectional Mamba](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/02_bidirectional_mamba_ssm.ipynb) · [02.1 xLSTM](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/02.1_xlstm.ipynb) | State-space and recurrent models |
| [03 CWT-ViT-KAN](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/03_wavelet_kan_cwt_vit.ipynb) | Time–frequency + transformer |
| [04 ECGFounder](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/04_ecgfounder_500.ipynb) | Foundation model fine-tune (500 Hz) |
| [05 Heterogeneous ensemble](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/05_heterogeneous_ensemble.ipynb) | Soft voting + stacking |
| [06 Visualization](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/06_visualize_experiment_results.ipynb) | Paper tables and figures |
| [`ecg_common.py`](projects/2026/medical/ecg-ptbxl-ensemble/notebooks/ecg_common.py) | Shared protocol: data module, trainer, metrics, ensemble helpers |

---

### Academic publications (arXiv)

| Paper | arXiv | Summary |
|-------|-------|---------|
| **Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** | [2609.12803](https://arxiv.org/abs/2609.12803) | Comparison of 5 deep learning architectures (ResNet, Mamba, xLSTM, CWT-ViT-KAN, ECGFounder) and heterogeneous ensembles on PTB-XL; stacking reaches Macro AUROC 0.936. |
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Preprocessing across histopathology magnifications, data pipeline engineering, and CNN-based classification. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | ECG signal image labeling, denoising, and convolutional neural networks for cardiovascular disease detection. |

*Related notebooks:* PTB-XL study — [project](#featured-project-ptb-xl-ecg-classification-2026); histopathology and breast cancer pipeline work — [2022–2023 summary table](#undergraduate-open-source-practice-20222023).

---

### Undergraduate open-source practice (2022–2023)

Bachelor’s-era **personal / academic practice** in computer vision, machine learning, and medical imaging/signals under **`projects/`** (**year → domain → project**). Raw datasets and model weights are not in the repo; code and sample pipeline outputs are shared.

- During the bachelor's program, I helped junior students with applied AI and machine learning practice.

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

---

### Tech stack

| Area | Tools & topics |
|------|----------------|
| **Programming & infrastructure** | Python, SQL schema design, Supabase (PostgreSQL), RLS & RPC architecture, Supabase Edge Functions (Deno), React (Vite) / React Native (Expo), TypeScript, Docker, GitHub Actions CI/CD, Flask API |
| **AI & data science** | PyTorch, TensorFlow, YOLOv5/v7, Detectron2, OpenCV, SAHI, Scikit-learn, NumPy, Pandas |
| **Deep learning research** | 1D-CNN / ResNet, Mamba (state-space models), xLSTM, ViT, KAN, self-supervised learning (SSL) ECG foundation models, linear probing and fine-tuning (ECGFounder, ECG-FM, HuBERT-ECG), ensemble learning (soft voting, stacking) |
| **Hardware & prototyping** | SolidWorks, 3D prototyping, DFM, hardware–software integration, Bluetooth Low Energy device integration, real-time signal pipelines |
| **Medical & regulatory** | 12-lead ECG signal processing, raw device data and filter verification, clinical data pipeline (ECG–angiography pairing, de-identification), PTB-XL / WFDB, DICOM, CE-MDR compliance workflows |
| **Desktop apps** | PySide6, PyInstaller — clinical ECG viewing and labeling app |
| **Dev environment** | Jupyter, Google Colab (GPU training), scikit-image |

---

### Contact & license

- [LinkedIn](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub](https://github.com/yunus-emre-mert)
- License: **MIT** — [LICENSE](LICENSE)

Built with open-source libraries (Mask R-CNN, Detectron2, Ultralytics YOLOv5, and others). Third-party datasets and vendored tutorial code are not included in this repository.

**Suggested GitHub repo topics:** `machine-learning`, `deep-learning`, `computer-vision`, `medical-imaging`, `jupyter-notebook`, `healthcare-ai`, `ecg`, `ptb-xl`, `saas`, `multi-tenant`, `supabase`
