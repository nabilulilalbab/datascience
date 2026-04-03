# Panduan Menjalankan Proyek Prediksi Churn Pelanggan

Proyek ini bertujuan untuk memprediksi probabilitas pelanggan berhenti berlangganan menggunakan metode statistika deskriptif dan algoritma pemelajaran mesin Random Forest.

## Struktur Folder
- `generate_data.py`: Skrip untuk membuat dataset sintetik `telecom_churn.csv`.
- `churn_prediction.py`: Skrip utama untuk analisis data, visualisasi, dan pemodelan.
- `REPORT.md`: Laporan mendalam mengenai metodologi, teori, dan hasil evaluasi.
- `requirements.txt`: Daftar pustaka (library) yang dibutuhkan.
- `output_visual/`: Folder berisi grafik hasil analisis.

## Cara Menjalankan

### 1. Persiapan Lingkungan
Pastikan Python 3.11 sudah terpasang. Gunakan lingkungan virtual yang sudah ada atau buat baru:
```bash
# Jika membuat baru
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Membuat Dataset
Jalankan skrip berikut untuk menghasilkan data:
```bash
./venv/bin/python generate_data.py
```

### 3. Menjalankan Analisis dan Pemodelan
Jalankan skrip utama untuk melihat hasil statistik dan melatih model:
```bash
./venv/bin/python churn_prediction.py
```

## Hasil Analisis
Setelah menjalankan skrip utama, periksa folder `output_visual/` untuk melihat:
- `histogram_numerik.png`: Distribusi variabel seperti Usia dan Tagihan.
- `distribusi_churn.png`: Keseimbangan kelas target.
- `korelasi_heatmap.png`: Hubungan antar variabel.

Detail metrik evaluasi model (Akurasi, AUC, dll.) akan muncul pada terminal saat eksekusi selesai.
