# Analisis Penerapan Metode Data Science: Prediksi Customer Churn pada Industri Telekomunikasi

---

## DAFTAR JURNAL REFERENSI YANG TELAH DIVALIDASI

| No | Jurnal | Penulis | Tahun | Publisher | Link Akses |
|----|--------|---------|-------|-----------|------------|
| 1 | **Customer churn prediction in telecom using machine learning in big data platform** | Ahmad, A. K., Jafar, A., & Aljoumaa, K. | 2019 | Journal of Big Data (Springer) | https://doi.org/10.1186/s40537-019-0191-6 |
| 2 | **Big data and business analytics: Trends, platforms, success factors and applications** | Ajah, I. A., & Nweke, H. F. | 2019 | Big Data and Cognitive Computing (MDPI) | https://doi.org/10.3390/bdcc3020032 |
| 3 | **Customer churn prediction: A systematic review of recent advances, trends, and challenges in machine learning and deep learning** | Imani, M., Joudaki, M., & Beikmohammadi, A. | 2025 | Machine Learning and Knowledge Extraction (MDPI) | https://doi.org/10.3390/make7030105 |

---

## 1. BUSINESS UNDERSTANDING

### 1.1 Latar Belakang Masalah

Industri telekomunikasi merupakan salah satu sektor utama di negara-negara berkembang. Kemajuan teknologi dan meningkatnya jumlah operator telah meningkatkan tingkat persaingan di pasar (Ahmad et al., 2019). Perusahaan telekomunikasi menghadapi tantangan besar dalam mempertahankan pelanggan (*customer retention*) karena biaya untuk mendapatkan pelanggan baru jauh lebih tinggi dibandingkan dengan mempertahankan pelanggan yang sudah ada.

Menurut penelitian Ahmad et al. (2019) yang diterbitkan dalam *Journal of Big Data* (Springer), biaya akuisisi pelanggan baru dapat mencapai **enam kali lebih tinggi** daripada biaya retensi pelanggan. Hal ini menjadikan prediksi churn sebagai investasi strategis yang menguntungkan.

*Customer churn* (perpindahan pelanggan dari satu provider ke provider lain) menjadi masalah kritis yang berdampak langsung pada pendapatan perusahaan. Menurut Ajah dan Nweke (2019), penggunaan *business analytics* dan *big data* dapat membantu perusahaan dalam mengidentifikasi pola perilaku pelanggan dan mengambil tindakan preventif untuk mengurangi tingkat churn.

### 1.2 Tujuan Bisnis

Berdasarkan penelitian Ahmad et al. (2019), tujuan bisnis yang ingin dicapai adalah:

1. **Mengembangkan model prediksi churn** yang dapat mengidentifikasi pelanggan yang berpotensi melakukan churn dengan akurasi tinggi (target AUC ≥ 90%)
2. **Mengurangi tingkat churn** melalui intervensi proaktif terhadap pelanggan berisiko tinggi
3. **Meningkatkan retensi pelanggan** sebagai strategi paling menguntungkan untuk menghasilkan revenue
4. **Mengoptimalkan alokasi sumber daya** pemasaran dengan fokus pada pelanggan yang benar-benar berisiko churn

### 1.3 Manfaat yang Diharapkan

1. **Efisiensi Biaya**: Mengurangi biaya akuisisi pelanggan baru dengan fokus pada retensi
2. **Peningkatan Revenue**: Mempertahankan pelanggan bernilai tinggi yang berpotensi churn
3. **Pengambilan Keputusan Berbasis Data**: Dashboard prediksi untuk tim pemasaran dan layanan pelanggan
4. **Personalisasi Layanan**: Menyediakan penawaran khusus untuk pelanggan berisiko berdasarkan profil mereka
5. **Kompetitif Advantage**: Memiliki sistem prediksi churn yang lebih baik dari pesaing

---

## 2. DATA UNDERSTANDING

### 2.1 Jenis dan Sumber Data

Berdasarkan studi kasus SyriaTel (Ahmad et al., 2019), data yang digunakan meliputi:

| No | Jenis Data | Sumber | Volume | Format |
|----|-----------|--------|--------|--------|
| 1 | Data Demografi Pelanggan | CRM System | Terabyte | Structured |
| 2 | Data Billing dan Transaksi | Billing System | Terabyte | Structured |
| 3 | Data Call Detail Records (CDR) | Network Systems | Petabyte | Semi-structured |
| 4 | Data SMS dan Internet Usage | Network Systems | Petabyte | Semi-structured |
| 5 | Data Komplain Pelanggan | Customer Service | Gigabyte | Unstructured |
| 6 | Social Network Data | Network Analysis | Big Scale Graph | Graph Data |

**Total Dataset**: ~70 Terabyte pada HDFS (Hadoop Distributed File System)
**Periode Data**: Informasi pelanggan selama 9 bulan sebelum baseline

### 2.2 Deskripsi Variabel (Fitur)

#### 2.2.1 Variabel Demografi dan Akun
| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| customer_id | String | Identifikasi unik pelanggan |
| account_length | Integer | Lama berlangganan (bulan) |
| gender | Categorical | Jenis kelamin pelanggan |
| age | Integer | Usia pelanggan |
| location | Categorical | Wilayah geografis |

#### 2.2.2 Variabel Usage dan Billing
| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| total_calls | Float | Total panggilan per bulan |
| total_minutes | Float | Total menit penggunaan |
| total_charge | Float | Total biaya tagihan |
| number_customer_service_calls | Integer | Jumlah panggilan ke layanan pelanggan |
| international_plan | Boolean | Berlangganan paket internasional |
| voice_mail_plan | Boolean | Berlangganan voice mail |

#### 2.2.3 Variabel Social Network Analysis (SNA)
| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| degree_centrality | Float | Ukuran konektivitas dalam jaringan |
| betweenness_centrality | Float | Seberapa sering pelanggan menjadi jembatan komunikasi |
| similarity_value | Float | Tingkat kesamaan pola penggunaan dengan pelanggan lain |
| network_connectivity | Float | Tingkat keterhubungan dalam jaringan sosial |

#### 2.2.4 Variabel Target
| Variabel | Tipe | Deskripsi |
|----------|------|-----------|
| churn | Boolean | Yes/No - apakah pelanggan melakukan churn |

### 2.3 Struktur Data

#### Representasi Matematis Data

Data dalam kasus ini dapat direpresentasikan dalam berbagai struktur matematis:

**1. Skalar (0-D Tensor)**
- Nilai tunggal seperti rata-rata tagihan, total churn rate
- Contoh: `avg_churn_rate = 0.15` (15% pelanggan churn)

**2. Vektor (1-D Tensor)**
- Deretan nilai untuk satu fitur dari semua pelanggan
- Contoh: `charges = [29.5, 45.2, 12.8, 67.3, ...]` (tagihan tiap pelanggan)

**3. Matriks (2-D Tensor)**
- Dataset seluruhnya: baris = pelanggan, kolom = fitur
- Dimensi: `(n_customers, n_features)` = `(5000, 21)`

$$X = \begin{bmatrix} 
x_{11} & x_{12} & \cdots & x_{1m} \\
x_{21} & x_{22} & \cdots & x_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
x_{n1} & x_{n2} & \cdots & x_{nm}
\end{bmatrix}$$

Dimana:
- $n$ = jumlah sampel (pelanggan)
- $m$ = jumlah fitur
- $x_{ij}$ = nilai fitur $j$ untuk pelanggan $i$

---

## 3. KAITAN DENGAN KONSEP STATISTIKA DAN PYTHON

### 3.1 Konsep Statistik Deskriptif

Menurut Ajah dan Nweke (2019), analisis deskriptif merupakan komponen fundamental dalam *business analytics* yang berfokus pada merangkum dan menggambarkan karakteristik dari sekumpulan data. Dalam konteks churn prediction, kita menggunakan:

#### 3.1.1 Measures of Central Tendency (Ukuran Pemusatan)
| Metode | Formula | Kegunaan |
|--------|---------|----------|
| Mean | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$ | Rata-rata tagihan, rata-rata durasi panggilan |
| Median | Nilai tengah setelah diurutkan | Mengurangi efek outlier pada data tagihan |
| Mode | Nilai yang paling sering muncul | Frekuensi paket yang paling populer |

#### 3.1.2 Measures of Dispersion/Spread (Ukuran Penyebaran)
| Metode | Formula | Kegunaan |
|--------|---------|----------|
| Range | $Range = x_{max} - x_{min}$ | Selisih tagihan tertinggi dan terendah |
| Variance | $\sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$ | Variasi penggunaan layanan |
| Standard Deviation | $\sigma = \sqrt{\sigma^2}$ | Deviasi standar durasi panggilan |
| Interquartile Range (IQR) | $IQR = Q_3 - Q_1$ | Mengidentifikasi outlier dalam data |

#### 3.1.3 Measures of Asymmetry (Ukuran Asimetri)
| Metode | Formula | Interpretasi |
|--------|---------|--------------|
| Skewness | $\gamma_1 = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{x_i - \bar{x}}{\sigma}\right)^3$ | Distribusi tagihan miring ke kanan/kiri |
| Kurtosis | $\gamma_2 = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{x_i - \bar{x}}{\sigma}\right)^4 - 3$ | Tingkat "tajam" distribusi data |

### 3.2 Implementasi dengan NumPy

NumPy (Numerical Python) adalah library fundamental untuk komputasi numerik di Python. Library ini menyediakan struktur data array multidimensi yang efisien (Ajah & Nweke, 2019).

#### 3.2.1 Skalar, Vektor, dan Matriks dalam NumPy

```python
import numpy as np

# SKALAR (0-D Array)
churn_rate = np.array(0.15)  # Tingkat churn 15%
print(f"Scalar - Churn Rate: {churn_rate}, Shape: {churn_rate.shape}")
# Output: Scalar - Churn Rate: 0.15, Shape: ()

# VEKTOR (1-D Array)
customer_ages = np.array([25, 34, 45, 28, 52, 41, 33, 29, 48, 36])
print(f"Vector - Customer Ages Shape: {customer_ages.shape}")
# Output: Vector - Customer Ages Shape: (10,)

# MATRIKS (2-D Array)
# 5 pelanggan x 4 fitur (age, total_minutes, total_calls, total_charge)
customer_data = np.array([
    [25, 300.5, 120, 45.50],
    [34, 180.2, 80, 28.90],
    [45, 450.8, 200, 75.20],
    [28, 150.0, 60, 22.50],
    [52, 320.7, 150, 52.80]
])
print(f"Matrix - Customer Data Shape: {customer_data.shape}")
# Output: Matrix - Customer Data Shape: (5, 4)
```

#### 3.2.2 Shape dan Reshaping dalam NumPy

```python
# Mengecek dimensi array
print(f"Dimensi: {customer_data.ndim}")  # Output: 2
print(f"Shape: {customer_data.shape}")   # Output: (5, 4)
print(f"Size: {customer_data.size}")     # Output: 20
print(f"Data Type: {customer_data.dtype}")  # Output: float64

# Reshaping - mengubah struktur array tanpa mengubah data
customer_data_reshaped = customer_data.reshape(2, 10)
print(f"Reshaped: {customer_data_reshaped.shape}")  # Output: (2, 10)

# Flatten - mengubah ke 1-D
flattened = customer_data.flatten()
print(f"Flattened shape: {flattened.shape}")  # Output: (20,)

# Transpose - menukar baris dan kolom
transposed = customer_data.T
print(f"Transposed shape: {transposed.shape}")  # Output: (4, 5)
```

#### 3.2.3 Filtering dalam NumPy

```python
# Membuat mask untuk pelanggan dengan tagihan tinggi (> 50)
high_charge_mask = customer_data[:, 3] > 50  # Kolom 3 = total_charge
high_charge_customers = customer_data[high_charge_mask]
print("Pelanggan dengan tagihan tinggi:")
print(high_charge_customers)

# Multiple conditions: Pelanggan muda (< 35) dengan durasi tinggi (> 200 menit)
young_high_usage = customer_data[
    (customer_data[:, 0] < 35) &  # age < 35
    (customer_data[:, 1] > 200)   # minutes > 200
]
print("Pelanggan muda dengan penggunaan tinggi:")
print(young_high_usage)

# np.where - mengganti nilai berdasarkan kondisi
# Kategorisasi: "High" jika > 300 menit, "Low" jika <= 300
usage_category = np.where(customer_data[:, 1] > 300, "High", "Low")
print("Kategori penggunaan:", usage_category)
```

#### 3.2.4 Random pada NumPy

```python
# np.random untuk sampling dan simulasi
np.random.seed(42)  # Untuk reproducibility

# Generate random sample data pelanggan
random_ages = np.random.randint(18, 70, size=100)  # 100 pelanggan, usia 18-70
random_charges = np.random.normal(50, 15, size=100)  # Mean=50, Std=15

# Sampling - memilih subset random dari data
sample_indices = np.random.choice(customer_data.shape[0], size=3, replace=False)
sample_customers = customer_data[sample_indices]
print("Random sample 3 pelanggan:", sample_customers)

# Train-test split simulation
n_samples = customer_data.shape[0]
indices = np.random.permutation(n_samples)
train_size = int(0.8 * n_samples)
train_idx, test_idx = indices[:train_size], indices[train_size:]
train_data, test_data = customer_data[train_idx], customer_data[test_idx]
```

#### 3.2.5 Statistical Operations dengan NumPy

```python
# Measures of Central Tendency
mean_charge = np.mean(customer_data[:, 3])      # Rata-rata tagihan
median_charge = np.median(customer_data[:, 3])  # Median tagihan

# Measures of Spread/Variance
std_charge = np.std(customer_data[:, 3])        # Standar deviasi
var_charge = np.var(customer_data[:, 3])        # Variansi
range_charge = np.ptp(customer_data[:, 3])      # Range (peak-to-peak)

# Percentiles
q1 = np.percentile(customer_data[:, 3], 25)     # First quartile
q3 = np.percentile(customer_data[:, 3], 75)     # Third quartile
iqr = q3 - q1                                    # Interquartile range

# Correlation
correlation = np.corrcoef(customer_data[:, 1], customer_data[:, 3])
print(f"Korelasi menit vs tagihan: {correlation[0,1]:.4f}")

# Summary Statistics
print("Ringkasan Statistik:")
print(f"Mean: {mean_charge:.2f}")
print(f"Std Dev: {std_charge:.2f}")
print(f"Min: {np.min(customer_data[:, 3]):.2f}")
print(f"Max: {np.max(customer_data[:, 3]):.2f}")
```

### 3.3 Implementasi dengan Pandas

Pandas adalah library untuk manipulasi dan analisis data yang powerful. Library ini menyediakan struktur data DataFrame yang memudahkan pengolahan data tabel (Ajah & Nweke, 2019).

#### 3.3.1 Tipe Data (dtype) dalam Pandas

```python
import pandas as pd

# Membuat DataFrame
df = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'age': [25, 34, 45, 28, 52],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'total_minutes': [300.5, 180.2, 450.8, 150.0, 320.7],
    'total_calls': [120, 80, 200, 60, 150],
    'total_charge': [45.50, 28.90, 75.20, 22.50, 52.80],
    'international_plan': [False, True, False, False, True],
    'churn': [False, True, False, True, False]
})

# Cek tipe data
print(df.dtypes)
```

Output:
```
customer_id            object
age                     int64
gender                 object
total_minutes         float64
total_calls             int64
total_charge          float64
international_plan       bool
churn                    bool
dtype: object
```

```python
# Konversi tipe data
df['gender'] = df['gender'].astype('category')  # Efisiensi memori
df['churn'] = df['churn'].astype('int')         # 0/1 untuk modeling

# Optimalisasi memori untuk data besar
df['age'] = df['age'].astype('int8')            # -128 to 127 (cukup untuk umur)
df['total_calls'] = df['total_calls'].astype('int16')

print(df.dtypes)
```

#### 3.3.2 Data Manipulation dalam Pandas

```python
# ============================================================
# A. DATA SELECTION
# ============================================================

# 1. Memilih Kolom (seperti vektor)
charges = df['total_charge']           # Single column (Series)
age_charges = df[['age', 'total_charge']]  # Multiple columns (DataFrame)

# 2. Memilih Baris (filtering)
# Pelanggan yang churn
churned = df[df['churn'] == True]

# Pelanggan dengan tagihan tinggi (> 40)
high_spenders = df[df['total_charge'] > 40]

# Multiple conditions
# Pelanggan wanita yang tidak churn dan punya international plan
target_customers = df[
    (df['gender'] == 'F') & 
    (df['churn'] == False) & 
    (df['international_plan'] == True)
]

# Using query (lebih readable)
target = df.query("age > 30 and total_charge > 40 and churn == False")

# iloc vs loc
# iloc: index-based (posisi)
first_3_rows = df.iloc[:3]             # Baris 0-2
first_3_cols = df.iloc[:, :3]          # Kolom 0-2

# loc: label-based (nama)
specific_customers = df.loc[df['customer_id'].isin(['C001', 'C003'])]

# ============================================================
# B. DATA TRANSFORMATION
# ============================================================

# Membuat kolom baru
df['charge_per_minute'] = df['total_charge'] / df['total_minutes']
df['is_senior'] = df['age'] >= 50

# apply() - transformasi custom
def categorize_usage(minutes):
    if minutes < 200:
        return 'Low'
    elif minutes < 350:
        return 'Medium'
    else:
        return 'High'

df['usage_category'] = df['total_minutes'].apply(categorize_usage)

# Binning dengan cut
df['age_group'] = pd.cut(df['age'], 
                          bins=[0, 30, 45, 60, 100], 
                          labels=['Young', 'Adult', 'Middle', 'Senior'])

# ============================================================
# C. AGGREGATION & GROUPBY
# ============================================================

# Groupby - mengelompokkan data
# Rata-rata tagihan per gender
gender_stats = df.groupby('gender')['total_charge'].mean()

# Multiple aggregations
churn_analysis = df.groupby('churn').agg({
    'total_charge': ['mean', 'std', 'min', 'max'],
    'total_minutes': 'mean',
    'age': 'median'
})

# Cross-tabulation
pd.crosstab(df['gender'], df['churn'], margins=True)

# Pivot table
pivot = df.pivot_table(
    values='total_charge', 
    index='gender', 
    columns='churn', 
    aggfunc=['mean', 'count']
)

# ============================================================
# D. HANDLING MISSING DATA
# ============================================================

# Cek missing values
print(df.isnull().sum())

# Handle missing values
df['total_charge'].fillna(df['total_charge'].mean(), inplace=True)  # Imputasi mean
df.dropna(subset=['customer_id'], inplace=True)  # Hapus jika ID kosong

# ============================================================
# E. MERGING & JOINING
# ============================================================

# Misal ada data tambahan
sna_features = pd.DataFrame({
    'customer_id': ['C001', 'C002', 'C003', 'C004', 'C005'],
    'degree_centrality': [0.85, 0.42, 0.73, 0.31, 0.92],
    'network_connectivity': [0.76, 0.55, 0.68, 0.44, 0.89]
})

# Merge (SQL-style join)
full_data = pd.merge(df, sna_features, on='customer_id', how='left')

# Concat (menambah baris/kolom)
new_customers = pd.DataFrame({...})
all_customers = pd.concat([df, new_customers], ignore_index=True)
```

#### 3.3.3 Statistical Analysis dengan Pandas

```python
# Deskriptif Statistik Lengkap
desc_stats = df.describe()
print(desc_stats)

# Statistik khusus
print(f"Skewness tagihan: {df['total_charge'].skew():.4f}")
print(f"Kurtosis tagihan: {df['total_charge'].kurtosis():.4f}")

# Correlation Matrix
correlation_matrix = df[['age', 'total_minutes', 'total_calls', 'total_charge']].corr()
print(correlation_matrix)

# Value counts (frequency)
print(df['churn'].value_counts())
print(df['churn'].value_counts(normalize=True))  # Proporsi

# Detecting Outliers dengan IQR
Q1 = df['total_charge'].quantile(0.25)
Q3 = df['total_charge'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['total_charge'] < lower_bound) | 
              (df['total_charge'] > upper_bound)]
print(f"Jumlah outliers: {len(outliers)}")
```

### 3.4 Integrasi NumPy dan Pandas untuk Churn Prediction

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# ============================================================
# COMPLETE WORKFLOW: PREPARASI DATA UNTUK MODELING
# ============================================================

# 1. Load data (simulasi)
np.random.seed(42)
n_samples = 1000

# Generate synthetic dataset
data = {
    'customer_id': [f'C{i:04d}' for i in range(n_samples)],
    'age': np.random.randint(18, 80, n_samples),
    'total_minutes': np.random.normal(250, 80, n_samples),
    'total_calls': np.random.poisson(100, n_samples),
    'customer_service_calls': np.random.poisson(2, n_samples),
    'international_plan': np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
    'account_length': np.random.randint(1, 100, n_samples)
}

df = pd.DataFrame(data)

# Generate target variable (churn) dengan pola logis
# Pelanggan dengan banyak keluhan dan durasi pendek lebih mungkin churn
churn_prob = 1 / (1 + np.exp(-(-3 + 
                              0.5 * df['customer_service_calls'] - 
                              0.005 * df['total_minutes'] +
                              0.3 * df['international_plan'])))
df['churn'] = (np.random.random(n_samples) < churn_prob).astype(int)

# 2. Feature Engineering
df['charge_per_minute'] = np.where(df['total_minutes'] > 0, 
                                    df['total_minutes'] * 0.15, 0)
df['is_high_risk'] = ((df['customer_service_calls'] > 3) | 
                       (df['total_minutes'] < 150)).astype(int)

# 3. Statistical Analysis - Memahami distribusi
print("=== STATISTIK DESKRIPTIF ===")
numeric_cols = ['age', 'total_minutes', 'total_calls', 'customer_service_calls']
print(df[numeric_cols].describe())

print("\n=== SPREAD/VARIANCE ANALYSIS ===")
for col in numeric_cols:
    print(f"{col}:")
    print(f"  Std Dev: {df[col].std():.4f}")
    print(f"  Variance: {df[col].var():.4f}")
    print(f"  CV: {(df[col].std()/df[col].mean())*100:.2f}%")

print("\n=== CHURN ANALYSIS ===")
churn_stats = df.groupby('churn')[numeric_cols].mean()
print(churn_stats)

# 4. Preprocessing untuk Modeling
# Seleksi fitur
feature_cols = ['age', 'total_minutes', 'total_calls', 
                'customer_service_calls', 'account_length', 
                'charge_per_minute', 'is_high_risk']

X = df[feature_cols].values  # Convert ke NumPy array (Matrix)
y = df['churn'].values       # Target vector

print(f"\nFeature Matrix Shape: {X.shape}")  # (1000, 7)
print(f"Target Vector Shape: {y.shape}")     # (1000,)

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Standardization (z-score normalization)
# Formula: z = (x - μ) / σ
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n=== SCALED DATA STATISTICS ===")
print(f"Mean (train): {np.mean(X_train_scaled, axis=0)}")
print(f"Std (train): {np.std(X_train_scaled, axis=0)}")
```

---

## 4. KESIMPULAN

Analisis ini menunjukkan bagaimana konsep-konsep fundamental Data Science diterapkan dalam kasus nyata prediksi customer churn pada industri telekomunikasi:

1. **Business Understanding**: Churn prediction merupakan kasus nyata yang berdampak signifikan pada revenue perusahaan telekomunikasi (Ahmad et al., 2019).

2. **Data Understanding**: Data telekomunikasi mencakup berbagai tipe (structured, semi-structured, unstructured) dan dapat direpresentasikan dalam struktur matematis (skalar, vektor, matriks).

3. **Statistical Foundation**: Konsep statistik deskriptif seperti ukuran pemusatan (mean, median), ukuran penyebaran (variance, standard deviation, IQR), dan ukuran asimetri (skewness, kurtosis) menjadi dasar dalam memahami pola data (Ajah & Nweke, 2019).

4. **Python Implementation**: NumPy menyediakan struktur array multidimensi dan operasi matematis efisien, sementara Pandas menawarkan manipulasi data tabular yang powerful.

5. **State-of-the-Art**: Menurut Imani et al. (2025), teknik machine learning modern seperti XGBoost dan ensemble methods telah terbukti efektif dalam meningkatkan akurasi prediksi churn hingga mencapai AUC 93%+ seperti yang ditunjukkan oleh Ahmad et al. (2019).

---

## DAFTAR PUSTAKA (DENGAN LINK VALID)

Ahmad, A. K., Jafar, A., & Aljoumaa, K. (2019). Customer churn prediction in telecom using machine learning in big data platform. *Journal of Big Data*, *6*(1), Article 28. https://doi.org/10.1186/s40537-019-0191-6

Ajah, I. A., & Nweke, H. F. (2019). Big data and business analytics: Trends, platforms, success factors and applications. *Big Data and Cognitive Computing*, *3*(2), Article 32. https://doi.org/10.3390/bdcc3020032

Imani, M., Joudaki, M., & Beikmohammadi, A. (2025). Customer churn prediction: A systematic review of recent advances, trends, and challenges in machine learning and deep learning. *Machine Learning and Knowledge Extraction*, *7*(3), Article 105. https://doi.org/10.3390/make7030105

McKinney, W. (2012). *Python for data analysis: Data wrangling with Pandas, NumPy, and IPython*. O'Reilly Media.

---

*Dokumen ini dibuat sebagai referensi untuk analisis penerapan metode Data Science dengan basis jurnal ilmiah yang telah divalidasi.*

**Status Validasi:** ✅ Link Jurnal Aktif dan Dapat Diakses
- Jurnal 1 (Ahmad et al., 2019): Springer Open Access - AKTIF
- Jurnal 2 (Ajah & Nweke, 2019): MDPI Open Access - AKTIF  
- Jurnal 3 (Imani et al., 2025): MDPI Open Access - AKTIF
