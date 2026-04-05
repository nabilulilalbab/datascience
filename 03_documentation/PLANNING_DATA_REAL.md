# Planning: Migrasi ke Dataset Real IBM Telco Customer Churn

## Executive Summary

Planning ini menjelaskan strategi untuk **migrasi dari dataset synthetic (1,000 rows, 9 columns) ke dataset real IBM Telco Customer Churn dari Kaggle (7,043 rows, 21 columns)** tanpa mengubah struktur proyek yang sudah ada.

---

## 1. Analisis Gap Dataset

### Dataset Synthetic (Current)
```
Rows: 1,000
Columns: 9
- CustomerID
- Gender (Male/Female)
- Age (18-64)
- Subscription_Type (Prepaid/Postpaid)
- Monthly_Bill (Rp 50k-200k)
- Total_Usage_Minutes (50-999 menit)
- Customer_Service_Calls (0-5)
- Past_Due_Days (0-29)
- Churn_Status (Yes/No)
```

### Dataset Real IBM Kaggle
```
Rows: 7,043
Columns: 21
- customerID
- gender (Male/Female)
- SeniorCitizen (0/1)
- Partner (Yes/No)
- Dependents (Yes/No)
- tenure (months: 0-72)
- PhoneService (Yes/No)
- MultipleLines (Yes/No/No phone service)
- InternetService (DSL/Fiber optic/No)
- OnlineSecurity (Yes/No/No internet service)
- OnlineBackup (Yes/No/No internet service)
- DeviceProtection (Yes/No/No internet service)
- TechSupport (Yes/No/No internet service)
- StreamingTV (Yes/No/No internet service)
- StreamingMovies (Yes/No/No internet service)
- Contract (Month-to-month/One year/Two year)
- PaperlessBilling (Yes/No)
- PaymentMethod (4 categories)
- MonthlyCharges (18.25-118.75)
- TotalCharges (18.8-8684.8) ️ STRING dengan 11 whitespace values
- Churn (Yes/No)
```

### Churn Rate Comparison
- **Synthetic:** ~50% (balanced untuk pembelajaran)
- **Real:** 26.54% (imbalanced, lebih realistis)

---

## 2. Strategi Migrasi

### Pendekatan: **Incremental Migration**

Kita akan membuat **2 versi kode** yang dapat berjalan paralel:

**A. Keep Existing (Synthetic) - untuk dokumentasi pembelajaran**
   - `churn_prediction.py` (existing)
   - `generate_data.py` (existing)
   - `telecom_churn.csv` (existing)

**B. Create New (Real Data) - untuk analisis real-world**
   - `churn_prediction_real.py` (new)
   - `WA_Fn-UseC_-Telco-Customer-Churn.csv` (already exists)
   - Update laporan dengan section komparasi

---

## 3. Mapping Fitur: Synthetic  Real

| Synthetic Feature | Real Feature | Transformation Needed |
|-------------------|--------------|----------------------|
| `CustomerID` | `customerID` | Rename only |
| `Gender` | `gender` | Capitalize values |
| `Age` | `SeniorCitizen` | ️ Convert: Age  Binary (0/1) |
| `Subscription_Type` | `Contract` | ️ Map: PrepaidMonth-to-month, PostpaidOne year |
| `Monthly_Bill` | `MonthlyCharges` | Scale conversion (Rp  $) |
| `Total_Usage_Minutes` | `tenure` | ️ Semantic different: minutes  months |
| `Customer_Service_Calls` | `TechSupport` | ️ Convert: Count  Binary |
| `Past_Due_Days` |  NOT AVAILABLE | Feature engineering needed |
| `Churn_Status` | `Churn` | Rename only |

### ️ Major Transformation Issues:
1. **Age vs SeniorCitizen**: Kehilangan granularity (continuous  binary)
2. **Total_Usage_Minutes vs tenure**: Semantik berbeda (usage intensity  loyalty duration)
3. **Customer_Service_Calls vs TechSupport**: Type berbeda (count  binary)
4. **Past_Due_Days**: Tidak ada padanan di dataset real

---

## 4. Opsi Implementasi

### Opsi A: **Adaptasi Sederhana** (Rekomendasi untuk Pembelajaran)
Gunakan fitur yang ada di dataset real dengan minimal preprocessing.

**Fitur yang digunakan:**
- Demographics: gender, SeniorCitizen, Partner, Dependents
- Services: PhoneService, InternetService, Contract
- Billing: MonthlyCharges, TotalCharges, tenure
- Target: Churn

**Kelebihan:**
-  Simple dan straightforward
-  Memanfaatkan fitur service yang kaya
-  Lebih realistis untuk use case telekomunikasi

**Kekurangan:**
-  Tidak 1:1 dengan model synthetic
-  Perlu re-training dan re-evaluasi

---

### Opsi B: **Feature Engineering untuk Matching** (Kompleks)
Engineer fitur baru agar match dengan model synthetic.

**Transformasi:**
```python
# Age approximation (reverse engineering dari SeniorCitizen)
df['Age'] = df['SeniorCitizen'].map({0: 40, 1: 65})  # Crude approximation

# Total_Usage_Minutes dari tenure
df['Total_Usage_Minutes'] = df['tenure'] * 30  # Assuming 30 hours/month

# Customer_Service_Calls dari TechSupport + OnlineSecurity
df['Customer_Service_Calls'] = (
    df['TechSupport'].eq('No').astype(int) + 
    df['OnlineSecurity'].eq('No').astype(int)
)

# Past_Due_Days dari PaymentMethod
# Electronic check  higher risk  estimated days
```

**Kelebihan:**
-  Konsisten dengan model yang sudah dilatih
-  Bisa compare apple-to-apple

**Kekurangan:**
-  Banyak asumsi (not data-driven)
-  Engineered features mungkin tidak akurat
-  Kompleksitas tinggi

---

### Opsi C: **Full Re-implementation** (Rekomendasi untuk Production)
Rebuild model dari scratch dengan semua 21 fitur.

**Fitur yang digunakan:** ALL 21 columns

**Kelebihan:**
-  Memanfaatkan full richness dataset
-  Performa model lebih baik (lebih banyak signal)
-  Lebih representative untuk real-world

**Kekurangan:**
-  Tidak comparable dengan hasil synthetic
-  Butuh dokumentasi baru
-  Laporan harus di-update extensively

---

## 5. Masalah Data Quality yang Harus Diselesaikan

### Issue 1: TotalCharges Non-Numeric
```python
# Problem:
df['TotalCharges'].dtype  # object (string)
# 11 rows contain whitespace instead of numbers

# Solution:
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['MonthlyCharges'], inplace=True)
```

### Issue 2: Kategori "No internet service" / "No phone service"
```python
# Problem:
df['OnlineSecurity'].unique()
# ['No', 'Yes', 'No internet service']

# Solution A: Binary encoding
df['OnlineSecurity'] = df['OnlineSecurity'].replace({
    'No internet service': 'No'
})

# Solution B: Three-category (preserve information)
# Keep as is, use one-hot encoding
```

### Issue 3: Imbalanced Classes (26.54% churn)
```python
# Sudah handled di model existing dengan:
# class_weight='balanced'

# Atau tambahkan SMOTE:
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)
```

---

## 6. Tahapan Implementasi (Step by Step)

### Phase 1: Preparation (ANALYSIS ONLY - NO CODE CHANGES)
- [x] Analisis struktur dataset real  DONE
- [x] Identifikasi gap dengan synthetic  DONE
- [x] Buat planning dokumen  IN PROGRESS
- [ ] Review dan approval planning

### Phase 2: Data Cleaning Script
- [ ] Buat `data_cleaning_real.py`
  - Fix TotalCharges non-numeric
  - Handle "No service" categories
  - Validate data types
  - Check missing values
  - Export clean data

### Phase 3: Exploratory Data Analysis (EDA)
- [ ] Buat `eda_real_data.py`
  - Statistika deskriptif untuk 21 fitur
  - Visualisasi distribusi
  - Correlation analysis (21x21 heatmap)
  - Churn rate per kategori
  - Feature importance preliminary

### Phase 4: Model Development
- [ ] **Opsi A:** Buat `churn_prediction_real.py` (full 21 features)
- [ ] **Opsi B:** Buat `churn_prediction_real_adapted.py` (feature engineering)
- [ ] Implement preprocessing pipeline
- [ ] Train Random Forest dengan hyperparameter tuning
- [ ] Evaluate dengan metrik yang sama

### Phase 5: Comparison & Analysis
- [ ] Buat `comparison_synthetic_vs_real.py`
  - Compare model performance
  - Compare feature importance
  - Analyze prediction patterns
  - Statistical tests (if applicable)

### Phase 6: Documentation Update
- [ ] Update `REPORT.md`
  - Add section "5. Validasi dengan Data Real"
  - Compare hasil synthetic vs real
  - Discuss findings
- [ ] Update `README.md`
  - Add instructions untuk dual dataset
- [ ] Update Laporan Praktikum Word
  - Add Appendix: Real Data Analysis

---

## 7. Expected Results Comparison

### Model Performance Prediction

| Metrik | Synthetic (Current) | Real (Expected) | Reasoning |
|--------|---------------------|-----------------|-----------|
| **Accuracy** | 76% | 78-82% | More data, richer features |
| **AUC-ROC** | 0.8389 | 0.82-0.88 | Similar, maybe slightly better |
| **Precision (Churn)** | 0.73 | 0.65-0.75 | Lower due to imbalance |
| **Recall (Churn)** | 0.66 | 0.70-0.80 | Better with more features |
| **F1-Score** | 0.70 | 0.68-0.77 | Balanced improvement |

### Feature Importance (Predicted Top 5 for Real Data)
1. **Contract** (Month-to-month paling churn)
2. **tenure** (Pelanggan baru lebih churn)
3. **InternetService** (Fiber optic users different behavior)
4. **MonthlyCharges** (Higher charges  higher churn)
5. **TechSupport** (No support  higher churn)

---

## 8. Risk & Mitigation

### Risk 1: Model Tidak Comparable
**Impact:** Tidak bisa claim "improvement" dari synthetic
**Mitigation:** Fokus pada "validation" bukan "comparison"

### Risk 2: Performa Lebih Buruk
**Impact:** Expectation mismatch
**Mitigation:** Explain imbalanced data, real-world complexity

### Risk 3: Overhead Maintenance
**Impact:** 2 codebase untuk maintain
**Mitigation:** Modular design, clear documentation

---

## 9. Rekomendasi Final

### Untuk Keperluan Akademik/Pembelajaran:
**Pilih Opsi C (Full Re-implementation)**

**Reasoning:**
1. Dataset real punya 21 fitur yang sangat kaya  jangan disia-siakan
2. Bisa showcase kemampuan handle real-world complexity
3. Hasil lebih impressive untuk portfolio
4. Lebih sesuai dengan best practice industry

**Action Items:**
1. Buat `churn_prediction_real.py` dengan ALL features
2. Full EDA dengan 21 fitur
3. Update laporan dengan section baru "Validasi Data Real"
4. Keep synthetic version sebagai "baseline/learning version"

### Untuk Keperluan Riset/Publikasi:
**Pilih Opsi C + Comparison Analysis**

**Additional Requirements:**
1. Statistical significance tests
2. Cross-validation (k-fold)
3. Hyperparameter tuning (Grid/Random Search)
4. Ensemble comparison (RF vs XGBoost vs LightGBM)

---

## 10. Timeline Estimate

| Phase | Task | Estimated Time |
|-------|------|----------------|
| 1 | Planning & Analysis |  DONE |
| 2 | Data Cleaning Script | 1-2 hours |
| 3 | EDA Real Data | 2-3 hours |
| 4 | Model Development | 3-4 hours |
| 5 | Comparison Analysis | 2 hours |
| 6 | Documentation Update | 2-3 hours |
| **TOTAL** | | **10-14 hours** |

---

## 11. File Structure (After Implementation)

```
project/
├── data/
│   ├── telecom_churn.csv (synthetic - 1K rows)
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv (real - 7K rows)
├── scripts/
│   ├── generate_data.py (synthetic generation)
│   ├── churn_prediction.py (synthetic analysis)
│   ├── data_cleaning_real.py (NEW - cleaning real data)
│   ├── churn_prediction_real.py (NEW - real data analysis)
│   └── comparison_synthetic_vs_real.py (NEW - comparison)
├── output_visual/
│   ├── [existing synthetic visualizations]
│   └── real_data/ (NEW)
│       ├── eda_real_*.png
│       └── model_real_*.png
├── docs/
│   ├── README.md (updated)
│   ├── REPORT.md (updated with real data section)
│   ├── DATASET_REFERENCE.md
│   ├── PLANNING_DATA_REAL.md (this file)
│   └── Laporan_Praktikum_*.docx (updated)
└── requirements.txt (maybe add imblearn for SMOTE)
```

---

## 12. Next Steps (When Ready to Implement)

**Command to execute when approved:**
```bash
# Phase 2: Data Cleaning
python scripts/data_cleaning_real.py

# Phase 3: EDA
python scripts/eda_real_data.py

# Phase 4: Model Training
python scripts/churn_prediction_real.py

# Phase 5: Comparison
python scripts/comparison_synthetic_vs_real.py
```

---

## Conclusion

Planning ini menyediakan **3 opsi implementasi** dengan **Opsi C (Full Re-implementation)** sebagai rekomendasi utama untuk memaksimalkan value dari dataset real yang sangat kaya (21 fitur).

**Key Decision Points:**
1.  Keep synthetic version untuk dokumentasi pembelajaran
2.  Build new version dengan real data (full features)
3.  Update dokumentasi untuk include both versions
4. ⏸️ Wait for approval sebelum mulai coding

**Ready to proceed?** Konfirmasi pilihan opsi (A/B/C) untuk mulai implementasi.

---

*Planning Document Created: 5 April 2026*  
*Status: DRAFT - Awaiting Approval*  
*Next Action: Review & Approve  Execute Phase 2*
