#!/usr/bin/env python3
"""
Step 6: Comparison Analysis - Synthetic vs Real Data
Compare model performance and insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 80)
print("COMPARISON ANALYSIS: SYNTHETIC vs REAL DATA")
print("=" * 80)

# Results from Synthetic Data (from previous run)
synthetic_results = {
    'dataset': 'Synthetic (Generated)',
    'samples': 1000,
    'features': 9,
    'churn_rate': 41.40,
    'accuracy': 76.00,
    'auc_roc': 0.8389,
    'precision_churn': 0.73,
    'recall_churn': 0.66,
    'f1_churn': 0.70,
    'confusion_matrix': [[97, 20], [28, 55]],  # [[TN, FP], [FN, TP]]
    'top_features': ['Customer_Service_Calls', 'Past_Due_Days', 'Total_Usage_Minutes']
}

# Results from Real Data (from current run)
real_results = {
    'dataset': 'Real IBM Telco',
    'samples': 7043,
    'features': 19,
    'churn_rate': 26.54,
    'accuracy': 78.99,
    'auc_roc': 0.8212,
    'precision_churn': 0.64,
    'recall_churn': 0.48,
    'f1_churn': 0.55,
    'confusion_matrix': [[934, 101], [195, 179]],  # [[TN, FP], [FN, TP]]
    'top_features': ['TotalCharges', 'MonthlyCharges', 'tenure']
}

print("\n" + "=" * 80)
print("1. DATASET COMPARISON")
print("=" * 80)

comparison_df = pd.DataFrame([synthetic_results, real_results])
print("\n")
print(comparison_df[['dataset', 'samples', 'features', 'churn_rate']].to_string(index=False))

print("\n" + "=" * 80)
print("2. MODEL PERFORMANCE COMPARISON")
print("=" * 80)

print("\nMetrik Evaluasi:")
print(f"{'Metric':<20} {'Synthetic':>12} {'Real':>12} {'Delta':>12}")
print("-" * 60)
print(f"{'Accuracy (%)':<20} {synthetic_results['accuracy']:>12.2f} {real_results['accuracy']:>12.2f} {real_results['accuracy']-synthetic_results['accuracy']:>+12.2f}")
print(f"{'AUC-ROC':<20} {synthetic_results['auc_roc']:>12.4f} {real_results['auc_roc']:>12.4f} {real_results['auc_roc']-synthetic_results['auc_roc']:>+12.4f}")
print(f"{'Precision (Churn)':<20} {synthetic_results['precision_churn']:>12.2f} {real_results['precision_churn']:>12.2f} {real_results['precision_churn']-synthetic_results['precision_churn']:>+12.2f}")
print(f"{'Recall (Churn)':<20} {synthetic_results['recall_churn']:>12.2f} {real_results['recall_churn']:>12.2f} {real_results['recall_churn']-synthetic_results['recall_churn']:>+12.2f}")
print(f"{'F1-Score (Churn)':<20} {synthetic_results['f1_churn']:>12.2f} {real_results['f1_churn']:>12.2f} {real_results['f1_churn']-synthetic_results['f1_churn']:>+12.2f}")

print("\n" + "=" * 80)
print("3. CONFUSION MATRIX COMPARISON")
print("=" * 80)

# Synthetic
cm_syn = synthetic_results['confusion_matrix']
print("\nSynthetic Data (200 test samples):")
print(f"  TN: {cm_syn[0][0]:4d}  |  FP: {cm_syn[0][1]:4d}")
print(f"  FN: {cm_syn[1][0]:4d}  |  TP: {cm_syn[1][1]:4d}")

# Real
cm_real = real_results['confusion_matrix']
print("\nReal Data (1,409 test samples):")
print(f"  TN: {cm_real[0][0]:4d}  |  FP: {cm_real[0][1]:4d}")
print(f"  FN: {cm_real[1][0]:4d}  |  TP: {cm_real[1][1]:4d}")

# Normalized comparison
print("\nNormalized (percentages):")
total_syn = sum([sum(row) for row in cm_syn])
total_real = sum([sum(row) for row in cm_real])

print(f"{'Metric':<20} {'Synthetic':>12} {'Real':>12}")
print("-" * 50)
print(f"{'TN %':<20} {cm_syn[0][0]/total_syn*100:>12.2f} {cm_real[0][0]/total_real*100:>12.2f}")
print(f"{'FP %':<20} {cm_syn[0][1]/total_syn*100:>12.2f} {cm_real[0][1]/total_real*100:>12.2f}")
print(f"{'FN %':<20} {cm_syn[1][0]/total_syn*100:>12.2f} {cm_real[1][0]/total_real*100:>12.2f}")
print(f"{'TP %':<20} {cm_syn[1][1]/total_syn*100:>12.2f} {cm_real[1][1]/total_real*100:>12.2f}")

print("\n" + "=" * 80)
print("4. KEY INSIGHTS")
print("=" * 80)

print("\n✓ Accuracy Improvement:")
acc_improvement = real_results['accuracy'] - synthetic_results['accuracy']
print(f"  Real data achieved {acc_improvement:+.2f}% higher accuracy")
print(f"  {synthetic_results['accuracy']:.2f}% → {real_results['accuracy']:.2f}%")

print("\n✓ AUC-ROC Comparison:")
auc_diff = real_results['auc_roc'] - synthetic_results['auc_roc']
print(f"  AUC difference: {auc_diff:+.4f}")
if abs(auc_diff) < 0.02:
    print(f"  → Similar discriminative ability (both 'Good' category)")
else:
    print(f"  → {'Real' if auc_diff > 0 else 'Synthetic'} data shows better class separation")

print("\n✓ Recall Trade-off:")
recall_diff = real_results['recall_churn'] - synthetic_results['recall_churn']
print(f"  Recall (Churn): {synthetic_results['recall_churn']:.2f} → {real_results['recall_churn']:.2f} ({recall_diff:+.2f})")
print(f"  → Real data has lower recall due to imbalanced classes (26.54% vs 41.40%)")
print(f"  → This is expected and more realistic")

print("\n✓ Dataset Characteristics:")
print(f"  Synthetic: Balanced dataset ({synthetic_results['churn_rate']:.2f}% churn)")
print(f"  Real: Imbalanced dataset ({real_results['churn_rate']:.2f}% churn)")
print(f"  → Real data reflects actual business scenario")

print("\n✓ Feature Richness:")
print(f"  Synthetic: {synthetic_results['features']} features (basic)")
print(f"  Real: {real_results['features']} features (comprehensive)")
print(f"  → Real data provides {real_results['features'] - synthetic_results['features']} additional features")

print("\n" + "=" * 80)
print("5. VISUALIZATIONS")
print("=" * 80)

# Create comparison visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Comparison: Synthetic vs Real Data', fontsize=16, fontweight='bold')

# 1. Accuracy & AUC comparison
ax1 = axes[0, 0]
metrics = ['Accuracy', 'AUC-ROC']
synthetic_vals = [synthetic_results['accuracy'], synthetic_results['auc_roc']*100]
real_vals = [real_results['accuracy'], real_results['auc_roc']*100]
x = range(len(metrics))
width = 0.35
ax1.bar([i - width/2 for i in x], synthetic_vals, width, label='Synthetic', color='skyblue')
ax1.bar([i + width/2 for i in x], real_vals, width, label='Real', color='coral')
ax1.set_ylabel('Score (%)', fontsize=10)
ax1.set_title('Accuracy & AUC Comparison', fontsize=12, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(metrics)
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# 2. Precision, Recall, F1 for Churn class
ax2 = axes[0, 1]
metrics2 = ['Precision', 'Recall', 'F1-Score']
synthetic_vals2 = [synthetic_results['precision_churn'], 
                   synthetic_results['recall_churn'], 
                   synthetic_results['f1_churn']]
real_vals2 = [real_results['precision_churn'], 
              real_results['recall_churn'], 
              real_results['f1_churn']]
x2 = range(len(metrics2))
ax2.bar([i - width/2 for i in x2], synthetic_vals2, width, label='Synthetic', color='skyblue')
ax2.bar([i + width/2 for i in x2], real_vals2, width, label='Real', color='coral')
ax2.set_ylabel('Score', fontsize=10)
ax2.set_title('Churn Class Metrics Comparison', fontsize=12, fontweight='bold')
ax2.set_xticks(x2)
ax2.set_xticklabels(metrics2, rotation=15)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# 3. Dataset characteristics
ax3 = axes[1, 0]
chars = ['Samples', 'Features', 'Churn Rate (%)']
synthetic_chars = [synthetic_results['samples']/100, 
                   synthetic_results['features'], 
                   synthetic_results['churn_rate']]
real_chars = [real_results['samples']/100, 
              real_results['features'], 
              real_results['churn_rate']]
x3 = range(len(chars))
ax3.bar([i - width/2 for i in x3], synthetic_chars, width, label='Synthetic', color='skyblue')
ax3.bar([i + width/2 for i in x3], real_chars, width, label='Real', color='coral')
ax3.set_ylabel('Value (Samples in 100s)', fontsize=10)
ax3.set_title('Dataset Characteristics', fontsize=12, fontweight='bold')
ax3.set_xticks(x3)
ax3.set_xticklabels(chars, rotation=15, ha='right')
ax3.legend()
ax3.grid(axis='y', alpha=0.3)

# 4. Summary text
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = f"""
SUMMARY COMPARISON

Dataset Size:
  Synthetic: {synthetic_results['samples']:,} samples
  Real: {real_results['samples']:,} samples
  → Real is {real_results['samples']/synthetic_results['samples']:.1f}x larger

Feature Count:
  Synthetic: {synthetic_results['features']} features
  Real: {real_results['features']} features
  → Real has {real_results['features'] - synthetic_results['features']} more features

Performance:
  Accuracy: {synthetic_results['accuracy']:.2f}% → {real_results['accuracy']:.2f}%
  AUC-ROC: {synthetic_results['auc_roc']:.4f} → {real_results['auc_roc']:.4f}
  
Key Finding:
  Both models show good performance
  Real data is more challenging due to
  imbalanced classes (26.54% churn)
  but achieves higher accuracy
"""
ax4.text(0.1, 0.5, summary_text, fontsize=10, family='monospace',
         verticalalignment='center')

plt.tight_layout()
plt.savefig('output_visual_real/comparison_synthetic_vs_real.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: output_visual_real/comparison_synthetic_vs_real.png")
plt.close()

# Save comparison table
comparison_table = pd.DataFrame([
    {'Metric': 'Dataset', 'Synthetic': synthetic_results['dataset'], 'Real': real_results['dataset']},
    {'Metric': 'Samples', 'Synthetic': synthetic_results['samples'], 'Real': real_results['samples']},
    {'Metric': 'Features', 'Synthetic': synthetic_results['features'], 'Real': real_results['features']},
    {'Metric': 'Churn Rate (%)', 'Synthetic': synthetic_results['churn_rate'], 'Real': real_results['churn_rate']},
    {'Metric': 'Accuracy (%)', 'Synthetic': synthetic_results['accuracy'], 'Real': real_results['accuracy']},
    {'Metric': 'AUC-ROC', 'Synthetic': synthetic_results['auc_roc'], 'Real': real_results['auc_roc']},
    {'Metric': 'Precision (Churn)', 'Synthetic': synthetic_results['precision_churn'], 'Real': real_results['precision_churn']},
    {'Metric': 'Recall (Churn)', 'Synthetic': synthetic_results['recall_churn'], 'Real': real_results['recall_churn']},
    {'Metric': 'F1-Score (Churn)', 'Synthetic': synthetic_results['f1_churn'], 'Real': real_results['f1_churn']},
])

comparison_table.to_csv('output_visual_real/comparison_table.csv', index=False)
print("✓ Saved: output_visual_real/comparison_table.csv")

print("\n" + "=" * 80)
print("COMPARISON COMPLETE")
print("=" * 80)
print("\n✓ Synthetic Data: Good baseline for learning")
print("✓ Real Data: Better accuracy with more realistic scenario")
print("✓ Both models perform in 'Good' range (AUC > 0.80)")
print("✓ Real data provides richer insights with 19 features")
print("\n" + "=" * 80)
