# Referensi Dataset untuk Research Customer Churn Prediction

## Dataset Asli dari Kaggle

Untuk pengembangan lebih lanjut atau validasi dengan data riil, berikut adalah dataset churn telekomunikasi yang relevan dari Kaggle:

---

## 1. **Telco Customer Churn (IBM Sample Dataset)**  REKOMENDASI UTAMA

**Link:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**Spesifikasi:**
- **Jumlah Record:** 7,043 customers
- **Jumlah Fitur:** 21 features
- **Target Variable:** Churn (Yes/No)
- **Popularitas:** 600,000+ downloads
- **Format:** CSV

**Fitur-fitur:**
- CustomerID
- Gender (Male/Female)
- SeniorCitizen (0/1)
- Partner, Dependents
- Tenure (months)
- PhoneService, MultipleLines
- InternetService (DSL/Fiber optic/No)
- OnlineSecurity, OnlineBackup, DeviceProtection
- TechSupport, StreamingTV, StreamingMovies
- Contract (Month-to-month/One year/Two year)
- PaperlessBilling
- PaymentMethod
- MonthlyCharges, TotalCharges
- **Churn** (Target)

**Kelebihan:**
-  Dataset paling populer untuk churn prediction
-  Banyak digunakan dalam paper dan jurnal ilmiah
-  Struktur mirip dengan dataset sintetik proyek ini
-  Clean dan well-documented
-  Ribuan kernel/notebook untuk referensi
-  Cocok dengan metodologi Random Forest yang digunakan

**Relevansi dengan Proyek:**
Dataset ini memiliki kesamaan struktur dengan `telecom_churn.csv` yang digunakan dalam proyek, dengan fitur seperti:
- Demographics (Gender, Age/SeniorCitizen)
- Billing information (MonthlyCharges ~ Monthly_Bill)
- Service usage patterns (Tenure, Services ~ Total_Usage_Minutes)
- Customer service interaction (~ Customer_Service_Calls)

---

## 2. **Customer Churn Prediction 2020 (Maven Analytics)**

**Link:** https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics

**Spesifikasi:**
- **Jumlah Record:** 7,043 customers
- **Jumlah Fitur:** Similar dengan IBM dataset
- **Kualitas:** Clean, no missing values

**Kelebihan:**
-  Version yang lebih bersih dari IBM dataset
-  Documentation yang sangat baik
-  Banyak visualization examples

---

## 3. **Telco Churn Dataset (Extended Version)**

**Link:** https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset

**Spesifikasi:**
- **Jumlah Record:** 7,043 rows
- **Jumlah Fitur:** 33 columns (extended)
- **Format:** CSV

**Kelebihan:**
-  Extended version dengan lebih banyak fitur
-  Cocok untuk feature engineering advanced

---

## 4. **Orange Telecom's Churn Dataset**

**Link:** https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets

**Spesifikasi:**
- **Jumlah Record:** 3,333 customers
- **Source:** Real-world data dari operator telekomunikasi Prancis
- **Kompleksitas:** Medium to High

**Kelebihan:**
-  Real-world data (bukan sample/synthetic)
-  Mencakup data temporal
-  Lebih challenging untuk modeling

---

## Perbandingan dengan Dataset Proyek

| Aspek | Dataset Proyek (Synthetic) | Kaggle IBM Dataset |
|-------|----------------------------|---------------------|
| Jumlah Record | 1,000 | 7,043 |
| Jumlah Fitur | 9 | 21 |
| Source | Generated/Synthetic | IBM Sample |
| Kompleksitas | Medium | Medium-High |
| Missing Values | None | Minimal |
| Kelebihan | Controlled, Educational | Real-world patterns |

---

## Cara Menggunakan Dataset Kaggle

### 1. Download Dataset
```bash
# Install Kaggle API
pip install kaggle

# Setup Kaggle credentials
# Download kaggle.json dari https://www.kaggle.com/settings
# Simpan di ~/.kaggle/kaggle.json

# Download dataset
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip
```

### 2. Adaptasi Kode
Dataset Kaggle dapat langsung digunakan dengan modifikasi minimal pada `churn_prediction.py`:

```python
# Load Kaggle dataset
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Feature engineering untuk menyesuaikan dengan model
# Mapping fitur Kaggle ke struktur proyek
```

---

## Rekomendasi Penggunaan

### Untuk Pembelajaran:
- Gunakan **dataset proyek (synthetic)** - lebih sederhana dan terkontrol

### Untuk Validasi Model:
- Gunakan **IBM Telco Dataset** - validasi performa model pada data real

### Untuk Research Advanced:
- Gunakan **Orange Telecom Dataset** - real-world complexity

### Untuk Publikasi Paper:
- Gunakan **IBM Telco Dataset** - paling banyak dirujuk dalam literatur

---

## Referensi Jurnal yang Menggunakan Dataset Ini

1. **Ahmad, A. K., et al. (2019)** menggunakan dataset telekomunikasi serupa untuk analisis churn dengan machine learning
2. **Imani, M., et al. (2025)** dalam systematic review mereka menganalisis berbagai dataset churn termasuk IBM Telco
3. Ratusan paper di IEEE, ACM, dan Springer menggunakan IBM Telco dataset sebagai benchmark

---

## Update Dataset Proyek (Opsional)

Jika ingin mengupdate proyek dengan dataset Kaggle:

1. Download dataset dari link di atas
2. Modifikasi `generate_data.py` untuk load data Kaggle
3. Sesuaikan preprocessing di `churn_prediction.py`
4. Update dokumentasi di `REPORT.md` dan `README.md`
5. Re-run analysis dan update laporan

---

## Kesimpulan

Dataset **Telco Customer Churn (IBM)** dari Kaggle adalah pilihan terbaik untuk:
- Validasi model yang sudah dibuat
- Pembelajaran lebih lanjut
- Publikasi atau presentasi research
- Komparasi dengan hasil proyek synthetic

Link utama: **https://www.kaggle.com/datasets/blastchar/telco-customer-churn**

---

*Dokumen ini dibuat untuk melengkapi research Customer Churn Prediction*  
*Tanggal: 5 April 2026*
