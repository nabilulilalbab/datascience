# Customer Churn Prediction using Machine Learning

A data science project implementing customer churn prediction for the telecommunications industry. This project includes both baseline implementation with synthetic data and validation using real IBM Telco customer data from Kaggle.

## Project Overview

This project demonstrates a complete machine learning pipeline for predicting customer churn. The analysis uses Random Forest Classifier and achieves 78.99% accuracy on the real dataset with 7,043 customer records and 19 features.

The project is organized into two main components:
- Baseline implementation using generated synthetic data for initial model development
- Production validation using IBM Telco Customer Churn dataset from Kaggle

## Directory Structure

```
project/
├── 01_synthetic_baseline/          # Baseline implementation
├── 02_real_data_implementation/    # Production validation
├── 04_references/                  # Academic journals and materials
├── 05_research_notes/              # Research documentation
├── README.md
└── PROJECT_STRUCTURE.md
```

For detailed navigation and file descriptions, refer to [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md).

## Getting Started

### Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)

### Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

Navigate to the implementation directory and execute scripts in sequence:

```bash
cd 02_real_data_implementation

# Step 1: Data cleaning
python data_cleaning_real.py

# Step 2: Exploratory data analysis
python eda_real_data.py

# Step 3: Model training and evaluation
python churn_prediction_real.py

# Step 4: Performance comparison
python comparison_synthetic_vs_real.py
```

## Results

### Model Performance

| Metric | Synthetic Baseline | Real Data | Improvement |
|--------|-------------------|-----------|-------------|
| Accuracy | 76.00% | 78.99% | +2.99% |
| AUC-ROC | 0.8389 | 0.8212 | Comparable |
| Dataset Size | 1,000 | 7,043 | 7x larger |
| Features | 9 | 19 | 10 additional |

### Key Findings

The model identifies three primary factors contributing to customer churn:

1. Total charges paid over customer lifetime (16.57% importance)
2. Monthly billing amount (16.29% importance)
3. Length of customer relationship in months (14.86% importance)

Business analysis reveals significant churn rate variation by contract type:
- Month-to-month contracts: 42.71% churn rate
- One-year contracts: 11.28% churn rate
- Two-year contracts: 2.83% churn rate

Additionally, customers using fiber optic internet service show elevated churn rates at 41.89%.

## Documentation

Technical documentation and reports are available in the following locations:

- Complete navigation guide: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- Implementation details: `02_real_data_implementation/README.md`
- Baseline methodology: `01_synthetic_baseline/README.md`

## References

This project references three peer-reviewed academic journals:

1. Ahmad, A. K., Jafar, A., & Aljoumaa, K. (2019). Customer churn prediction in telecom using machine learning in big data platform. *Journal of Big Data*, 6(1).

2. Ajah, I. A., & Nweke, H. F. (2019). Big data and business analytics: Trends, platforms, success factors and applications. *Big Data and Cognitive Computing*, 3(2).

3. Imani, M., Joudaki, M., & Beikmohammadi, A. (2025). Customer churn prediction: A systematic review. *Machine Learning and Knowledge Extraction*, 7(1).

### Dataset Source

IBM Telco Customer Churn dataset available at: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Technical Stack

- Python 3.11
- pandas, numpy (data processing)
- matplotlib, seaborn (visualization)
- scikit-learn (machine learning)

## Project Status

Current version: 2.0  
Last updated: April 5, 2026  
Status: Complete and validated
