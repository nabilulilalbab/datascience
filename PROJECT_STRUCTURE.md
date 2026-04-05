# Project Structure Guide

This document provides a comprehensive overview of the project organization and file locations for the Customer Churn Prediction implementation.

**Project Type:** Data Science - Machine Learning  
**Last Updated:** April 2026

## Directory Organization

```
project/
├── 01_synthetic_baseline/          (7 files)   - Baseline implementation
├── 02_real_data_implementation/    (17 files)  - Real data validation
├── 04_references/                  (14 files)  - Journals & materials
├── 05_research_notes/              (4 files)   - Research notes
├── requirements.txt
├── .gitignore
└── PROJECT_STRUCTURE.md (this file)
```

---

## 1. Synthetic Baseline Implementation

**Location:** `01_synthetic_baseline/`  
**Purpose:** Initial implementation using generated synthetic data for model development and learning

### Contents

```
01_synthetic_baseline/
├── README.md
├── churn_prediction.py           - Complete ML pipeline
├── generate_data.py               - Synthetic data generator
├── telecom_churn.csv              - Generated dataset (1,000 samples)
└── output_visual/                 - Visualization outputs
    ├── distribusi_churn.png
    ├── histogram_numerik.png
    └── korelasi_heatmap.png
```

### Performance Metrics

- Dataset size: 1,000 samples
- Features: 9 attributes
- Model accuracy: 76.00%
- AUC-ROC score: 0.8389
- Churn rate: 41.40% (balanced distribution)

### Use Cases

- Baseline model development
- Understanding machine learning pipeline
- Initial feature engineering experiments

---

## 2. Real Data Implementation

**Location:** `02_real_data_implementation/`  
**Purpose:** Production validation using IBM Telco Customer Churn dataset from Kaggle

### Contents

```
02_real_data_implementation/
├── README.md
├── data_cleaning_real.py                      - Data preprocessing
├── eda_real_data.py                           - Exploratory analysis
├── churn_prediction_real.py                   - Model training and evaluation
├── comparison_synthetic_vs_real.py            - Performance comparison
├── WA_Fn-UseC_-Telco-Customer-Churn.csv       - Raw dataset
├── WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv - Cleaned dataset
└── output_visual_real/                        - Analysis outputs (10 files)
    ├── histogram_numerik.png
    ├── distribusi_churn.png
    ├── korelasi_heatmap_numeric.png
    ├── churn_by_contract.png
    ├── confusion_matrix.png
    ├── feature_importance.png
    ├── comparison_synthetic_vs_real.png
    ├── statistik_deskriptif.csv
    ├── feature_importance.csv
    └── comparison_table.csv
```

### Performance Metrics

- Dataset size: 7,043 samples
- Features: 19 attributes (after preprocessing)
- Model accuracy: 78.99%
- AUC-ROC score: 0.8212
- Churn rate: 26.54% (realistic imbalanced distribution)

### Key Insights

Top three predictive features:
1. TotalCharges - 16.57% feature importance
2. MonthlyCharges - 16.29% feature importance
3. tenure - 14.86% feature importance

Business analysis findings:
- Month-to-month contracts show 42.71% churn rate
- One-year contracts show 11.28% churn rate
- Two-year contracts show 2.83% churn rate
- Fiber optic internet users show 41.89% churn rate

---

## 3. Academic References

**Location:** `04_references/`  
**Purpose:** Peer-reviewed journals and learning materials

### Contents

```
04_references/
├── jurnal/                        - Academic papers (3 PDFs)
│   ├── s40537-019-0191-6.pdf     - Ahmad et al. (2019)
│   ├── BDCC-03-00032-v2.pdf      - Ajah & Nweke (2019)
│   └── make-07-00105.pdf         - Imani et al. (2025)
│
└── contoh/                        - Learning notebooks (11 files)
    ├── Matematika dan Statistika Deskriptif Data.ipynb
    ├── 2.5 Math Statistics - Spread.ipynb
    ├── Numpy_Pengenalan.ipynb
    ├── Pandas_dttype.ipynb
    └── ... (7 additional notebooks)
```

### Referenced Journals

1. Ahmad, A. K., Jafar, A., & Aljoumaa, K. (2019). Customer churn prediction in telecom using machine learning in big data platform. *Journal of Big Data*, 6(1).

2. Ajah, I. A., & Nweke, H. F. (2019). Big data and business analytics: Trends, platforms, success factors and applications. *Big Data and Cognitive Computing*, 3(2).

3. Imani, M., Joudaki, M., & Beikmohammadi, A. (2025). Customer churn prediction: A systematic review of recent advances in machine learning. *Machine Learning and Knowledge Extraction*, 7(1).

---

## 4. Research Notes

**Location:** `05_research_notes/`  
**Purpose:** Research documentation and preliminary analysis

### Contents

```
05_research_notes/
└── research-data-science-jurnal/
    ├── Analisis_Data_Science_Customer_Churn.md
    ├── Analisis_Data_Science_dengan_Jurnal_Valid.md
    ├── report.html
    └── report_final.html
```

---

## Quick Start Instructions

### For Synthetic Baseline

```bash
cd 01_synthetic_baseline
python generate_data.py
python churn_prediction.py
```

### For Real Data Implementation

Execute scripts in the following sequence:

```bash
cd 02_real_data_implementation

# Data preparation
python data_cleaning_real.py

# Exploratory analysis
python eda_real_data.py

# Model training and evaluation
python churn_prediction_real.py

# Performance comparison
python comparison_synthetic_vs_real.py
```

---

## Performance Comparison

| Metric | Synthetic Baseline | Real Data | Difference |
|--------|-------------------|-----------|------------|
| Dataset Size | 1,000 | 7,043 | 7x increase |
| Feature Count | 9 | 19 | 10 additional |
| Accuracy | 76.00% | 78.99% | +2.99% |
| AUC-ROC | 0.8389 | 0.8212 | Comparable |
| Churn Rate | 41.40% | 26.54% | More realistic |

The real data implementation demonstrates improved accuracy while working with a more realistic and challenging imbalanced dataset.

---

## Technical Requirements

- Python 3.11 or higher
- pandas, numpy (data processing)
- matplotlib, seaborn (visualization)
- scikit-learn (machine learning)

Install all dependencies using:
```bash
pip install -r requirements.txt
```

---

## Navigation Guide

### For New Users

1. Start with this document for overall project structure
2. Review `README.md` for project overview
3. Explore `01_synthetic_baseline/README.md` for baseline implementation
4. Examine `02_real_data_implementation/README.md` for production validation

### For Analysis and Results

- Visualizations: `02_real_data_implementation/output_visual_real/`
- Statistical data: CSV files in `output_visual_real/`
- Model performance: `comparison_table.csv`

### For References

- Academic journals: `04_references/jurnal/`
- Learning materials: `04_references/contoh/`
- Dataset source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

---

## Project Status

**Current Version:** 2.0  
**Status:** Complete and validated  
**Last Updated:** April 5, 2026

Implementation includes:
- Complete baseline implementation with synthetic data
- Production validation with real IBM Telco dataset
- Comprehensive documentation and analysis
- Academic reference integration
- Performance comparison and insights

---

*For detailed implementation information, refer to README files in respective directories.*
