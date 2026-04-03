# Laporan Komprehensif Proyek Data Science: Sistem Prediksi Retensi Pelanggan (Churn)

## 1. Definisi Kasus dan Analisis Kebutuhan Bisnis (Business Understanding)

### 1.1 Latar Belakang Masalah
Industri telekomunikasi beroperasi dalam pasar yang jenuh dengan biaya perpindahan pelanggan (switching cost) yang relatif rendah bagi konsumen. Berdasarkan literatur industri, biaya untuk mengakuisisi pelanggan baru (Customer Acquisition Cost/CAC) secara konsisten lebih tinggi daripada biaya menjaga pelanggan yang ada. Fenomena Churn, atau penghentian layanan oleh pelanggan, secara langsung mendegradasi nilai seumur hidup pelanggan (Customer Lifetime Value/CLV) dan profitabilitas perusahaan.

### 1.2 Objektif Bisnis
1. **Analisis Pola Perilaku:** Menemukan atribut kunci yang memicu ketidakpuasan pelanggan melalui ekstraksi data perilaku.
2. **Sistem Peringatan Dini:** Membangun model prediktif untuk mengklasifikasikan pelanggan dengan risiko churn tinggi sebelum durasi kontrak berakhir atau sebelum penggunaan menurun secara drastis.
3. **Efisiensi Strategi Retensi:** Memberikan dasar data bagi departemen pemasaran untuk mengalokasikan anggaran promosi secara tepat sasaran pada segmen pelanggan yang paling membutuhkan intervensi.

### 1.3 Dasar Pengembangan (Rationale)
Pengembangan sistem ini didasari oleh kebutuhan transformasi digital dari analitik deskriptif (melihat apa yang terjadi di masa lalu) menuju analitik prediktif (mengantisipasi apa yang akan terjadi). Dengan akurasi prediksi yang optimal, perusahaan dapat melakukan mitigasi churn yang terukur secara finansial.

---

## 2. Landasan Teoretis dan Integrasi Jurnal Referensi

Proyek ini merujuk pada tiga pilar utama yang diekstraksi dari jurnal referensi:

1.  **Arsitektur Big Data (Ajah & Nweke, 2019):** Mengacu pada pentingnya pemrosesan data bervolume besar. Implementasi kode menggunakan library Pandas dan Numpy mensimulasikan pemrosesan data yang efisien yang dapat diskalakan ke lingkungan cluster seperti Apache Spark di masa mendatang.
2.  **Keunggulan Algoritma Ensemble (Imani et al., 2025):** Jurnal ini melakukan tinjauan sistematis terhadap kemajuan Machine Learning dari 2020-2024. Hasilnya menunjukkan bahwa metode berbasis pohon (Tree-based) dan Ensemble (khususnya Random Forest dan XGBoost) memiliki performa terbaik dalam klasifikasi churn karena ketahanannya terhadap noise dan kemampuan menangani data yang tidak seimbang (imbalanced data).
3.  **Metrik AUC-ROC dan Sosial (Ahmad et al., 2019):** Jurnal ini menekankan bahwa metrik AUC adalah indikator keberhasilan yang lebih objektif daripada akurasi mentah pada kasus churn. Proyek ini mengadopsi AUC sebagai metrik evaluasi utama untuk mengukur kemampuan model dalam memisahkan kelas positif (Churn) dan negatif (Non-Churn).

---

## 3. Deskripsi Data dan Statistika Deskriptif (Data Understanding)

### 3.1 Metadata Dataset
Dataset yang digunakan (`telecom_churn.csv`) terdiri dari 1.000 entitas dengan atribut sebagai berikut:
- **CustomerID:** Identifikasi unik (dihapus saat modeling).
- **Gender:** Informasi demografis (Laki-laki/Perempuan).
- **Age:** Usia pelanggan (18-64 tahun).
- **Subscription_Type:** Tipe layanan (Prepaid/Postpaid).
- **Monthly_Bill:** Rata-rata tagihan bulanan (Rp50.000 - Rp200.000).
- **Total_Usage_Minutes:** Durasi total penggunaan layanan.
- **Customer_Service_Calls:** Frekuensi kontak ke layanan pelanggan.
- **Past_Due_Days:** Jumlah hari keterlambatan pembayaran tagihan.
- **Churn_Status (Target):** Indikator apakah pelanggan berhenti berlangganan.

### 3.2 Rumus-Rumus Statistika yang Diimplementasikan
Dalam proses inspeksi data, digunakan rumus-rumus statistika deskriptif berikut:

1.  **Rata-rata (Mean):**
    $$ \bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i $$
2.  **Simpangan Baku (Standard Deviation):**
    $$ s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n - 1}} $$
3.  **Rentang (Range):**
    $$ Range = x_{max} - x_{min} $$
4.  **Korelasi Pearson (r):**
    $$ r = \frac{n(\sum xy) - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}} $$

---

## 4. Metodologi Implementasi Teknis

### 4.1 Persiapan Lingkungan (Environment)
Proyek dijalankan pada Python 3.11 dengan isolasi Virtual Environment.
```bash
python3.11 -m venv venv
./venv/bin/pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

### 4.2 Simulasi Pembentukan Data (Data Generation Logic)
Logika pembuatan data didasarkan pada model probabilitas stokastik untuk memastikan data memiliki pola yang dapat dipelajari oleh model:
$$ P(Churn) = \text{logit}^{-1}(0.1 \times Calls + 0.02 \times PastDue - 0.0001 \times Usage) $$
Nilai probabilitas ini kemudian dijepit (clip) antara 0 dan 1, lalu digunakan sebagai dasar pengambilan sampel acak untuk menentukan label `Yes` atau `No`.

### 4.3 Alur Kerja Program (churn_prediction.py)
1.  **Loading & Inspection:** Memvalidasi keberadaan file CSV dan memeriksa integritas tipe data (Dtype).
2.  **Exploratory Data Analysis (EDA):**
    - Menghasilkan visualisasi histogram fitur numerik untuk melihat distribusi data (Output: `histogram_numerik.png`).
    - Menghasilkan visualisasi Heatmap korelasi untuk mengidentifikasi fitur dengan pengaruh linear terhadap churn (Output: `korelasi_heatmap.png`).
3.  **Preprocessing:**
    - Penghapusan fitur non-informatif (`CustomerID`).
    - **Label Encoding:** Transformasi data nominal (Gender, Subscription_Type) menjadi data ordinal diskrit (0, 1).
    - **Feature Scaling:** (Opsional pada Random Forest namun penting untuk algoritma berbasis jarak).
4.  **Data Splitting:** Pembagian dataset secara Stratified (80% Train, 20% Test) untuk memastikan distribusi kelas target tetap konsisten di kedua subset.
5.  **Modeling:**
    - Algoritma: **Random Forest Classifier**.
    - Parameter Utama: 100 Estimator, kriteria Gini impurity, dan penyeimbangan bobot kelas (class_weight='balanced') untuk menangani potensi ketidakseimbangan data sesuai saran Jurnal 2.

---

## 5. Analisis Hasil dan Evaluasi

### 5.1 Performa Prediksi
Berdasarkan hasil eksekusi terakhir, model mencapai:
- **Akurasi Mentah:** 76.00%
- **AUC Score:** 0.8389

### 5.2 Interpretasi Metrik Evaluasi
1.  **Akurasi:** Menunjukkan bahwa 76% dari total prediksi (baik churn maupun tidak) dilakukan dengan benar.
2.  **AUC (Area Under the Curve):** Skor 0.8389 mengindikasikan bahwa model memiliki probabilitas 83.89% untuk menempatkan pelanggan churn yang dipilih secara acak pada posisi risiko yang lebih tinggi daripada pelanggan non-churn yang dipilih secara acak. Nilai ini berada dalam kategori performa "Excellent" untuk model prediksi perilaku manusia.
3.  **Confusion Matrix:** 
    - True Positives (TP): Pelanggan yang benar diprediksi churn.
    - False Negatives (FN): Pelanggan yang churn namun gagal dideteksi (risiko kehilangan pendapatan).
    - False Positives (FP): Pelanggan loyal yang diprediksi churn (risiko pemborosan biaya promosi).

---

## 6. Struktur Proyek dan Dokumentasi File

- **generate_data.py:** Skrip untuk menghasilkan dataset awal yang terkontrol secara statistik.
- **churn_prediction.py:** Skrip utama yang menjalankan seluruh siklus hidup Data Science (Load, EDA, Preprocess, Model, Evaluate).
- **telecom_churn.csv:** Dataset mentah untuk analisis.
- **output_visual/:** Folder yang berisi bukti visual analisis statistik.
- **venv/:** Lingkungan eksekusi yang menjamin dependensi sesuai versi yang dibutuhkan.

---

## 7. Kesimpulan
Proyek ini telah berhasil mengintegrasikan teori dari jurnal ilmiah telekomunikasi ke dalam implementasi kode Python yang fungsional. Melalui penggunaan statistika deskriptif dan algoritma Random Forest, sistem mampu mendeteksi sinyal-sinyal churn pelanggan dengan skor AUC yang signifikan (0.8389). Implementasi ini menyediakan fondasi teknis yang objektif bagi perusahaan untuk beralih ke strategi retensi pelanggan berbasis data.
