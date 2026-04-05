# Real Data Implementation and Validation

This directory contains the production validation implementation using the IBM Telco Customer Churn dataset from Kaggle.

## Purpose

This implementation validates the churn prediction model with real-world data to:
- Verify model effectiveness on actual customer data
- Analyze performance with realistic class imbalance
- Extract actionable business insights
- Demonstrate production-ready implementation

## Contents

### Scripts (Execute in Order)

1. **data_cleaning_real.py** - Data preprocessing and quality validation
   - Fixes TotalCharges data type issues
   - Validates data integrity
   - Outputs cleaned dataset

2. **eda_real_data.py** - Exploratory data analysis
   - Statistical analysis of 21 features
   - Distribution visualization
   - Correlation analysis
   - Business pattern identification

3. **churn_prediction_real.py** - Model training and evaluation
   - Label encoding of categorical features
   - Random Forest model training
   - Performance evaluation
   - Feature importance analysis

4. **comparison_synthetic_vs_real.py** - Comparative analysis
   - Performance comparison
   - Dataset characteristics comparison
   - Visualization of differences

### Data Files

- **WA_Fn-UseC_-Telco-Customer-Churn.csv** - Raw dataset from Kaggle (7,043 records)
- **WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv** - Cleaned and validated dataset

### Output Directory

**output_visual_real/** contains 10 analysis files:

Visualizations (7 PNG files):
- histogram_numerik.png - Distribution of numerical features
- distribusi_churn.png - Churn class distribution
- korelasi_heatmap_numeric.png - Correlation matrix
- churn_by_contract.png - Churn rates by contract type
- confusion_matrix.png - Model prediction matrix
- feature_importance.png - Top 15 feature importance chart
- comparison_synthetic_vs_real.png - Performance comparison visualization

Data Files (3 CSV files):
- statistik_deskriptif.csv - Descriptive statistics
- feature_importance.csv - Complete feature importance values
- comparison_table.csv - Detailed comparison metrics

## Dataset Specifications

- Source: Kaggle - IBM Telco Customer Churn
- Total Records: 7,043 customers
- Features: 21 attributes (19 used after preprocessing)
- Target: Churn (Yes/No)
- Class Distribution: 26.54% churn, 73.46% no churn (imbalanced)
- URL: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Performance Results

### Model Metrics

- Accuracy: 78.99%
- AUC-ROC: 0.8212
- Precision (Churn): 0.64
- Recall (Churn): 0.48
- F1-Score (Churn): 0.55

### Feature Importance (Top 3)

1. TotalCharges - 16.57%
2. MonthlyCharges - 16.29%
3. tenure - 14.86%

## Key Business Insights

### Contract Type Analysis

- Month-to-month contracts: 42.71% churn rate
- One-year contracts: 11.28% churn rate
- Two-year contracts: 2.83% churn rate

Recommendation: Incentivize long-term contract commitments.

### Service Quality Indicators

- Fiber optic internet users: 41.89% churn rate
- Technical support availability impacts retention

Recommendation: Improve fiber service quality and support responsiveness.

## Execution Instructions

Run scripts in sequence:

```bash
# Step 1: Clean the data
python data_cleaning_real.py

# Step 2: Perform exploratory analysis
python eda_real_data.py

# Step 3: Train and evaluate model
python churn_prediction_real.py

# Step 4: Generate comparison analysis
python comparison_synthetic_vs_real.py
```

## Comparison with Synthetic Baseline

| Metric | Synthetic | Real | Change |
|--------|-----------|------|--------|
| Samples | 1,000 | 7,043 | 7x increase |
| Features | 9 | 19 | 10 additional |
| Accuracy | 76.00% | 78.99% | +2.99% |
| AUC-ROC | 0.8389 | 0.8212 | Comparable |
| Churn Rate | 41.40% | 26.54% | More realistic |

The real data implementation demonstrates improved accuracy while handling a more challenging and realistic imbalanced dataset.

## Technical Notes

- All categorical features use label encoding
- Random Forest trained with balanced class weights to handle imbalance
- Stratified train/test split (80/20) maintains class distribution
- All results are reproducible with random_state=42

## References

Dataset used in this validation is cited in:
- Ahmad, A. K., et al. (2019). Customer churn prediction in telecom using machine learning in big data platform. Journal of Big Data, 6(1).
