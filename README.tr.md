# Yunus Emre Mert

**Backend Mühendisi**

[🇬🇧 English (README.md)](README.md)

[LinkedIn](https://www.linkedin.com/in/yunus-emre-mert) · [GitHub](https://github.com/yunus-emre-mert)

---

## Türkçe

### Özet

Çok kiracılı (multi-tenant) B2B SaaS mimarileri, ölçeklenebilir FastAPI mikroservisleri ve yüksek hacimli veri işleme hatları (data pipelines) geliştiren bir **Backend Mühendisiyim**. **Clinovatech**’te kliniklere hizmet veren multi-tenant SaaS backend’ini uçtan uca tasarladım ve geliştirdim: kiracı izolasyonu, yetkilendirme, şema göçleri, önbellek ve arka plan işleri. **Cormetry Health**’te (2024 – Kasım 2026) giyilebilir EKG cihazının platform yazılımını, mobil uygulama tasarımını ve hekimlerin kayıt etiketlemesi için Windows uygulamasını geliştirdim. Model eğitimi ve lisans dönemi çalışmaları aşağıda; ticari kaynak kod **IP ve NDA** kapsamında bu depoda değildir.

| Odak (2024 – güncel) | Özet |
|----------------------|------|
| **Clinovatech & SaaS** | Software Engineer (Backend & Systems), Sözleşmeli. Multi-tenant B2B SaaS backend’i (RLS) ve klinik platformu için FastAPI mikroservisi: Pydantic, SQLAlchemy, Alembic, Redis, RabbitMQ, Celery, pytest — [vaka analizi](projects/2026/saas/clinovatech-platform/README.md) |
| **Cormetry Health** | Software Engineer (2024 – Kasım 2026). Giyilebilir EKG platformunun yazılımı, mobil uygulama tasarımı ve hekim etiketlemesi için Windows uygulaması — [platform](projects/2024-2025/medical/cormetry-ecg-platform/README.md) · [etiketleme](projects/2026/medical/ecg-coronary-stenosis/README.md) |
| **EKG yapay zeka araştırması (2026)** | PTB-XL çok etiketli sınıflandırma, 5 mimari + heterojen ensemble, arXiv [2609.12803](https://arxiv.org/abs/2609.12803) — [detay](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026) |
| **Açık kaynak portföy (2022–2023)** | Sınıflandırma, nesne tespiti, medikal pipeline’lar — [detay tablo](#lisans-dönemi-açık-kaynak-pratikleri-20222023) |

---

### Backend deneyimi (2023 – güncel)

#### Clinovatech — Software Engineer (Backend & Systems), Sözleşmeli (2025 – 2026)

- Klinikler için multi-tenant B2B SaaS **backend’ini uçtan uca tasarladım ve geliştirdim**.
- Kullanıcı, rol, paket ve modül bazlı yetkilendirme modelini kurguladım: **3 abonelik paketi** ve paketler arasında taşınabilir **~20 modül**.
- Paket–modül ve kullanıcı–modül yapısıyla, kod değişikliği olmadan **kliniğe özel paket** ve klinik parametreleriyle özelleştirme sağladım.
- Diş klinikleri için randevu, kliniğe özel tedavi listeleri, seçilebilir tedavi akışı (Plan → Tedavi → Ödeme veya Plan → Ödeme), hasta listesi, hakediş, stok ve lab modüllerini geliştirdim.
- Kiracı izolasyonunu **veritabanı düzeyinde (RLS)** zorunlu kıldım; değiştirilemez denetim kaydı ve izole serverless ayrıcalıklı işlemlerle güvenlik katmanını tamamladım.
- Klinik platformu için **FastAPI ve Pydantic** ile yeni bir mikroservis başlattım; istek ve yanıt sözleşmelerini tipli modellerle tanımladım.
- Veritabanı katmanını **SQLAlchemy** modelleri ve **Alembic** şema göçleriyle yönettim.
- Okuma ağırlıklı uç noktalarda Redis tabanlı önbellekleme (caching) katmanı kurgulayarak veritabanı yükünü ve yanıt sürelerini optimize ettim.
- E-posta ve ağır işleri **RabbitMQ ve Celery** ile arka plana alarak istek yolunu kısalttım.
- Servis davranışını **pytest** ile güvence altına aldım.
- Yığın: **FastAPI, Pydantic, SQLAlchemy, Alembic, Redis, RabbitMQ, Celery, pytest**, Supabase (PostgreSQL), Edge Functions, Docker ve CI/CD.

[Vaka analizi](projects/2026/saas/clinovatech-platform/README.md)

#### Cormetry Health Teknoloji A.Ş. — Software Engineer (2024 – Kasım 2026)

- **Platform API’si:** FastAPI servisi; istek ve yanıt sözleşmeleri **Pydantic** ile, davranış **pytest** ile doğrulanır.
- **Hasta / doktor rolleri:** Hasta kaydı kendi cihazıyla alır; doktor yalnızca kendisine atanmış hastaları ve kayıtlarını görür. Veri izolasyonu **veritabanı düzeyinde (RLS)** sağlanır.
- **Uçtan uca 12 derivasyonlu EKG platformu:** Bu API’nin hizmet verdiği yazılım tarafını da geliştirdim: cihazdan Bluetooth ile veri alan mobil uygulama, bulut altyapısı ve doktor web paneli (React Native / Expo, React + Vite, Supabase). Doktor panelinde **açıklanabilir, kural tabanlı otomatik EKG analizi** bulunur.
- Donanım ekibiyle **BLE veri iletim protokollerini** ve **gerçek zamanlı sinyal doğrulama hatlarını** koordine ettim; firmware entegrasyonunu yazılım gereksinimlerine göre gerçek cihazda doğruladım — [vaka analizi](projects/2024-2025/medical/cormetry-ecg-platform/README.md).
- **TÜBİTAK BİGG 1512 proje yürütmesi:** Projeyi uçtan uca yönettim; iş planı, bütçe takibi, dönem raporları; **yatırımcı ve TÜBİTAK hakem sunumlarında teknik sunum** ve canlı prototip demosu. **900.000 TL hibe** destekli **giyilebilir 12-lead EKG** projesinde **500 Hz** prototip üretimi ve validasyon testleri.
- **12-lead EKG sınıflandırma araştırması:** PTB-XL üzerinde CNN, state-space, rekürrent, transformer ve foundation model yaklaşımlarının karşılaştırması ve heterojen ensemble — [proje](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026).
- **EKG'den koroner darlık tahmini:** **Klinik veri toplama sürecinde** aktif rol aldım; **~1000 hastalık** EKG–anjiyo kohortunun toplanmasını ve işlenmesini uçtan uca yürüttüm. Ham cihaz verisini doğru ölçek ve zamanla okudum, filtreleri cihazın resmi görüntüleyicisiyle doğruladım; kayıtları kalite ve eşleşmeye göre kullanılabilir / kontrol / dışlanan gruplara ayırdım.
- **SSL + gözetimli ince ayar:** Öz-denetimli ön-eğitilmiş EKG temel modellerini gözetimli eğitimle kohorta uyarladım ve kilitli test kümesinde **precision öncelikli** karar kuralıyla karşılaştırdım.
- **Klinik EKG görüntüleme ve etiketleme uygulaması:** Hekimler aynı hastanın **EKG'sini ve anjiyo raporunu tek uygulamada** görüp etiketleyebilsin diye yerel bir masaüstü uygulaması (PySide6) geliştirdim — [vaka analizi](projects/2026/medical/ecg-coronary-stenosis/README.md).

#### CorPal Dijital Sağlık Teknolojileri A.Ş. — Software Developer, Yarı Zamanlı (Mart 2023 – Ağustos 2023)

- Kronik hasta yönetimi platformunun Firebase tabanlı bulut veri altyapısı entegrasyonunu, hastalardan alınan ses verilerinin işlenmesi (audio data processing) süreçlerini ve Flutter tabanlı mobil uygulama geliştirmesini yürüttüm.

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
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Histopatoloji görüntülerinde çoklu büyütme oranlarına göre ön işleme, veri pipeline mühendisliği ve CNN tabanlı sınıflandırma; Xception mimarisi ile **%89 doğruluk** ve **0.90 Macro F1**. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | EKG sinyal görüntülerinin etiketlenmesi, gürültü azaltma ve evrişimli sinir ağları ile kardiyovasküler hastalık tespiti. |

*İlgili notebook’lar:* PTB-XL çalışması — [proje](#öne-çıkan-proje-ptb-xl-ekg-sınıflandırma-2026); histopatoloji ve meme kanseri pipeline çalışmaları — [2022–2023 özet tablosu](#lisans-dönemi-açık-kaynak-pratikleri-20222023).

---

### Lisans dönemi: açık kaynak pratikleri (2022–2023)

Lisans döneminde bilgisayarlı görü, makine öğrenmesi ve medikal görüntü/sinyal üzerine **kişisel / akademik pratik** notebook’ları **`projects/`** altında (**yıl → alan → proje**). Ham veri setleri ve model ağırlıkları repoda yoktur; kod ve örnek pipeline çıktıları paylaşılmıştır.

- **ASIL LAB (Yıldız Teknik Üniversitesi):** Laboratuvara yeni katılan lisans öğrencilerine Python, yapay zeka (AI) mimarileri ve SolidWorks konularında yapılandırılmış eğitimler vererek ekibin teknik adaptasyon sürecine liderlik ettim.

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
| **Backend** | Python, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Redis, RabbitMQ, Celery, pytest, Docker |
| **Programlama & altyapı** | SQL şema tasarımı, Supabase (PostgreSQL), RLS & RPC mimarisi, Supabase Edge Functions (Deno), React (Vite) / React Native (Expo), TypeScript, GitHub Actions CI/CD, Flask API |
| **AI & veri bilimi** | PyTorch, TensorFlow, YOLOv5/v7, Detectron2, OpenCV, SAHI, Scikit-learn, NumPy, Pandas |
| **Derin öğrenme araştırması** | 1D-CNN / ResNet, Mamba (state-space modeller), xLSTM, ViT, KAN, öz-denetimli öğrenme (SSL) EKG temel modelleri, linear probing ve fine-tuning (ECGFounder, ECG-FM, HuBERT-ECG), ensemble learning (soft voting, stacking) |
| **Veri entegrasyonu** | Bluetooth Low Energy (BLE) veri entegrasyonu, gerçek zamanlı sinyal pipeline |
| **Medikal veri** | 12-lead EKG sinyal işleme, ham cihaz verisi ve filtre doğrulama, klinik veri hattı (EKG–anjiyo eşleme, kimliksizleştirme), PTB-XL / WFDB, DICOM |
| **Masaüstü uygulama** | PySide6, PyInstaller — klinik EKG görüntüleme ve etiketleme uygulaması |
| **Geliştirme ortamı** | Jupyter, Google Colab (GPU eğitimi), scikit-image |

---

### İletişim & lisans

- [LinkedIn](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub](https://github.com/yunus-emre-mert)
- Lisans: **MIT** — [LICENSE](LICENSE)

Projeler açık kaynak kütüphanelerden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.
