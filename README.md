# My Portfolio

*Machine learning & computer vision (2022–2023)*

[Türkçe](#türkçe) · [English](#english)

---

## Türkçe

**My Portfolio — 2022–2023 bilgisayarlı görü ve tıbbi görüntüleme projeleri.**

Bu depo, üniversite ve yarışma dönemimde yaptığım **görüntü işleme ve tıbbi görüntü analizi** çalışmalarını toplar. Özellikle röntgen, BT ve mamografi gibi görüntülerde bulgu tespiti, veri hazırlığı ve model eğitimi üzerine odaklandım.

### Bu repoda ne var?

- **Jupyter notebook’lar** — model eğitimi ve veri işleme kodları.
- **Notebook içinde kayıtlı sonuçlar** — grafikler ve metrikler; projeyi yeniden çalıştırmadan inceleyebilirsiniz.
- **Ham veri setleri ve eğitilmiş model dosyaları repoda yok** — yalnızca kod ve örnek çıktılar.

### Kimler için?

İnsan kaynakları ve teknik olmayan okuyucular için kısa özet ve öne çıkan projeler aşağıda. Teknik detay için tablodaki linklerden ilgili notebook’a gidebilirsiniz.

### Klasör yapısı

Kodlar `projects/` altında **yıl → alan → (isteğe bağlı proje klasörü)** şeklinde düzenlenir. Colab şablonları portföye dahil değildir; [`templates/`](templates/) klasöründedir.

| Klasör (`projects/…/`) | Ne tür iş? |
|------------------------|------------|
| `classification/` | Görüntü sınıflandırma |
| `object-detection/` | Kutu ile bulgu / nesne tespiti |
| `medical/` | Tıbbi görüntü ve sinyal, veri pipeline |
| `segmentation/` | Piksel düzeyinde segmentasyon |
| `generative/` | Autoencoder, GAN |
| `llm/` | Büyük dil modeli denemeleri |

Bazı nesne tespiti konuları alt klasörde toplanır: `airplane-detection/`, `teknofest-abdominal-ct/`, `abdominal-ct-detection/`, `dermatology-detection/`, `tools/` (script’ler).

### Öne çıkan çalışmalar

1. **Mammografi analizi (mezuniyet projesi)** — Mamografi görüntülerinde model eğitimi ve analiz sürecini uçtan uca işledim. [Notebook](projects/2023/medical/mammography-training.ipynb)

2. **Meme kanseri veri pipeline’ı** — Görüntü ve etiketlerin modele hazırlanması için uçtan uca veri işleme akışı kurdum. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)

3. **Pnömoni tespiti (göğüs röntgeni)** — Göğüs röntgenlerinde pnömoni / normal ayrımı için derin öğrenme modeli eğittim. [Notebook](projects/2023/classification/pneumonia-classification.ipynb)

4. **Teknofest — karın BT bulgu tespiti** — Yarışma kapsamında BT kesitlerinde çok sınıflı bulgu tespiti modeli geliştirdim. [Notebook (2022)](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb)

5. **Dermatoloji lezyon tespiti** — Cilt görüntülerinde lezyon tespiti; büyük görüntüler için dilimli (SAHI) inference denemesi. [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [YOLOv5 + SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb)

6. **Histopatoloji sınıflandırma** — Mikroskop görüntülerinde transfer learning ile kanser / doku sınıflandırması (VGG16, Xception). [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb)

### Tüm projeler (özet)

| Proje | Alan | Yıl | Kısa açıklama | Detay |
|-------|------|-----|---------------|--------|
| Mammografi eğitimi | Tıbbi görüntü | 2023 | Mezuniyet projesi — mamografi model eğitimi | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Meme kanseri veri pipeline’ı | Veri hazırlığı | 2023 | Etiket ve görüntü ön işleme akışı | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Meme kanseri sınıflandırma | Sınıflandırma | 2023 | Inception tabanlı sınıflandırma | [notebook](projects/2023/classification/inception-breast-cancer.ipynb) |
| Pnömoni sınıflandırma | Sınıflandırma | 2023 | Göğüs röntgeni — pnömoni tespiti | [notebook](projects/2023/classification/pneumonia-classification.ipynb) |
| DICOM → JPG dönüşümü | Veri hazırlığı | 2023 | Tıbbi DICOM formatından görüntü üretimi | [notebook](projects/2023/medical/dicom-to-jpg.ipynb) |
| Tıbbi veri işleme | Veri hazırlığı | 2023 | Genel tıbbi görüntü işleme yardımcıları | [notebook](projects/2023/medical/medical-image-utilities.ipynb) |
| DICOM dönüşüm (2022) | Veri hazırlığı | 2022 | Erken DICOM dönüşüm denemeleri | [notebook](projects/2022/medical/dcm-convert.ipynb) |
| MIT-BIH aritmi analizi | Tıbbi sinyal | 2022 | EKG kayıtlarında aritmi veri analizi | [notebook](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Karın BT bulgu tespiti | Nesne tespiti | 2022–2023 | Teknofest (2022) ve Faster R-CNN ile BT tespiti (2023) | [2022](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) |
| Uçak tespiti | Nesne tespiti | 2022–2023 | R-CNN → Faster R-CNN / Detectron2 geliştirme süreci | [2022 R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) |
| Dermatoloji lezyon tespiti | Nesne tespiti | 2023 | YOLOv5 ve büyük görüntüler için SAHI | [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Histopatoloji veri hazırlığı | Veri hazırlığı | 2022 | Çoklu büyütme (40×–400×) veri seti düzenleme | [notebook](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Histopatoloji — VGG16 | Sınıflandırma | 2022 | Transfer learning ile doku sınıflandırma | [notebook](projects/2022/classification/vgg16-histopathology-classifier.ipynb) |
| Histopatoloji — Xception (çok sınıflı) | Sınıflandırma | 2022 | Xception ile çok sınıflı sınıflandırma | [notebook](projects/2022/classification/xception-histopathology-classifier.ipynb) |
| Histopatoloji — Xception (ikili) | Sınıflandırma | 2022 | İkili (kanser / normal) sınıflandırma | [notebook](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) |
| Autoencoder | Üretken model | 2022 | Autoencoder eğitimi | [notebook](projects/2022/generative/autoencoders.ipynb) |
| GAN denemeleri | Üretken model | 2022 | GAN modelleri (genel ve MURA dirsek verisi) | [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| Görüntü segmentasyonu | Segmentasyon | 2022–2023 | scikit-image örneği (2022) ve segmentasyon demosu (2023) | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |
| Erken LLM / AI denemesi | Diğer | 2023 | Büyük dil modelleri ile erken deneme | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |
| Etiket dönüştürücü (XML → CSV) | Veri hazırlığı | 2022 | Nesne tespiti etiketlerini CSV formatına çevirme | [script](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |

### Şablonlar

[`templates/`](templates/) klasöründe YOLO / R-CNN ve veri formatı dönüşümü için **Colab başlangıç notebook’ları** var. Bunlar portföy projesi değil; yeni deneyler için şablon niteliğindedir.

### Nasıl inceleyebilirsiniz?

1. Tablodaki linke tıklayın.
2. GitHub’da notebook açıldığında aşağı kaydırın — eğitim grafikleri ve örnek çıktılar hücrelerde görünür.
3. Kodu çalıştırmak için notebook’u indirip Jupyter veya Google Colab kullanabilirsiniz (veri setleri repoda olmadığı için bazı hücreler yerel veri gerektirir).

### Kullandığım araçlar

Python · Jupyter · Google Colab · TensorFlow / Keras · PyTorch · Detectron2 · YOLOv5 · OpenCV · scikit-image · SAHI

### Kaynaklar

Projeler açık kaynak kütüphaneler ve eğitim materyallerinden yararlanılarak geliştirildi (Mask R-CNN, Detectron2, Ultralytics YOLOv5 vb.). Üçüncü taraf veri setleri ve kopyalanmış tutorial kodları bu repoda yer almaz.

### İletişim

[LinkedIn profilim](https://linkedin.com/in/YOUR-PROFILE) *(URL’yi kendi profilinizle güncelleyin)*

### Lisans

MIT — ayrıntılar için [LICENSE](LICENSE).

### GitHub *(isteğe bağlı)*

Repo **About** alanına kısa açıklama ve konular ekleyebilirsiniz: `machine-learning`, `computer-vision`, `medical-imaging`, `jupyter-notebook`.

---

## English

**My Portfolio — computer vision and medical imaging projects from 2022–2023.**

This repository collects my **image processing and medical image analysis** work from university and competition projects. I focused on finding abnormalities in X-rays, CT, and mammography, plus data preparation and model training.

### What is in this repo?

- **Jupyter notebooks** — training and data pipeline code.
- **Saved outputs inside notebooks** — plots and metrics so you can review without re-running training.
- **Raw datasets and model weight files are not included** — only code and sample results.

### Who is this for?

A short summary and highlighted projects for recruiters and non-technical readers. For technical depth, open the linked notebooks in the table below.

### Folder layout

Code lives under `projects/` as **year → area → (optional project folder)**. Colab starters are not portfolio work; see [`templates/`](templates/).

| Folder (`projects/…/`) | What it covers |
|------------------------|----------------|
| `classification/` | Image classification |
| `object-detection/` | Bounding-box detection |
| `medical/` | Medical imaging, signals, data pipelines |
| `segmentation/` | Pixel-level segmentation |
| `generative/` | Autoencoders, GANs |
| `llm/` | Large language model experiments |

Some object-detection topics are grouped in subfolders: `airplane-detection/`, `teknofest-abdominal-ct/`, `abdominal-ct-detection/`, `dermatology-detection/`, `tools/` (scripts).

### Highlighted work

1. **Mammography analysis (graduation project)** — End-to-end mammography model training and analysis. [Notebook](projects/2023/medical/mammography-training.ipynb)

2. **Breast cancer data pipeline** — Full preprocessing workflow to prepare images and labels for modeling. [Notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb)

3. **Pneumonia detection (chest X-ray)** — Deep learning classifier for pneumonia vs. normal chest X-rays. [Notebook](projects/2023/classification/pneumonia-classification.ipynb)

4. **Teknofest — abdominal CT abnormality detection** — Multi-class object detection on CT slices for a competition project. [Notebook (2022)](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb)

5. **Dermatology lesion detection** — Lesion detection on skin images, including sliced inference (SAHI) for large images. [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [YOLOv5 + SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb)

6. **Histopathology classification** — Transfer learning on microscope images (VGG16, Xception). [VGG16](projects/2022/classification/vgg16-histopathology-classifier.ipynb) · [Xception](projects/2022/classification/xception-histopathology-classifier.ipynb)

### All projects (summary)

| Project | Area | Year | Summary | Details |
|---------|------|------|---------|---------|
| Mammography training | Medical imaging | 2023 | Graduation project — mammography model training | [notebook](projects/2023/medical/mammography-training.ipynb) |
| Breast cancer data pipeline | Data prep | 2023 | Image and label preprocessing workflow | [notebook](projects/2023/medical/breast-cancer-data-pipeline.ipynb) |
| Breast cancer classification | Classification | 2023 | Inception-based classification | [notebook](projects/2023/classification/inception-breast-cancer.ipynb) |
| Pneumonia classification | Classification | 2023 | Chest X-ray pneumonia detection | [notebook](projects/2023/classification/pneumonia-classification.ipynb) |
| DICOM to JPG | Data prep | 2023 | Convert medical DICOM to image files | [notebook](projects/2023/medical/dicom-to-jpg.ipynb) |
| Medical data processing | Data prep | 2023 | General medical image utilities | [notebook](projects/2023/medical/medical-image-utilities.ipynb) |
| DICOM conversion (2022) | Data prep | 2022 | Early DICOM conversion experiments | [notebook](projects/2022/medical/dcm-convert.ipynb) |
| MIT-BIH arrhythmia analysis | Medical signal | 2022 | ECG arrhythmia dataset analysis | [notebook](projects/2022/medical/mit-bih-arrhythmia.ipynb) |
| Abdominal CT detection | Object detection | 2022–2023 | Teknofest (2022) and Faster R-CNN on CT (2023) | [2022](projects/2022/object-detection/teknofest-abdominal-ct/teknofest-abdominal-ct-detection.ipynb) · [2023](projects/2023/object-detection/abdominal-ct-detection/faster-rcnn-abdominal-ct-detection.ipynb) |
| Airplane detection | Object detection | 2022–2023 | R-CNN through Faster R-CNN / Detectron2 iterations | [2022 R-CNN](projects/2022/object-detection/airplane-detection/rcnn-airplane-detection.ipynb) · [2023 Faster R-CNN](projects/2023/object-detection/airplane-detection/faster-rcnn-airplane-detection.ipynb) · [Detectron2](projects/2023/object-detection/airplane-detection/detectron2-airplane-detection.ipynb) |
| Dermatology lesion detection | Object detection | 2023 | YOLOv5 and SAHI for large images | [YOLOv5](projects/2023/object-detection/dermatology-detection/yolov5-dermatology-detection.ipynb) · [SAHI](projects/2023/object-detection/dermatology-detection/yolov5-sahi-dermatology-detection.ipynb) |
| Histopathology dataset prep | Data prep | 2022 | Multi-magnification (40×–400×) dataset organization | [notebook](projects/2022/classification/histopathology-dataset-preparation.ipynb) |
| Histopathology — VGG16 | Classification | 2022 | Transfer learning for tissue classes | [notebook](projects/2022/classification/vgg16-histopathology-classifier.ipynb) |
| Histopathology — Xception (multi-class) | Classification | 2022 | Multi-class Xception classifier | [notebook](projects/2022/classification/xception-histopathology-classifier.ipynb) |
| Histopathology — Xception (binary) | Classification | 2022 | Binary cancer vs. normal classification | [notebook](projects/2022/classification/xception-binary-histopathology-classifier.ipynb) |
| Autoencoders | Generative | 2022 | Autoencoder training | [notebook](projects/2022/generative/autoencoders.ipynb) |
| GAN experiments | Generative | 2022 | GAN models (general and MURA elbow dataset) | [GAN](projects/2022/generative/gans.ipynb) · [GAN v2](projects/2022/generative/gans-v2.ipynb) · [MURA](projects/2022/generative/mura-elbow-gans.ipynb) |
| Image segmentation | Segmentation | 2022–2023 | scikit-image example (2022) and demo (2023) | [2022](projects/2022/segmentation/segmentation-skimage.ipynb) · [2023](projects/2023/segmentation/segmentation-demo.ipynb) |
| Early LLM / AI experiment | Other | 2023 | Early large language model experimentation | [notebook](projects/2023/llm/llm-prompt-experiment.ipynb) |
| Annotation converter (XML → CSV) | Data prep | 2022 | Pascal VOC XML annotations to CSV | [script](projects/2022/object-detection/tools/xml-annotation-to-csv.py) |

### Templates

The [`templates/`](templates/) folder contains **Colab starter notebooks** for YOLO / R-CNN and label format conversion. These are not portfolio deliverables — they are starting points for new experiments.

### How to review

1. Click a link in the table.
2. Scroll through the notebook on GitHub to see training plots and sample outputs.
3. To run code locally, download the notebook and use Jupyter or Google Colab (some cells expect datasets that are not in this repo).

### Tools used

Python · Jupyter · Google Colab · TensorFlow / Keras · PyTorch · Detectron2 · YOLOv5 · OpenCV · scikit-image · SAHI

### Acknowledgments

Built with open-source libraries and tutorials (Mask R-CNN, Detectron2, Ultralytics YOLOv5, and others). Third-party datasets and vendored tutorial code are not included in this repository.

### Contact

[My LinkedIn profile](https://linkedin.com/in/YOUR-PROFILE) *(replace with your profile URL)*

### License

MIT — see [LICENSE](LICENSE).
