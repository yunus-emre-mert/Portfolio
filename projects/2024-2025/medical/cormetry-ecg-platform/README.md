# Cormetry Health — Platform API’si ve Cihazdan Buluta EKG Veri Yolu

*Cormetry Health — Platform API and Device-to-Cloud ECG Data Path*

[Türkçe](#türkçe) · [English](#english)

> **Gizlilik / Confidentiality:** Bu sayfa ticari bir ürün için yapılan işi ve mimari yaklaşımı özetler; kaynak kod, donanım detayları ve protokoller **fikri mülkiyet (IP) ve NDA** kapsamında paylaşılmaz. / This page summarizes work on a commercial product; source code, hardware details, and protocols are not shared under **IP and NDA** obligations.

---

## Türkçe

### Özet

**Cormetry Health**’te giyilebilir 12 derivasyonlu EKG için **platform API’sini** ve **cihazdan buluta veri yolunu** tasarladım. FastAPI servisinde istek ve yanıt sözleşmeleri **Pydantic** ile tanımlı, davranış **pytest** ile doğrulanır. Hasta kaydı kendi cihazından **Bluetooth Low Energy** ile alınır; doktor yalnızca kendisine atanmış hastaları görür ve bu izolasyon **veritabanında (RLS)** zorunludur. Aynı API mobil istemciye, bulut backend’ine ve doktor web paneline hizmet verir. Panelde açıklanabilir, kural tabanlı EKG analizi bir ürün özelliği olarak durur.

| | |
|---|---|
| **Rol** | Software Engineer (2024 – Kasım 2026). Platform API’si, BLE alımı, gerçek zamanlı sinyal hatları; firmware doğrulaması; TÜBİTAK 1512 yürütmesi |
| **Dönem** | 2024 – Kasım 2026 |
| **Kurum** | Cormetry Health Teknoloji A.Ş. |
| **Alan** | Kardiyoloji / dijital sağlık / medikal cihaz yazılımı |
| **Çekirdek teknolojiler** | FastAPI, Pydantic, pytest, React Native (Expo), React + Vite, TypeScript, Supabase (PostgreSQL, Auth, Storage, RLS), Bluetooth Low Energy |

**Öne çıkanlar**

- **Platform API’si:** FastAPI servisi; istek ve yanıt sözleşmeleri **Pydantic** ile, davranış **pytest** ile doğrulanır.
- **Hasta / doktor rolleri** ve **veritabanı düzeyinde veri izolasyonu (RLS)**: doktor yalnızca kendisine atanmış hastaları, hasta yalnızca kendi kayıtlarını görür.
- **Cihazdan buluta veri yolu:** BLE alımı, bulut backend’i ve doktor web paneli aynı API’nin arkasında durur.
- 8 fiziksel kanaldan **12 derivasyonlu**, EKG kâğıdı görünümünde inceleme (mobil ve web).
- Doktor panelinde **açıklanabilir, kural tabanlı otomatik EKG analizi**.
- Bluetooth üzerinde veri kaybına dayanıklı sinyal işleme ve simülatörle doğrulanmış kalibrasyon.
- Dış tedarikçiden alınan firmware ve PCB geliştirmesinin **yazılım gereksinimlerine göre entegrasyonu ve gerçek cihazla doğrulanması**.
- **TÜBİTAK BİGG 1512** projesinin uçtan uca yönetilmesi: iş planı, dönem raporları, bütçe takibi, **yatırımcı ve hakem sunumlarında teknik sunumlar** ve canlı prototip demosu.

### Problem

Klinik EKG cihazları pahalı, sabit ve verileri paylaşmak zahmetli. Hedef; hastanın taşınabilir bir cihazla kaydı kendisinin alabildiği, kaydın otomatik olarak buluta yüklendiği ve atanmış doktorun kaydı web üzerinden profesyonel EKG görünümünde inceleyebildiği bir sistem kurmaktı.

### Çözüm

```mermaid
flowchart LR
    device[EKG_cihazi] -->|Bluetooth| mobile[Mobil_uygulama_hasta]
    mobile --> cloud["Bulut: veritabani + dosya deposu"]
    mobile --> api["FastAPI + Pydantic"]
    api --> cloud
    cloud --> web[Doktor_web_paneli]
    web --> api
    web --> analysis[Otomatik_EKG_analizi]
```

1. **EKG cihazı:** Medikal sınıf 24-bit analog ön uç, mikrodenetleyici ve BLE modülünden oluşan, 10 elektrotla 500 örnek/saniye ölçüm yapan taşınabilir cihaz.
2. **Mobil uygulama (hasta):** Cihazı bulur, bağlanır, kısa bir EKG kaydı alır, sinyali işler ve buluta yükler. Geçmiş kayıtlar 12 derivasyonlu EKG kâğıdı görünümünde izlenir.
3. **Doktor web paneli:** Doktor kendisine atanmış hastaları ve kayıtlarını görür, filtrelenmiş 12 derivasyon görünümünü inceler ve otomatik analiz sonuçlarını okur.
4. **Platform API’si:** FastAPI servisi, mobil ve web istemcilerinin yanında durur. Veri, kimlik ve dosya katmanı Supabase üzerinde kalır.

### Platform API’si

Platform için bir **FastAPI** servisi yazdım. İstek ve yanıt sözleşmeleri **Pydantic** modelleriyle tanımlı. Servisin davranışı **pytest** ile doğrulanır. Veri, kimlik ve dosya katmanı **Supabase** (PostgreSQL, Auth, Storage, RLS) üzerinde durur.

### Roller ve veri güvenliği

- **Hasta:** Kaydı kendisi alır; yalnızca kendi kayıtlarını görür.
- **Doktor:** Yalnızca kendisine atanmış hastaları ve onların kayıtlarını görür, yönetir ve inceler.
- Yetkilendirme uygulama katmanında değil, **veritabanı katmanında (Row Level Security)** uygulanır; aynı kural kayıt dosyalarının saklandığı depoya da uygulanır.
- Rol ve modül erişim mantığı mobil ve web için **ortak bir katmanda** tutulur.

### Mobil uygulama

- Bluetooth Low Energy ile cihaz tarama, bağlantı ve kararlı veri akışı; bağlantı hatalarına karşı yeniden deneme.
- Kayıt oturumu: ham veri ve kayıt bilgileri otomatik olarak buluta yüklenir.
- EKG kâğıdı ızgarası üzerinde 12 derivasyon görüntüleyici; kullanıcının seçebildiği dijital filtreler (yüksek geçiren, alçak geçiren, şebeke paraziti).

### Doktor web paneli

- Hasta listesi, hasta bazlı kayıt geçmişi ve profil sayfaları.
- Mobil ile aynı sinyal işleme hattını kullanan 12 derivasyon EKG monitörü.
- Kayıt yönetimi (yeniden adlandırma, silme, ham veriyi indirme).
- **Açıklanabilir, kural tabanlı EKG analizi:**
  - Sinyal kalitesi (taban hattı kayması, şebeke paraziti, artefakt, elektrot teması).
  - Vuru tespiti ve dalga sınırları; temel aralık ölçümleri (RR, PR, QRS, QT / QTc).
  - Elektriksel aks.
  - Ritim, ileti, ST-T ve hipertrofi bulguları.

### Sinyal işleme

- Cihazdan gelen ham sinyalin uçtan uca işlenmesi: bayttan milivolta, kanaldan derivasyona, oradan analize.
- Bluetooth üzerinde oluşabilen veri kayıplarına karşı **kendini toparlayan** bir çözümleme yaklaşımı.
- 8 fiziksel kanaldan standart formüllerle **12 derivasyon** türetilmesi.
- Klinik ölçeğe dönüşümün bir **EKG simülatörüyle doğrulanması**.

### Mimari ve kod kalitesi

- Mobil ve web uygulamaları tek bir **monorepo** içinde; iki platformda paylaşılan rol/erişim katmanı.
- Her iki uygulamada da katmanlı (feature-sliced) mimari.
- Ortak tasarım token'ları ve bileşenlerden oluşan bir tasarım sistemi.
- Fiziksel cihazla geliştirmeyi hızlandıran otomasyon scriptleri ve Android build profilleri.

### TÜBİTAK BİGG 1512 proje yürütmesi

Proje, **TÜBİTAK BİGG 1512** kapsamında **900.000 TL hibe** ile desteklendi. Projeyi uçtan uca yönettim:

- İş planına göre iş-zaman, kapsam ve bütçe takibi; dönem raporları.
- TÜBİTAK hakem değerlendirmelerinde proje sunumu ve prototipin canlı demosu.
- Yatırımcılara yönelik teknik sunumlar.

### Donanım entegrasyonu

Firmware ve PCB geliştirmesi dış hizmet olarak alındı. Bu süreçte:

- Yazılım ihtiyaçlarına göre donanım gereksinimlerini tanımladım (örnekleme hızı, kanal yapısı, veri ve komut protokolü).
- Tedarikçiden gelen teslimleri uygulamaya entegre edip gerçek cihazla doğruladım.
- Protokol ve donanım tarafındaki belirsizlikleri tespit edip netleştirilmesini sağladım.
- Hata ayıklamada donanım ve yazılım kaynaklı sorunları ayırt edip ilgili tarafa yönlendirdim.

### Çözülen problemler

- Bluetooth üzerinde veri kaybı yaşansa da sinyalin bozulmadan görüntülenmesi.
- 8 fiziksel kanaldan tam 12 derivasyon görünümü.
- Ham cihaz verisinin doğrulanmış klinik ölçeğe çevrilmesi.
- Doktor–hasta veri gizliliğinin veritabanı düzeyinde garanti altına alınması.

### Teknoloji yığını

- **Mobil:** React Native, Expo, TypeScript, Bluetooth Low Energy, React Navigation
- **Web:** React, Vite, TypeScript, Radix UI
- **Backend:** Supabase (PostgreSQL, Auth, Storage, Row Level Security), FastAPI, Pydantic
- **Test:** pytest
- **Araçlar:** npm workspaces, EAS Build, Vercel

### Rolüm

- Software Engineer olarak mobil, web, backend ve cihaz entegrasyonunun uçtan uca geliştirilmesi.
- Platform API’si: FastAPI servisi, Pydantic sözleşmeleri ve pytest.
- TÜBİTAK 1512 kapsamında proje yürütmesi: iş planı, dönem raporları, yatırımcı ve hakem sunumları, canlı prototip demosu.
- Hasta / doktor rol modeli ve veritabanı düzeyinde yetkilendirme (RLS).
- Gömülü cihazdan gelen sinyal için uçtan uca veri hattı ve kural tabanlı EKG analizi.
- Dış tedarikçiden gelen firmware ve PCB teslimlerinin yazılım gereksinimlerine göre entegrasyonu ve gerçek cihazla doğrulanması.
- Klinik kohort hattı ve etiketleme iş istasyonu — [vaka analizi](../../../2026/medical/ecg-coronary-stenosis/README.md). PTB-XL değerlendirme hattı — [proje](../../../2026/medical/ecg-ptbxl-ensemble/README.md).

### Durum

Ticari ürün geliştirme. Kaynak kod, donanım detayları ve protokoller **IP / NDA** nedeniyle paylaşılmamaktadır.

---

## English

### Summary

At **Cormetry Health** I designed the **platform API** and the **device-to-cloud data path** for a wearable 12-lead ECG. Request and response contracts on the FastAPI service are **Pydantic** models; behavior is checked with **pytest**. The patient records on their own device over **Bluetooth Low Energy**; a doctor sees only assigned patients, and that isolation is enforced **in the database (RLS)**. The same API serves the mobile client, the cloud backend, and the doctor web panel. Explainable, rule-based ECG analysis is a product feature on that panel.

| | |
|---|---|
| **Role** | Software Engineer (2024 – November 2026). Platform API, BLE ingestion, real-time signal pipelines; firmware validation; TÜBİTAK 1512 delivery |
| **Period** | 2024 – November 2026 |
| **Organization** | Cormetry Health Teknoloji A.Ş. |
| **Domain** | Cardiology / digital health / medical device software |
| **Core technologies** | FastAPI, Pydantic, pytest, React Native (Expo), React + Vite, TypeScript, Supabase (PostgreSQL, Auth, Storage, RLS), Bluetooth Low Energy |

**Highlights**

- **Platform API:** FastAPI service; request and response contracts with **Pydantic**, behavior checked with **pytest**.
- **Patient / doctor roles** with **database-level isolation (RLS)**: a doctor sees only assigned patients, and a patient sees only their own recordings.
- **Device-to-cloud data path:** BLE ingestion, the cloud backend, and the doctor web panel sit behind the same API.
- **12-lead** review in an ECG-paper view (mobile and web), derived from 8 physical channels.
- **Explainable, rule-based automated ECG analysis** on the doctor panel.
- Signal handling that tolerates data loss over Bluetooth, and calibration verified with a simulator.
- **Integrated and validated the outsourced firmware and PCB** against software requirements, on the real device.
- **Managed the TÜBİTAK BİGG 1512 project end to end:** work plan, period reports, budget tracking, **technical presentations to investors and reviewers**, and live prototype demos.

### Problem

Clinical ECG devices are expensive, stationary, and make sharing data cumbersome. The goal was a system where patients take recordings themselves with a portable device, recordings are uploaded to the cloud automatically, and the assigned doctor reviews them on the web in a professional ECG view.

### Solution

```mermaid
flowchart LR
    device[ECG_device] -->|Bluetooth| mobile[Mobile_app_patient]
    mobile --> cloud["Cloud: database + file storage"]
    mobile --> api["FastAPI + Pydantic"]
    api --> cloud
    cloud --> web[Doctor_web_panel]
    web --> api
    web --> analysis[Automated_ECG_analysis]
```

1. **ECG device:** A portable device with a medical-grade 24-bit analog front end, a microcontroller, and a BLE module, measuring through 10 electrodes at 500 samples per second.
2. **Mobile app (patient):** Finds and connects to the device, takes a short ECG recording, processes the signal, and uploads it. Past recordings are shown in a 12-lead ECG-paper view.
3. **Doctor web panel:** The doctor sees assigned patients and their recordings, reviews the filtered 12-lead view, and reads the automated analysis results.
4. **Platform API:** A FastAPI service sits beside the mobile and web clients. Data, identity, and files stay on Supabase.

### Platform API

I built a **FastAPI** service for the platform. Request and response contracts are **Pydantic** models. Service behavior is checked with **pytest**. Data, identity, and files stay on **Supabase** (PostgreSQL, Auth, Storage, RLS).

### Roles and data security

- **Patient:** Takes recordings and sees only their own recordings.
- **Doctor:** Sees, manages, and reviews only the patients assigned to them and their recordings.
- Authorization is enforced at the **database layer (Row Level Security)**, not in the app; the same rule applies to the storage holding recording files.
- Role and module access logic lives in a **shared layer** used by both mobile and web.

### Mobile app

- Bluetooth Low Energy device scanning, connection, and a stable data stream, with retries on connection errors.
- Recording session: raw data and recording details are uploaded to the cloud automatically.
- 12-lead viewer on an ECG-paper grid, with user-selectable digital filters (high-pass, low-pass, mains interference).

### Doctor web panel

- Patient list, per-patient recording history, and profile pages.
- A 12-lead ECG monitor using the same signal processing pipeline as mobile.
- Recording management (rename, delete, download raw data).
- **Explainable, rule-based ECG analysis:**
  - Signal quality (baseline wander, mains interference, artifacts, electrode contact).
  - Beat detection and wave boundaries; core interval measurements (RR, PR, QRS, QT / QTc).
  - Electrical axis.
  - Rhythm, conduction, ST-T, and hypertrophy findings.

### Signal processing

- End-to-end processing of the raw device signal: from bytes to millivolts, from channels to leads, and on to analysis.
- A **self-recovering** parsing approach that handles data loss over Bluetooth.
- **12 leads** derived from 8 physical channels with standard formulas.
- Conversion to clinical scale **verified with an ECG simulator**.

### Architecture and code quality

- Mobile and web apps in one **monorepo**, with a role/access layer shared across both.
- Layered (feature-sliced) architecture in both apps.
- A design system built from shared design tokens and components.
- Automation scripts and Android build profiles that speed up development on a physical device.

### TÜBİTAK BİGG 1512 project execution

The project was funded with a **900,000 TRY grant** under **TÜBİTAK BİGG 1512**. I managed the project end to end:

- Work-time, scope, and budget tracking against the business plan; period reports.
- Project presentation and a live prototype demo at TÜBİTAK reviewer evaluations.
- Technical presentations to investors.

### Hardware integration

Firmware and PCB development were outsourced. In this process I:

- Defined hardware requirements from the software's needs (sampling rate, channel layout, data and command protocol).
- Integrated vendor deliveries into the app and validated them on the real device.
- Found ambiguities on the protocol and hardware side and got them clarified.
- During debugging, separated hardware issues from software issues and routed them to the right party.

### Problems solved

- Showing the signal intact even when data is lost over Bluetooth.
- A full 12-lead view from 8 physical channels.
- Converting raw device data to a verified clinical scale.
- Guaranteeing doctor–patient data privacy at the database level.

### Tech stack

- **Mobile:** React Native, Expo, TypeScript, Bluetooth Low Energy, React Navigation
- **Web:** React, Vite, TypeScript, Radix UI
- **Backend:** Supabase (PostgreSQL, Auth, Storage, Row Level Security), FastAPI, Pydantic
- **Tests:** pytest
- **Tools:** npm workspaces, EAS Build, Vercel

### My role

- As a Software Engineer, end-to-end development of mobile, web, backend, and device integration.
- Platform API: FastAPI service, Pydantic contracts, and pytest.
- TÜBİTAK 1512 project execution: work plan, period reports, investor and reviewer presentations, and live prototype demos.
- Patient / doctor role model and database-level authorization (RLS).
- End-to-end data pipeline for the embedded device signal and rule-based ECG analysis.
- Integrated vendor firmware and PCB deliveries against software requirements and validated them on the real device.
- Clinical cohort pipeline and labeling workstation — [case study](../../../2026/medical/ecg-coronary-stenosis/README.md). PTB-XL evaluation pipeline — [project](../../../2026/medical/ecg-ptbxl-ensemble/README.md).

### Status

Commercial product development. Source code, hardware details, and protocols are not shared because of **IP / NDA**.
