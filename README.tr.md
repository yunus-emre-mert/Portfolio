# Yunus Emre Mert

**Backend Mühendisi**

[🇬🇧 English (README.md)](README.md)

[LinkedIn](https://www.linkedin.com/in/yunus-emre-mert) · [GitHub](https://github.com/yunus-emre-mert)

---

## Özet

Ölçeklenebilir, çok kiracılı (multi-tenant) SaaS ürünleri ve veri yoğunluklu uygulamalar tasarlayan bir **Backend Mühendisi ve Sistem Mimarıyım**. Temel odak noktam; karmaşık iş senaryolarını analiz edip netleştirmek, bunları sağlam veritabanı şemalarına (schema design) dönüştürmek ve sistemin ihtiyaç duyduğu uçtan uca veri boru hatlarını (data pipelines) inşa etmektir.

**Clinovatech**’te bir klinik SaaS platformunun backend mimarisini uçtan uca tasarladım: İş gereksinimlerini veritabanı tablolarına modeledim, veritabanı düzeyinde kiracı izolasyonu (RLS) kurguladım ve kod değişikliği gerektirmeyen dinamik bir yetkilendirme sistemi kurdum. **Cormetry Health**’te (2024 – Kasım 2026) ise giyilebilir IoT cihazlarından gelen yüksek hacimli medikal veriyi (EKG) işleyen asenkron boru hatlarını, bulut altyapısını ve API sözleşmelerini mimari olarak şekillendirdim. Ticari projelere ait kaynak kodlar **IP ve NDA** kapsamında olduğu için bu depoda yer almaz.

| Odak (2024 – güncel) | Özet |
|----------------------|------|
| **Clinovatech — sistem tasarımı** | Software Engineer (Backend & Systems), Sözleşmeli. Klinik SaaS backend’i: kiracı izolasyonu, paket ve yetkiler, API, önbellek ve arka plan işleri — [vaka analizi](projects/2026/saas/clinovatech-platform/README.md) |
| **Cormetry Health — API ve veri yolu** | Software Engineer (2024 – Kasım 2026). Giyilebilir cihazdan buluta ve doktor paneline giden API — [platform](projects/2024-2025/medical/cormetry-ecg-platform/README.md) · [etiketleme](projects/2026/medical/ecg-coronary-stenosis/README.md) |
| **Veri hatları** | Kayıtları yazılımın kullanabileceği veriye hazırlama — [detay](#veri-muhendisligi-ve-ml-entegrasyonu) |

---

## Backend deneyimi (2023 – güncel)

#### Clinovatech — Software Engineer (Backend & Systems), Sözleşmeli (2025 – 2026)

- Klinikler için çok kiracılı B2B SaaS **backend’ini** açık sınırlar olarak tasarladım: API sözleşmeleri, veritabanı izolasyonu, önbellek ve asenkron iş.
- Eksik bir uygulama filtresinin başka bir kliniğin satırlarını açamaması için **veritabanı düzeyinde kiracı izolasyonunu (RLS)** seçtim; değiştirilemez denetim kaydı ve izole serverless ayrıcalıklı işlemlerle güvenlik katmanını tamamladım.
- Yetkilendirme modelini kullanıcı, rol, paket ve modül etrafında kurguladım: **3 abonelik paketi** ve paketler arasında taşınabilir **~20 modül**.
- **Kliniğe özel paketleri** ve klinik parametrelerini, paket–modül ve kullanıcı–modül yapısıyla, kod değişikliği olmadan bir veri değişikliği haline getirdim.
- Klinik mikroservisini **FastAPI ve Pydantic** üzerinde kaynak odaklı bir **RESTful** HTTP arayüzü olarak tanımladım: koleksiyon ve kayıt yolları, standart HTTP metodları ve tipli JSON sözleşmesi.
- Operasyon **CMS**’ini **RESTful Flask API** üzerine kurdum; klinikler, paketler, modüller ve klinik parametreleri tek panelden yönetilir.
- Kalıcılık katmanını PostgreSQL (Supabase) üzerinde **SQLAlchemy** modelleri ve **Alembic** şema göçleriyle yönettim.
- Okuma ağırlıklı uç noktaların önüne **Redis** koyarak veritabanı yükünü ve API gecikmesini düşürdüm.
- E-posta ve ağır işleri **RabbitMQ ve Celery** üzerine alarak istek yolunu kısa tuttum.
- Servis davranışını **pytest** ile güvence altına aldım.
- Bu platform üzerinde diş kliniği alan modüllerini teslim ettim: randevu, kliniğe özel tedavi listeleri, seçilebilir tedavi akışı (Plan → Tedavi → Ödeme veya Plan → Ödeme), hasta listesi, hakediş, stok ve lab.
- Yığın: **FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Redis, RabbitMQ, Celery, pytest, Flask (RESTful CMS)**, Supabase Edge Functions, Docker ve CI/CD.

[Vaka analizi](projects/2026/saas/clinovatech-platform/README.md)

#### Cormetry Health Teknoloji A.Ş. — Software Engineer (2024 – Kasım 2026)

- **Platform API’si:** Giyilebilir EKG platformu için FastAPI servisini tasarladım. İstek ve yanıt sözleşmeleri **Pydantic** modelleridir; davranış **pytest** ile doğrulanır.
- **Erişim modeli:** Hasta kaydı kendi cihazıyla alır; doktor yalnızca kendisine atanmış hastaları ve kayıtlarını görür. İzolasyon **veritabanında (RLS)** zorunludur.
- **Cihazdan buluta veri yolu:** API, cihaz verisini **Bluetooth Low Energy** ile alan mobil istemciye, bulut backend’ine ve doktor web paneline (React Native / Expo, React + Vite, Supabase) hizmet verir. Açıklanabilir, kural tabanlı EKG analizi bu panelde bir ürün özelliği olarak sunulur.
- **IoT alımı:** Donanım ekibiyle **BLE iletim protokollerini** ve **gerçek zamanlı sinyal doğrulama hatlarını** belirledim; firmware entegrasyonunu fiziksel cihazda yazılım sözleşmesine göre doğruladım — [vaka analizi](projects/2024-2025/medical/cormetry-ecg-platform/README.md).
- **Klinik veri hattı:** **~1000 hastalık** EKG–anjiyo kohortunun toplanmasını ve işlenmesini yürüttüm. Ham cihaz örnekleri doğru ölçek ve zamanla okundu, filtreler cihazın resmi görüntüleyicisiyle kontrol edildi, kayıtlar kalite ve eşleşmeye göre kullanılabilir / kontrol / dışlanan kümelerine ayrıldı.
- **Model entegrasyonu:** Önceden eğitilmiş EKG temel modellerini gözetimli bir değerlendirme hattına uyarladım ve kilitli test kümesinde **precision öncelikli** bir karar kuralıyla karşılaştırdım; model çıktısı sabit sözleşmeli bir sistem kararıdır.
- **PTB-XL değerlendirme hattı:** Model ailelerini ve heterojen ensemble’ları karşılaştırmak için ortak veri ve skorlama yolunu kurdum — [proje](projects/2026/medical/ecg-ptbxl-ensemble/README.md).
- **Etiketleme iş istasyonu:** Hekimler aynı hastanın **EKG’sini ve anjiyo raporunu birlikte** görsün ve etiketler kohort hattına yazılsın diye yerel bir masaüstü uygulaması (PySide6) geliştirdim — [vaka analizi](projects/2026/medical/ecg-coronary-stenosis/README.md).
- **TÜBİTAK BİGG 1512 teslimi:** Giyilebilir **12-lead EKG** projesini uçtan uca yürüttüm (iş planı, bütçe, dönem raporları); yatırımcı ve TÜBİTAK hakemlerine teknik sunumlar ve canlı prototip demoları dahildir. **900.000 TL** hibe altında **500 Hz** prototip üretimi ve validasyon.

#### CorPal Dijital Sağlık Teknolojileri A.Ş. — Software Developer, Yarı Zamanlı (Mart 2023 – Ağustos 2023)

- Kronik hasta yönetimi platformunun Firebase tabanlı bulut veri altyapısı entegrasyonunu, hastalardan alınan ses verilerinin işlenmesi (audio data processing) süreçlerini ve Flutter tabanlı mobil uygulama geliştirmesini yürüttüm.

> **Gizlilik ve NDA:** Ticari projelere ait kaynak kodlar, **fikri mülkiyet (IP)** hakları ve **NDA** gizlilik anlaşmaları gereği bu kamuya açık depoda yer almaz. Mimari detaylar mülakat aşamasında aktarılabilir.

---

<a id="veri-muhendisligi-ve-ml-entegrasyonu"></a>

## Veri Mühendisliği ve ML Entegrasyonu

Yüksek hacimli zaman serisi ve görüntü verisi için boru hatları; model çıktısı, sistemin geri kalanının çağırabildiği bir sözleşmenin arkasında. Aşağıdaki notlar projelerdir. Yayınlar hemen altlarında, bu Python ve veri işleme işinin yazılı kaydıdır.

**PTB-XL EKG hattı (2026).** PTB-XL v1.0.3 üzerinde resmi `strat_fold` bölmesi, beş tanısal üst sınıfa eşlenen SCP kodları, 100 Hz ve 500 Hz tensör önbellekleri ve kayıt başına tek skorlama arayüzü. Test fold 10: stacking ile Macro AUROC **0.936**, AUPRC **0.836**, Macro F1 **0.763**. [Proje](projects/2026/medical/ecg-ptbxl-ensemble/README.md)

**BreaKHis histopatoloji hattı.** Büyütme oranları boyunca ön işleme ve ham görüntüden modele hazır girdiye giden bir Python yolu: **%89 doğruluk**, **0.90 Macro F1**. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)

**EKG görüntü hattı.** EKG sinyallerinin bir dedektöre girmeden önce etiketlenmesi, gürültüsünün azaltılması ve görüntü düzeyinde hazırlanması.

### Yayınlar (arXiv)

| Yayın | arXiv | Veri işi |
|-------|-------|----------|
| **Multi-Label 12-Lead ECG Classification on the PTB-XL Dataset: A Comparative Evaluation of Deep Learning Architectures and Heterogeneous Ensemble Approaches** — Yunus Emre Mert, Ece Akdoğan, Hüseyin Üvet (Yıldız Teknik Üniversitesi) | [2609.12803](https://arxiv.org/abs/2609.12803) · [PDF](projects/2026/medical/ecg-ptbxl-ensemble/paper/2609.12803v1.pdf) | SCP etiket eşlemesi, resmi fold bölmesi, 100 Hz / 500 Hz tensör önbellekleri, tek skorlama arayüzü. |
| **Breast Cancer Diagnosis Using the BreaKHis Dataset** | [2309.01007](https://arxiv.org/abs/2309.01007) | Büyütme oranına göre ön işleme ve ham histopatoloji görüntüsünden modele hazır girdiye giden hat. |
| **CNN Based Detection of Cardiovascular Diseases from ECG Images** | [2408.16800](https://arxiv.org/abs/2408.16800) | EKG sinyallerinin etiketlenmesi, gürültü azaltma ve görüntü düzeyinde hazırlık. |

---

<a id="lisans-donemi-acik-kaynak-pratikleri-2022-2023"></a>

<details>
<summary>Lisans dönemi: açık kaynak pratikleri (2022–2023)</summary>

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

</details>

---

## Teknik yetkinlikler

| Alan | Araçlar ve konular |
|------|--------------------|
| **Backend ve API** | Python, FastAPI, Pydantic, pytest, Flask (RESTful CMS); API istemcileri: React (Vite), React Native (Expo), TypeScript |
| **Veritabanları ve önbellek** | PostgreSQL, SQLAlchemy, Alembic, Redis, Supabase, SQL şema tasarımı |
| **Asenkron iş ve mesajlaşma** | RabbitMQ, Celery |
| **Altyapı ve bulut** | AWS (EC2), Docker, GitHub Actions CI/CD, PostgreSQL RLS, Supabase Edge Functions (Deno), RPC |
| **AI ve ML** | PyTorch, TensorFlow, Scikit-learn, NumPy, Pandas, OpenCV; 12 derivasyonlu EKG sinyal işleme, BLE gerçek zamanlı sinyal hatları, klinik kohort hatları (EKG–anjiyo eşleme, kimliksizleştirme), PTB-XL / WFDB, DICOM; temel model ince ayarı ve ensemble skorlama (ECGFounder, ECG-FM, HuBERT-ECG); YOLOv5/v7, Detectron2, SAHI; PySide6 klinik etiketleme uygulaması; Jupyter, Google Colab |

---

## İletişim ve lisans

- [LinkedIn](https://www.linkedin.com/in/yunus-emre-mert)
- [GitHub](https://github.com/yunus-emre-mert)
- Lisans: **MIT** — [LICENSE](LICENSE)

Projeler açık kaynak kütüphanelerden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.
