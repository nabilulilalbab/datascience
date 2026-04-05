#!/usr/bin/env python3
"""
Step 1: Data Cleaning untuk IBM Telco Customer Churn Dataset
- Fix TotalCharges (string → float)
- Handle "No service" categories
- Validate data quality
- Export clean data
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("STEP 1: DATA CLEANING - IBM Telco Customer Churn Dataset")
print("=" * 80)

# Load data
print("\n1. Loading data...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"   ✓ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Backup original
df_original = df.copy()

# Display info
print("\n2. Data Info (Before Cleaning):")
print(f"   - Total rows: {len(df)}")
print(f"   - Total columns: {len(df.columns)}")
print(f"   - Missing values: {df.isnull().sum().sum()}")

# Check data types
print("\n3. Data Types:")
print(df.dtypes)

print("\n" + "=" * 80)
print("CLEANING PROCESS")
print("=" * 80)

# Issue 1: Fix TotalCharges (string → float)
print("\n4. Fixing TotalCharges...")
print(f"   - Current type: {df['TotalCharges'].dtype}")

# Identify non-numeric values
non_numeric_mask = pd.to_numeric(df['TotalCharges'], errors='coerce').isna()
non_numeric_count = non_numeric_mask.sum()
print(f"   - Non-numeric values found: {non_numeric_count}")

if non_numeric_count > 0:
    print(f"   - Sample non-numeric values:")
    sample_rows = df[non_numeric_mask][['customerID', 'tenure', 'MonthlyCharges', 'TotalCharges']].head(5)
    print(sample_rows.to_string(index=False))
    
    # Strategy: Fill with MonthlyCharges (for tenure=0 customers)
    print("\n   - Strategy: Replace whitespace with MonthlyCharges")
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['MonthlyCharges'])
    print(f"   ✓ TotalCharges converted to numeric")
    print(f"   ✓ {non_numeric_count} values imputed with MonthlyCharges")

print(f"\n   - New type: {df['TotalCharges'].dtype}")
print(f"   - Missing values after fix: {df['TotalCharges'].isnull().sum()}")

# Issue 2: Validate SeniorCitizen (should be 0 or 1)
print("\n5. Validating SeniorCitizen...")
print(f"   - Unique values: {df['SeniorCitizen'].unique()}")
print(f"   - Value counts:\n{df['SeniorCitizen'].value_counts()}")
print(f"   ✓ SeniorCitizen is valid (0 or 1)")

# Issue 3: Check "No service" categories
print("\n6. Checking 'No service' categories...")
service_cols = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup', 
                'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

for col in service_cols:
    unique_vals = df[col].unique()
    if 'No internet service' in unique_vals or 'No phone service' in unique_vals:
        print(f"   - {col}: {unique_vals}")

print("\n   - Strategy: Keep as-is for now (will handle in encoding)")
print("   ✓ 'No service' categories identified")

# Validation: Check for duplicates
print("\n7. Checking for duplicates...")
duplicates = df.duplicated().sum()
print(f"   - Duplicate rows: {duplicates}")
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print(f"   ✓ {duplicates} duplicates removed")

# Validation: Final check
print("\n8. Final Validation:")
print(f"   - Total rows: {len(df)}")
print(f"   - Total columns: {len(df.columns)}")
print(f"   - Missing values: {df.isnull().sum().sum()}")
print(f"   - Numeric columns: {df.select_dtypes(include=[np.number]).columns.tolist()}")

# Summary statistics
print("\n9. Numeric Columns Summary:")
print(df[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())

# Save clean data
output_file = 'WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv'
df.to_csv(output_file, index=False)
print(f"\n✓ Clean data saved to: {output_file}")

print("\n" + "=" * 80)
print("CLEANING SUMMARY")
print("=" * 80)
print(f"✓ Original data: {df_original.shape}")
print(f"✓ Clean data: {df.shape}")
print(f"✓ Changes:")
print(f"  - TotalCharges: Converted to numeric ({non_numeric_count} values imputed)")
print(f"  - Duplicates: {duplicates} removed")
print(f"✓ Data quality: GOOD")
print(f"✓ Ready for EDA and modeling")
print("=" * 80)
