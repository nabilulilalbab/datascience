# Synthetic Baseline Implementation

This directory contains the initial baseline implementation of the customer churn prediction model using generated synthetic data.

## Purpose

The synthetic baseline serves as a controlled environment for:
- Initial model development and testing
- Understanding the machine learning pipeline
- Establishing performance benchmarks
- Educational demonstration of the methodology

## Contents

### Scripts

- **generate_data.py** - Generates synthetic customer data with controlled characteristics
- **churn_prediction.py** - Complete machine learning pipeline including preprocessing, training, and evaluation

### Data

- **telecom_churn.csv** - Synthetic dataset with 1,000 customer records and 9 features

### Outputs

- **output_visual/** - Directory containing visualization outputs
  - distribusi_churn.png - Bar chart showing churn distribution
  - histogram_numerik.png - Histograms of numerical features
  - korelasi_heatmap.png - Correlation matrix heatmap

## Dataset Specifications

- Total Records: 1,000
- Features: 9 attributes
  - CustomerID
  - Gender
  - Age
  - Subscription_Type
  - Monthly_Bill
  - Total_Usage_Minutes
  - Customer_Service_Calls
  - Past_Due_Days
  - Churn_Status (target variable)

## Performance Results

- Accuracy: 76.00%
- AUC-ROC: 0.8389
- Churn Rate: 41.40% (balanced distribution)

## Usage

Generate synthetic data:
```bash
python generate_data.py
```

Run the complete pipeline:
```bash
python churn_prediction.py
```

## Notes

This implementation uses synthetic data for baseline development. For production validation with real-world data, refer to the `02_real_data_implementation/` directory.

The synthetic data is designed to have clean, balanced characteristics to facilitate initial model development and understanding of the prediction pipeline.
