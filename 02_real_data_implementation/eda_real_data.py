#!/usr/bin/env python3
"""
Step 2: Exploratory Data Analysis (EDA) untuk IBM Telco Customer Churn Dataset
- Statistika deskriptif untuk 21 fitur
- Visualisasi distribusi
- Correlation analysis
- Churn analysis per kategori
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("STEP 2: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 80)

# Load clean data
print("\n1. Loading clean data...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv')
print(f"   ✓ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Create output directory
import os
os.makedirs('output_visual_real', exist_ok=True)
print(f"   ✓ Output directory created: output_visual_real/")

print("\n" + "=" * 80)
print("STATISTIKA DESKRIPTIF")
print("=" * 80)

# 2. Numeric Features Statistics
print("\n2. Statistika untuk Fitur Numerik:")
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
stats = df[numeric_cols].describe()
print(stats)

# Save statistics
stats.to_csv('output_visual_real/statistik_deskriptif.csv')
print("\n   ✓ Saved to: output_visual_real/statistik_deskriptif.csv")

# 3. Rumus Statistika (Manual Calculation untuk Validasi)
print("\n3. Validasi Rumus Statistika (Manual Calculation):")
for col in numeric_cols:
    n = len(df[col])
    mean = df[col].sum() / n
    variance = ((df[col] - mean) ** 2).sum() / (n - 1)
    std = np.sqrt(variance)
    range_val = df[col].max() - df[col].min()
    
    print(f"\n   {col}:")
    print(f"      n = {n}")
    print(f"      Mean (x̄) = Σxᵢ/n = {mean:.2f}")
    print(f"      Std Dev (s) = √[Σ(xᵢ-x̄)²/(n-1)] = {std:.2f}")
    print(f"      Range = max - min = {range_val:.2f}")

# 4. Categorical Features Distribution
print("\n" + "=" * 80)
print("DISTRIBUSI FITUR KATEGORIKAL")
print("=" * 80)

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
categorical_cols.remove('customerID')  # Remove ID
categorical_cols.remove('Churn')  # Will analyze separately

print(f"\n4. Categorical Features ({len(categorical_cols)} columns):")
for col in categorical_cols[:5]:  # First 5
    print(f"\n   {col}:")
    print(df[col].value_counts())

# 5. Churn Distribution
print("\n" + "=" * 80)
print("ANALISIS CHURN")
print("=" * 80)

print("\n5. Distribusi Churn:")
churn_counts = df['Churn'].value_counts()
print(churn_counts)
churn_rate = (df['Churn'] == 'Yes').sum() / len(df) * 100
print(f"\n   Churn Rate: {churn_rate:.2f}%")
print(f"   No Churn Rate: {100 - churn_rate:.2f}%")

# 6. Churn by Categorical Features
print("\n6. Churn Rate by Key Features:")

key_features = ['gender', 'SeniorCitizen', 'Partner', 'Contract', 'InternetService']
for feature in key_features:
    print(f"\n   {feature}:")
    churn_by_feature = pd.crosstab(df[feature], df['Churn'], normalize='index') * 100
    print(churn_by_feature.round(2))

print("\n" + "=" * 80)
print("VISUALISASI")
print("=" * 80)

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 7. Histogram untuk Numeric Features
print("\n7. Creating histogram untuk fitur numerik...")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribusi Fitur Numerik - IBM Telco Dataset', fontsize=16, fontweight='bold')

numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
colors = ['skyblue', 'lightcoral', 'lightgreen', 'gold']

for idx, (col, color) in enumerate(zip(numeric_features, colors)):
    row = idx // 2
    col_idx = idx % 2
    ax = axes[row, col_idx]
    
    ax.hist(df[col], bins=30, color=color, edgecolor='black', alpha=0.7)
    ax.set_title(f'Distribusi {col}', fontsize=12, fontweight='bold')
    ax.set_xlabel(col, fontsize=10)
    ax.set_ylabel('Frequency', fontsize=10)
    ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output_visual_real/histogram_numerik.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/histogram_numerik.png")
plt.close()

# 8. Churn Distribution Bar Chart
print("\n8. Creating bar chart untuk distribusi churn...")
fig, ax = plt.subplots(figsize=(10, 6))

churn_counts.plot(kind='bar', color=['green', 'red'], alpha=0.7, ax=ax)
ax.set_title('Distribusi Customer Churn - IBM Telco Dataset', fontsize=14, fontweight='bold')
ax.set_xlabel('Churn Status', fontsize=12)
ax.set_ylabel('Jumlah Customer', fontsize=12)
ax.set_xticklabels(['No Churn', 'Churn'], rotation=0)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, v in enumerate(churn_counts):
    ax.text(i, v + 50, f'{v}\n({v/len(df)*100:.1f}%)', 
            ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('output_visual_real/distribusi_churn.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/distribusi_churn.png")
plt.close()

# 9. Correlation Heatmap (Numeric only for now)
print("\n9. Creating correlation heatmap...")
fig, ax = plt.subplots(figsize=(10, 8))

# Select numeric columns
numeric_df = df[['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']]
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Matrix - Numeric Features', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('output_visual_real/korelasi_heatmap_numeric.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/korelasi_heatmap_numeric.png")
plt.close()

# 10. Churn by Contract Type
print("\n10. Creating churn analysis by Contract...")
fig, ax = plt.subplots(figsize=(10, 6))

contract_churn = pd.crosstab(df['Contract'], df['Churn'])
contract_churn.plot(kind='bar', stacked=False, color=['green', 'red'], alpha=0.7, ax=ax)
ax.set_title('Churn Distribution by Contract Type', fontsize=14, fontweight='bold')
ax.set_xlabel('Contract Type', fontsize=12)
ax.set_ylabel('Number of Customers', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.legend(['No Churn', 'Churn'], title='Status')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('output_visual_real/churn_by_contract.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/churn_by_contract.png")
plt.close()

print("\n" + "=" * 80)
print("EDA SUMMARY")
print("=" * 80)
print(f"✓ Statistika Deskriptif: Calculated for {len(numeric_cols)} numeric features")
print(f"✓ Categorical Analysis: Analyzed {len(categorical_cols)} categorical features")
print(f"✓ Churn Rate: {churn_rate:.2f}%")
print(f"✓ Visualizations Created: 4 plots")
print(f"  1. histogram_numerik.png")
print(f"  2. distribusi_churn.png")
print(f"  3. korelasi_heatmap_numeric.png")
print(f"  4. churn_by_contract.png")
print(f"✓ Output directory: output_visual_real/")
print("=" * 80)
