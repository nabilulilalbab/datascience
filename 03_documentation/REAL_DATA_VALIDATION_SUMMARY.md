# Real Data Validation Summary

**Dataset:** IBM Telco Customer Churn (Kaggle)  
**Implementation Date:** April 5, 2026  
**Status:** Complete and Validated

## Overview

This document summarizes the validation results of the customer churn prediction model using real-world data from IBM Telco Customer Churn dataset obtained from Kaggle.

## Dataset Specifications

- **Source:** Kaggle - IBM Telco Customer Churn
- **URL:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **Total Records:** 7,043 customer entries
- **Features:** 21 attributes (19 after preprocessing)
- **Target Variable:** Churn (Yes/No)
- **Class Distribution:** 26.54% churn, 73.46% no churn (imbalanced)

## Implementation Pipeline

The validation followed a six-stage pipeline:

1. **Data Cleaning** - Fixed TotalCharges data type issues (11 values corrected)
2. **Exploratory Data Analysis** - Statistical analysis and visualization
3. **Preprocessing** - Label encoding of 15 categorical features
4. **Model Training** - Random Forest Classifier (100 estimators, balanced weights)
5. **Evaluation** - Performance metrics calculation
6. **Comparison** - Synthetic baseline vs real data analysis

## Performance Results

### Model Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 78.99% |
| AUC-ROC | 0.8212 |
| Precision (Churn) | 0.64 |
| Recall (Churn) | 0.48 |
| F1-Score (Churn) | 0.55 |

### Confusion Matrix (Test Set: 1,409 samples)

|           | Predicted No | Predicted Yes |
|-----------|--------------|---------------|
| Actual No | 934          | 101           |
| Actual Yes| 195          | 179           |

## Feature Importance Analysis

Top three predictive features identified:

1. **TotalCharges** - 16.57% importance
   - Represents total amount charged to customer over relationship lifetime
   
2. **MonthlyCharges** - 16.29% importance
   - Current monthly billing amount
   
3. **tenure** - 14.86% importance
   - Length of customer relationship in months

## Business Insights

### Contract Type Impact

Analysis reveals strong correlation between contract type and churn behavior:

- Month-to-month contracts: 42.71% churn rate (high risk)
- One-year contracts: 11.28% churn rate (moderate risk)
- Two-year contracts: 2.83% churn rate (low risk)

**Recommendation:** Incentivize customers to commit to longer-term contracts through promotional offers or discounts.

### Service Quality Indicators

- Fiber optic internet users show elevated churn rate of 41.89%
- TechSupport availability ranks as 6th most important feature

**Recommendation:** Improve fiber optic service quality and technical support responsiveness to reduce churn in this segment.

## Comparison: Synthetic vs Real Data

| Aspect | Synthetic Baseline | Real Data | Difference |
|--------|-------------------|-----------|------------|
| Dataset Size | 1,000 | 7,043 | 7x larger |
| Feature Count | 9 | 19 | 10 additional features |
| Accuracy | 76.00% | 78.99% | +2.99% improvement |
| AUC-ROC | 0.8389 | 0.8212 | Comparable performance |
| Churn Rate | 41.40% | 26.54% | More realistic distribution |

## Validation Conclusions

1. **Model Effectiveness Confirmed** - The Random Forest approach demonstrates consistent performance across both synthetic and real datasets, validating the methodology.

2. **Improved Accuracy** - Real data implementation achieved 2.99% higher accuracy compared to synthetic baseline.

3. **Realistic Scenario** - Real data provides more challenging and realistic class imbalance (26.54% vs 41.40%), better reflecting actual business conditions.

4. **Richer Feature Set** - 19 features in real data enable more nuanced predictions and deeper business insights.

5. **AUC Performance** - Both implementations achieve AUC greater than 0.80, categorized as "Good" discriminative ability.

## Implementation Files

All validation code and results are available in:

- Location: `02_real_data_implementation/`
- Scripts: 4 Python files (cleaning, EDA, modeling, comparison)
- Outputs: 10 files (7 visualizations + 3 data files)

## References

This validation uses the dataset referenced in:

- Ahmad, A. K., Jafar, A., & Aljoumaa, K. (2019). Customer churn prediction in telecom using machine learning in big data platform. Journal of Big Data, 6(1).

---

**Document Version:** 1.0  
**Last Updated:** April 5, 2026
