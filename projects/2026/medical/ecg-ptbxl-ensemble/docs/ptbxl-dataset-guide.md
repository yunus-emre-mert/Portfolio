# PTB-XL Veri Seti Rehberi (v1.0.3)

Bu belge, PhysioNet üzerindeki **PTB-XL 1.0.3** kopyasını kod yazmak için yeterli ayrıntıda anlatır.

**Bu repodaki eğitim pipeline’ı** (bu klasördeki 00–06 notebook'ları ve `ecg_common.py`): resmi `strat_fold` 1–8 / 9 / 10; 01–03 / 02.1 `processed/sr100/`; ECGFounder (notebook 04) native 500 Hz `processed/sr500/`; standart tahminler `results/<model>/seed_<seed>/`. Notebook işlemleri: [`README.md`](../README.md).

Ham sinyal dosyalarına bakmadan yükleme, etiketleme, bölme ve yaygın tuzaklar aşağıdadır.

- **Kaynak:** Wagner et al., *PTB-XL, a large publicly available electrocardiography dataset*, Scientific Data 7, 154 (2020)
- **PhysioNet:** https://physionet.org/content/ptb-xl/1.0.3/
- **DOI:** 10.13026/kfzx-aw45
- **Lisans:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Yerel klasör adı:** `ptb-xl-a-large-publicly-available-electrocardiography-dataset-1.0.3/`

Aşağıda `DATA_ROOT` bu klasörün yolu anlamına gelir. Örnek yükleme kodundaki `path` değişkeni **sonda `/` (veya Windows’ta `\`)** içermelidir; yollar `path + filename_lr` ile birleştirilir.

---

## 1. Veri seti nedir?

PTB-XL, Almanya PTB (Physikalisch-Technische Bundesanstalt) klinik arşivinden gelen **12 derivasyonlu, 10 saniyelik** dinlenme EKG kayıtlarıdır.

| Ölçek | Değer |
|---|---|
| Kayıt sayısı | **21.799** |
| Hasta sayısı | **18.869** |
| Hasta başına kayıt | ortalama ~1.16; min 1, max 10 |
| Süre | 10 saniye |
| Derivasyon | 12 lead, standart sıra |
| Örnekleme | 100 Hz **ve** 500 Hz (aynı kayıtların iki kopyası) |
| Biçim | WFDB (`.hea` + `.dat`) |
| Etiket standardı | SCP-ECG (71 ifade) |
| Kayıt tarih aralığı | 1984-11-09 → 2001-06-11 |

Aynı hastanın birden fazla kaydı olabilir. **Aynı `patient_id` asla birden fazla `strat_fold` içinde yer almaz.** Train/test bölerken `strat_fold` kullanılmazsa hasta sızıntısı olur.

---

## 2. Klasör ağacı

```
DATA_ROOT/
├── ptbxl_database.csv      # kayıt meta verisi + etiketler (21.799 satır)
├── scp_statements.csv      # 71 SCP kodunun sözlüğü ve sınıf hiyerarşisi
├── RECORDS                 # WFDB kayıt listesi (uzantısız yollar)
├── SHA256SUMS.txt          # dosya bütünlük özetleri
├── LICENSE.txt             # CC BY 4.0
├── example_physionet.py    # resmi yükleme örneği
├── records100/             # 100 Hz sinyaller
│   ├── 00000/
│   ├── 01000/
│   ├── ...
│   └── 21000/
└── records500/             # 500 Hz sinyaller
    ├── 00000/
    ├── 01000/
    ├── ...
    └── 21000/
```

`records100` ve `records500` altında **22 alt klasör** vardır:

`00000, 01000, 02000, …, 21000`

Her kayıt için iki dosya vardır: `.hea` (başlık, metin) ve `.dat` (ikili sinyal). Toplam:

- `records100`: 21.799 `.hea` + 21.799 `.dat` (CSV ile aynı evren)
- `records500`: 21.799 `.hea` + 21.799 `.dat`

`RECORDS` dosyası önce tüm 100 Hz, sonra tüm 500 Hz yollarını listeler (21.799 × 2 satır). Satır örneği:

```
records100/00000/00001_lr
records500/00000/00001_hr
```

Uzantı **yazılmaz**. `wfdb.rdsamp()` tam olarak bu gövdeyi bekler.

---

## 3. Dosya adı ve yol formülü

`ecg_id` CSV’de **21.799** satırdır. Yolu kendin üretmek yerine **CSV’den `filename_lr` / `filename_hr` oku**.

```
folder   = f"{(ecg_id // 1000) * 1000:05d}"
lr_stem  = f"records100/{folder}/{ecg_id:05d}_lr"
hr_stem  = f"records500/{folder}/{ecg_id:05d}_hr"
```

Örnekler:

| ecg_id | 100 Hz gövde | 500 Hz gövde |
|---|---|---|
| 1 | `records100/00000/00001_lr` | `records500/00000/00001_hr` |
| 999 | `records100/00000/00999_lr` | `records500/00000/00999_hr` |
| 1000 | `records100/01000/01000_lr` | `records500/01000/01000_hr` |
| 21837 | `records100/21000/21837_lr` | `records500/21000/21837_hr` |

Son klasör (`21000`) 21000–21837 aralığındaki **kalan** kayıtları tutar. İlk klasör (`00000`) 00001–00999; `00000_lr` diye bir kayıt yoktur.

`ptbxl_database.csv` içindeki `filename_lr` / `filename_hr` sütunları tam olarak bu gövdelerdir. Yolu kendin üretmek yerine **CSV’den okumak** daha güvenlidir.

---

## 4. Sinyal biçimi (WFDB)

### 4.1 Başlık (`.hea`) sözleşmesi

100 Hz örnek (ilk satır):

```
00001_lr 12 100 1000
```

500 Hz örnek:

```
00001_hr 12 500 5000
```

Anlamı: `kayıt_adı  n_kanal  fs_Hz  n_örnek`

- Kanal sayısı: **12**
- Süre: her zaman **10 s** → 100 Hz’de 1000 örnek, 500 Hz’de 5000 örnek
- Kodlama: 16-bit signed integer (`fmt 16`)
- Kazanç: **1000.0 ADC birimi / mV**, baseline **0**
- Fiziksel birim: **mV**
- `wfdb.rdsamp()` kazancı uygulayarak **mV cinsinden float** döndürür

Ham dijital değerden mV:

```
mV = (digital_int16 - 0) / 1000.0
```

Dosya boyutu (kanal-interleaved 16-bit):

- 100 Hz `.dat`: `12 * 1000 * 2 = 24.000` byte
- 500 Hz `.dat`: `12 * 5000 * 2 = 120.000` byte

### 4.2 Derivasyon sırası (sabit)

WFDB `sig_name` sırası, indeks 0→11:

| İndeks | WFDB adı | Klinik ad |
|---|---|---|
| 0 | `I` | I |
| 1 | `II` | II |
| 2 | `III` | III |
| 3 | `AVR` | aVR |
| 4 | `AVL` | aVL |
| 5 | `AVF` | aVF |
| 6 | `V1` | V1 |
| 7 | `V2` | V2 |
| 8 | `V3` | V3 |
| 9 | `V4` | V4 |
| 10 | `V5` | V5 |
| 11 | `V6` | V6 |

**Dikkat:** dosyalarda `aVR` değil `AVR` yazar. Kodda lead ismi eşlemesi yapılırken bunu hesaba kat.

### 4.3 `wfdb.rdsamp` çıktısı

```python
signal, meta = wfdb.rdsamp(DATA_ROOT / "records100/00000/00001_lr")
# signal.shape == (1000, 12)   # 100 Hz
# signal.dtype == float64, birim mV
# meta['fs'] == 100
# meta['sig_name'] == ['I','II','III','AVR','AVL','AVF','V1','V2','V3','V4','V5','V6']
```

500 Hz için `signal.shape == (5000, 12)` ve `meta['fs'] == 500`.

Toplu yüklemede tensör şekli:

- 100 Hz: `(N, 1000, 12)`
- 500 Hz: `(N, 5000, 12)`

Bazı modeller kanal-önce bekler: `(N, 12, T)`. Dönüştürme: `np.transpose(X, (0, 2, 1))`.

### 4.4 Bellek uyarısı

Tüm kayıtları `float64` olarak RAM’e almak:

| Örnekleme | Yaklaşık RAM |
|---|---|
| 100 Hz | 21.799 × 1000 × 12 × 8 ≈ **2.1 GB** |
| 500 Hz | 21.799 × 5000 × 12 × 8 ≈ **10.5 GB** |

`float32` ile bu yarıya iner. Eğitim kodunda **tembel yükleme / batch** tercih edilmeli; resmi `example_physionet.py` her şeyi bir anda yükler, büyük makinelerde bile 500 Hz için ağırdır.

---

## 5. `ptbxl_database.csv` şeması

- Satır sayısı: **21.799** (başlık hariç)
- Birincil anahtar: `ecg_id`
- Resmi örnek kod: `pd.read_csv(..., index_col='ecg_id')`

### 5.1 Sütunlar

| Sütun | Pandas dtype (CSV okununca) | Eksik | Açıklama |
|---|---|---:|---|
| `ecg_id` | int64 | 0 | Kayıt kimliği (1.0.0 numaraları; CSV’de 21.799 satır) |
| `patient_id` | float64 | 0 | Hasta kimliği (aslında tamsayı; NaN olmadığı halde pandas float okur). **18.869** benzersiz |
| `age` | float64 | — | Yaş, yıl. ≥90 HIPAA için **300** kodu (1.0.3 PhysioNet açıklaması). Min/ortalama 00 notebook’ta ölçülür |
| `sex` | int64 | 0 | **0 = erkek, 1 = kadın** |
| `height` | float64 | 14.854 | cm. Doluysa ortalama≈166.7; min=6 ve max=209 (uç değer / hata olabilir) |
| `weight` | float64 | 12.408 | kg. Doluysa ortalama≈71.0; min=5, max=250 |
| `nurse` | float64 | 1.509 | Hemşire/teknisyen kimliği, 0–11 |
| `site` | float64 | 18 | Kayıt sitesi, 0–50 civarı; büyük çoğunluk 0, 1, 2 |
| `device` | object | 0 | Cihaz adı, 11 tür (aşağıda) |
| `recording_date` | object | 0 | `YYYY-MM-DD HH:MM:SS` |
| `report` | object | 0 | Serbest metin rapor, çoğunlukla **Almanca**, 9.883 benzersiz |
| `scp_codes` | object | 0 | Python dict **string**. Ana etiket alanı. Aşağıya bak |
| `heart_axis` | object | 8.505 | Elektriksel eksen: `MID, LAD, ALAD, RAD, ARAD, AXL, AXR, SAG` |
| `infarction_stadium1` | object | 16.211 | MI evresi: `unknown, Stadium I, Stadium I-II, Stadium II, Stadium II-III, Stadium III` |
| `infarction_stadium2` | object | 21.734 | İkinci evre (çok seyrek): `Stadium I/II/III` |
| `validated_by` | float64 | 9.411 | Doğrulayan kardiyolog kimliği 0–11 |
| `second_opinion` | bool | 0 | True: 557 |
| `initial_autogenerated_report` | bool | 0 | True: 6.813 (ilk rapor otomatik üretilmiş) |
| `validated_by_human` | bool | 0 | True: 16.094. **Fold 9 ve 10 tamamen True** |
| `baseline_drift` | object | 20.230 | Baseline drift olan lead’ler (serbest metin) |
| `static_noise` | object | 18.575 | Statik gürültü (serbest metin) |
| `burst_noise` | object | 21.224 | Patlama gürültüsü (serbest metin) |
| `electrodes_problems` | object | 21.807 | Elektrot sorunu, yalnızca 30 kayıt |
| `extra_beats` | object | 19.883 | Ekstra vurular; `1ES`, `SVES`, `VES` vb. 1.954 dolu |
| `pacemaker` | object | 21.544 | `ja, pacemaker` (287), birkaç belirsiz işaret |
| `strat_fold` | int64 | 0 | **1…10**, önerilen stratified split |
| `filename_lr` | object | 0 | 100 Hz WFDB gövdesi |
| `filename_hr` | object | 0 | 500 Hz WFDB gövdesi |

`patient_id`, `nurse`, `site`, `validated_by` float görünür çünkü CSV’de `.0` ve/veya NaN vardır. Kullanırken `astype('Int64')` (nullable int) dönüştürülebilir.

### 5.2 Cihaz adları (`device`)

Boşluklar anlamlıdır; string’i strip etmeden eşleme yapma. 1.0.3’te görülen adlar:

`CS100    3`, `CS-12`, `AT-6 C 5.5`, `CS-12   E`, `AT-6     6`, `AT-60    3`, `AT-6 C 5.8`, `AT-6 C`, `AT-6 C 5.0`, `AT-6 C 5.3`, `AT-6 C 5.6`

### 5.3 Kalite / gürültü alanları

Bu sütunlar kontrollü kategori değil, **Almanca/lead listesi serbest metindir**. Örnek kalıplar:

- Lead listesi: `V6`, `II,III,AVF`, `I-V1`, `alles` (hepsi)
- Şiddet: `leicht`, `mittel`, `stark`
- Elektrot: `Elektroden vertauscht???`, `Kontaktprobleme aVL ???`

Makine öğrenmesinde genelde:

1. Sütun doluysa o kayıt “gürültülü” diye ikili bayrak, veya
2. Hiç kullanılmaz (çoğu PTB-XL benchmark’ı ham etiketle eğitir).

`electrodes_problems` yalnızca 30 kayıtta dolu; elemek isteyenler bu 30’u çıkarabilir.

---

## 6. Etiketler: `scp_codes`

### 6.1 Saklama biçimi (kritik)

CSV hücresi **JSON değil**, Python dict literal’idir (tek tırnak):

```
{'NORM': 100.0, 'LVOLT': 0.0, 'SR': 0.0}
```

Doğru ayrıştırma:

```python
import ast
df.scp_codes = df.scp_codes.apply(ast.literal_eval)
# sonuç: dict[str, float]
```

`json.loads` **çalışmaz** (tek tırnak).

Kayıt başına 1–9 kod vardır (ortalama ≈2.80). Toplam 71 benzersiz kod; `scp_statements.csv` ile birebir örtüşür.

### 6.2 Likelihood (güven) skoru

Dict değeri 0–100 arası bir **likelihood**’dur. Gözlenen tekil değerler:

`0, 10, 14, 15, 30, 34, 35, 50, 80, 100`

Yorum (orijinal makale):

- Kardiyolog kodun **varlığını** işaretler; sayı o tanının ne kadar olası görüldüğüdür.
- **Ritim ifadelerinin çoğu 0.0** yazar (ör. `SR` 16.782 kez, hepsi 0.0). 0 demek “yok” demek değildir; ritim için “kodlandı ama skor verilmedi” anlamına gelir.
- Form ifadelerinin bir kısmı da hep 0.0’dır (`ABQRS`, `STD_`, `QWAVE`, …).
- Tanı (diagnostic) kodlarında skor genellikle >0’dır.

Yaygın eşik pratikleri:

| Eşik | Boş diagnostic superclass kalan kayıt | Kullanım |
|---|---:|---|
| ≥ 0 (hepsi) | 407 | En yaygın “makaledeki örnek kod” davranışı |
| ≥ 15 | 420 | Çok düşük güveni ele |
| ≥ 50 | 1.424 | “olası” |
| ≥ 80 | 2.746 | “yüksek olasılık” |
| ≥ 100 | 4.578 | Yalnızca kesin |

Resmi `example_physionet.py` **eşik uygulamaz**; dict’te anahtar varsa (skor 0 olsa bile) diagnostic sınıfa map eder. Ritim kodları diagnostic tablosunda olmadığı için superclass’a yansımaz.

### 6.3 Üç etiket ailesi

`scp_statements.csv` her kodu üç bayrakla ayırır (`1.0` veya boş):

| Aile | n kod | Anlam | Superclass’a girer mi? |
|---|---:|---|---|
| `diagnostic == 1` | 44 | Tanısal SCP ifadeleri | Evet |
| `form == 1` | 19 | Morfoloji / form | Hayır (4 kod hem diagnostic hem form) |
| `rhythm == 1` | 12 | Ritim | Hayır |

Hem diagnostic hem form olan 4 kod: `NDT`, `NST_`, `DIG`, `LNGQT`.

Hiçbir aileye düşmeyen kod yoktur.

---

## 7. `scp_statements.csv` şeması

- İlk sütun indeks: SCP kodu (`NORM`, `IMI`, `SR`, …)
- 71 satır

| Sütun | Açıklama |
|---|---|
| `description` | Kısa İngilizce açıklama |
| `diagnostic` | 1 ise tanısal |
| `form` | 1 ise form/morfoloji |
| `rhythm` | 1 ise ritim |
| `diagnostic_class` | 5 süper sınıftan biri (`NORM, MI, STTC, HYP, CD`) |
| `diagnostic_subclass` | 23 alt sınıftan biri |
| `Statement Category` | SCP kategori metni |
| `SCP-ECG Statement Description` | Uzun açıklama |
| `AHA code`, `aECG REFID`, `CDISC Code`, `DICOM Code` | Dış ontoloji eşlemeleri (çoğu boş) |

Superclass üretmek için resmi örnek yalnızca `diagnostic == 1` satırlarını kullanır:

```python
agg_df = pd.read_csv(DATA_ROOT + "scp_statements.csv", index_col=0)
agg_df = agg_df[agg_df.diagnostic == 1]
```

---

## 8. Tanı hiyerarşisi (asıl ML hedefi)

PTB-XL’in standart çok-etiketli (multi-label) görevi **5 diagnostic superclass** üzerinedir. Bir kayıt birden fazla superclass taşıyabilir.

### 8.1 Beş süper sınıf

| Kod | Anlam | Kayıt sayısı (PhysioNet 1.0.3, multi-label) |
|---|---|---:|
| `NORM` | Normal EKG | 9.514 |
| `MI` | Myocardial infarction | 5.469 |
| `STTC` | ST/T değişikliği | 5.235 |
| `CD` | Conduction disturbance | 4.898 |
| `HYP` | Hypertrophy | 2.649 |

Aşağıdaki kombinasyon sayıları `00` notebook / `dataset_stats.json` ile üretilir.

Boş diagnostic kayıtlar (yalnız form/ritim, tanı yok) superclass sınıflandırmasında **dışarıda bırakılır**. Resmi örnek kod bunları boş liste olarak bırakır; `load_metadata` bu satırları düşer.

**Dikkat:** `NORM` başka sınıflarla birlikte gelebilir. “Normal vs patolojik” ikili görevde `NORM`’un yalnız olduğu kayıtlar ile `NORM` içeren tüm kayıtları karıştırma.

### 8.2 Superclass üretme (resmi algoritma)

```python
def aggregate_diagnostic(y_dic, agg_df):
    tmp = []
    for key in y_dic.keys():          # likelihood yok sayılır
        if key in agg_df.index:       # yalnızca diagnostic==1 satırlar
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))             # sırasız, tekrarsız
```

Çıktı örneği: `['NORM']`, `['MI', 'CD']`, `[]`.

Sıralı kanonik vektör (önerilen sınıf sırası, literatürde sık):

```python
SUPERCLASSES = ["NORM", "MI", "STTC", "CD", "HYP"]
# multi-hot: [1,0,0,0,0] gibi
```

Makale metrikleri genelde **macro-averaged AUC** (çok-etiketli) kullanır; tek-etiketli accuracy uygun değildir.

### 8.3 23 diagnostic subclass

| subclass | superclass |
|---|---|
| `NORM` | NORM |
| `IMI` | MI |
| `AMI` | MI |
| `STTC` | STTC |
| `LVH` | HYP |
| `LAFB/LPFB` | CD |
| `ISC_` | STTC |
| `IRBBB` | CD |
| `ISCA` | STTC |
| `_AVB` | CD |
| `IVCD` | CD |
| `NST_` | STTC |
| `CRBBB` | CD |
| `CLBBB` | CD |
| `LAO/LAE` | HYP |
| `ISCI` | STTC |
| `LMI` | MI |
| `RVH` | HYP |
| `RAO/RAE` | HYP |
| `WPW` | CD |
| `ILBBB` | CD |
| `SEHYP` | HYP |
| `PMI` | MI |

Subclass, `diagnostic_class` gibi `scp_statements.csv` üzerinden üretilir (`diagnostic_subclass` sütunu). Daha dengesiz ve daha zor bir görevdir. Kayıt sayıları `00` / `dataset_stats.json`.

### 8.4 44 diagnostic kod → sınıf eşlemesi

**NORM / NORM**

- `NORM` — normal ECG

**MI**

- `AMI` → AMI (anterior MI)
- `ASMI` → AMI (anteroseptal MI)
- `ALMI` → AMI (anterolateral MI)
- `INJAS`, `INJAL`, `INJLA` → AMI (subendocardial injury, ilgili lead grubu)
- `IMI` → IMI (inferior MI)
- `ILMI`, `IPLMI`, `IPMI` → IMI
- `INJIN`, `INJIL` → IMI
- `LMI` → LMI (lateral MI)
- `PMI` → PMI (posterior MI)

**STTC**

- `NDT`, `DIG`, `LNGQT`, `ANEUR`, `EL` → STTC
- `NST_` → NST_
- `ISC_` → ISC_
- `ISCAL`, `ISCAS`, `ISCLA`, `ISCAN` → ISCA
- `ISCIN`, `ISCIL` → ISCI

**HYP**

- `LVH` → LVH
- `RVH` → RVH
- `LAO/LAE` → LAO/LAE
- `RAO/RAE` → RAO/RAE
- `SEHYP` → SEHYP

**CD**

- `LAFB`, `LPFB` → LAFB/LPFB
- `IRBBB` → IRBBB
- `CRBBB` → CRBBB
- `CLBBB` → CLBBB
- `ILBBB` → ILBBB
- `IVCD` → IVCD
- `1AVB`, `2AVB`, `3AVB` → `_AVB`
- `WPW` → WPW

### 8.5 Form kodları (diagnostic superclass’a girmez; 15’i yalnızca form)

`ABQRS, PVC, STD_, VCLVH, QWAVE, LOWT, NT_, PAC, LPR, INVT, LVOLT, HVOLT, TAB_, STE_, PRC(S)`

Bunlar “abnormal QRS”, premature beat, ST depression/elevation, voltaj kriteri gibi morfoloji notlarıdır. Ayrı bir form-sınıflandırma görevinde kullanılır.

### 8.6 Ritim kodları (12)

| Kod | Anlam | n | Not |
|---|---|---:|---|
| `SR` | sinus rhythm | 16782 | likelihood hep 0 |
| `AFIB` | atrial fibrillation | 1514 | çoğunlukla 0, 48 kayıtta 100 |
| `STACH` | sinus tachycardia | 826 | |
| `SARRH` | sinus arrhythmia | 772 | |
| `SBRAD` | sinus bradycardia | 637 | |
| `PACE` | normal functioning pacemaker | 296 | |
| `SVARR` | supraventricular arrhythmia | 157 | |
| `BIGU` | bigeminy | 82 | |
| `AFLT` | atrial flutter | 73 | |
| `SVTAC` | SVT | 27 | |
| `PSVT` | PSVT | 24 | hep 100 |
| `TRIGU` | trigeminy | 20 | |

Ritim sınıflandırması ayrı bir multi-label/multi-class görevdir; 5-class diagnostic benchmark’ın parçası değildir.

---

## 9. Önerilen train / validation / test bölmesi

`strat_fold` 1…10, yaklaşık eşit:

| fold | n | `validated_by_human` |
|---:|---:|---|
| 1 | 2177 | karışık |
| 2 | 2184 | karışık |
| 3 | 2194 | karışık |
| 4 | 2175 | karışık |
| 5 | 2176 | karışık |
| 6 | 2178 | karışık |
| 7 | 2178 | karışık |
| 8 | 2179 | karışık |
| 9 | 2193 | **%100 insan doğrulamalı** |
| 10 | 2203 | **%100 insan doğrulamalı** |

Literatürdeki kanonik protokol (Wagner / Strodthoff):

- **Test:** `strat_fold == 10`
- **Validation:** `strat_fold == 9` (önerilir)
- **Train:** `strat_fold <= 8` (val ayrıysa) veya `strat_fold != 10` (val yoksa)

Resmi `example_physionet.py` fold 10’u test, 1–9’u train yapar (ayrı val yok).

**Zorunlu kurallar:**

1. Kendi rastgele split’ini kullanma; `strat_fold` hasta-düzeyinde izoledir.
2. Fold 9–10’un tamamen kardiyolog doğrulamalı olması bilinçlidir; test kalitesi için bunları train’e katma.
3. Aynı `patient_id` birden fazla fold’a dağılmaz; ekstra hasta-gruplama gerekmez.

---

## 10. Resmi yükleme örneği (`example_physionet.py`)

Davranış özeti:

1. `ptbxl_database.csv` oku, indeks `ecg_id`
2. `scp_codes` ← `ast.literal_eval`
3. `sampling_rate==100` ise `filename_lr`, değilse `filename_hr` üzerinden `wfdb.rdsamp`
4. Sinyalleri `(N, T, 12)` numpy dizisine yığ
5. `scp_statements.csv` içinde `diagnostic==1` süz
6. Her kayda `diagnostic_superclass` listesi yaz
7. `strat_fold == 10` test, kalan train

Eksikleri (kendi kodunda düzelt):

- Tüm veri RAM’de
- Likelihood eşiği yok
- Boş superclass’lar (`[]`) train/test’te kalır
- Val seti yok
- Windows’ta `path+f` için `path`’in ayırıcıyla bitmesi gerekir; `pathlib.Path` daha güvenli
- `wfdb.rdsamp` gövdeye `.hea`/`.dat` eklenmemeli

Önerilen yol birleştirme:

```python
from pathlib import Path
root = Path(DATA_ROOT)
record_path = root / row.filename_lr   # uzantı yok
signal, meta = wfdb.rdsamp(str(record_path))
```

---

## 11. Tipik modelleme sözleşmeleri

Kod yazarken varsayılan görev (aksi söylenmedikçe):

1. Girdi: 12-lead, 10 s, **100 Hz** `(12, 1000)` veya `(1000, 12)` — 100 Hz literatürde yeter ve daha hafif
2. Hedef: 5-class **multi-label** superclass, `SUPERCLASSES = ["NORM","MI","STTC","CD","HYP"]`
3. Superclass: diagnostic kodlar, eşik yok (örnek kod ile aynı) veya ≥50
4. Boş diagnostic kayıtlar (407): **dışarıda bırak**
5. Split: train folds 1–8, val 9, test 10
6. Metrik: macro AUC; ek olarak per-class AUC, macro/micro F1 (eşik 0.5)
7. Sinyal birimi: mV; isteğe bağlı z-score **lead bazında veya kayıt bazında**. Global min-max önerme; amplitüd klinik bilgi taşır
8. Augmentasyon (opsiyonel): zaman kaydırma, Gauss gürültüsü, lead dropout — split’ten sonra yalnızca train’de

İkinci görev seçenekleri (isteğe bağlı, karıştırma):

- 23-class subclass (daha dengesiz)
- 71-class tüm SCP (diagnostic+form+rhythm)
- Yalnızca ritim (`AFIB` vs `SR` vb.)
- Cinsiyet/yaş tahmini (meta sızıntısına dikkat)

---

## 12. Kod tuzakları (checklist)

1. `json.loads(scp_codes)` kullanma → `ast.literal_eval`
2. `sex`: 0 erkek, 1 kadın (tersine çevirme)
3. Lead adı `AVR` ≠ `aVR`
4. `filename_*` uzantısız; `wfdb.rdsamp` tam gövde
5. `path + filename` için `DATA_ROOT` ayırıcıyla bitmeli
6. `patient_id` float gelebilir → `int` / `Int64`
7. Ritim kodunda likelihood 0 = yok değil
8. `df.sub` diye sütun adı kullanma (`DataFrame.sub` ile çakışır)
9. `NORM` tek başına ≠ `NORM` içeren
10. Kendi K-fold’un hasta sızdırır; `strat_fold` kullan
11. 500 Hz’i toptan yükleme bellek patlatır
12. Alman `report` metnini etiket sanma; asıl etiket `scp_codes`
13. `device` string’lerindeki boşlukları strip ederek birleştirme (benzersiz adlar bozulur) — gerekmedikçe dokunma
14. `height==6` gibi fizyolojik imkânsız değerler var; demografiyi özellik yapacaksan aykırı değerleri NaN yap
15. Multi-label’de softmax değil **sigmoid** + `BCEWithLogits`

---

## 13. Bağımlılıklar

```
pandas
numpy
wfdb
```

`example_physionet.py` başka paket istemez. Derin öğrenme için ayrıca `torch` / `tensorflow` vb. proje koduna aittir.

Sinyali WFDB’siz okumak mümkün ama önerilmez: `.dat` little-endian `int16`, shape `(T, 12)` reshape, sonra `/ 1000.0`. Başlıktaki kazanç 1000.0/mV ve baseline 0 varsayımına bağlıdır; PTB-XL 1.0.3 kayıtlarında bu sabittir.

---

## 14. Atıf

Kod/raporda:

> Wagner, P., Strodthoff, N., Bousseljot, R., Samek, W., & Schaeffter, T. (2022). PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. https://doi.org/10.13026/kfzx-aw45

> Wagner, P. et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data 7, 154 (2020).

---

## 15. Bu belgeden kod üretirken yeterli olan özet

- Kayıt tablosu: `DATA_ROOT/ptbxl_database.csv`, indeks `ecg_id`, **21799** satır (sürüm 1.0.3)
- Kod sözlüğü: `DATA_ROOT/scp_statements.csv`, indeks SCP kodu
- Sinyal: `wfdb.rdsamp(DATA_ROOT / filename_lr)` → `(1000, 12)` mV, 100 Hz
- Etiket: `ast.literal_eval(scp_codes)` → diagnostic map → 5-d multi-hot
- Split sütunu: `strat_fold`
- Sabitler: 12 lead, 10 s, 100/500 Hz, CC BY 4.0
