#!/usr/bin/env python3
"""
Step 3-5: Full Pipeline - Preprocessing, Training, dan Evaluation
IBM Telco Customer Churn Dataset dengan 21 fitur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("CUSTOMER CHURN PREDICTION - IBM TELCO DATASET (REAL DATA)")
print("Full Pipeline: Preprocessing → Training → Evaluation")
print("=" * 80)

# Load clean data
print("\n1. Loading data...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn_CLEAN.csv')
print(f"   ✓ Data loaded: {df.shape}")

print("\n" + "=" * 80)
print("STEP 3: PREPROCESSING & FEATURE ENGINEERING")
print("=" * 80)

# 2. Drop customerID
print("\n2. Dropping customerID...")
df_model = df.drop('customerID', axis=1)
print(f"   ✓ Dropped customerID, shape: {df_model.shape}")

# 3. Encode Target Variable
print("\n3. Encoding target variable (Churn)...")
df_model['Churn'] = df_model['Churn'].map({'No': 0, 'Yes': 1})
print(f"   ✓ Churn encoded: No=0, Yes=1")
print(f"   - Class distribution: {df_model['Churn'].value_counts().to_dict()}")

# 4. Identify categorical columns
print("\n4. Identifying categorical columns...")
categorical_cols = df_model.select_dtypes(include=['object']).columns.tolist()
print(f"   ✓ Found {len(categorical_cols)} categorical columns:")
print(f"     {categorical_cols}")

# 5. Label Encoding for all categorical features
print("\n5. Label Encoding categorical features...")
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    label_encoders[col] = le
    print(f"   ✓ {col}: {len(le.classes_)} classes → {le.classes_[:3]}...")

print(f"\n   ✓ Total features after encoding: {df_model.shape[1]}")

# 6. Verify no object columns remain
print("\n6. Verification:")
object_cols = df_model.select_dtypes(include=['object']).columns.tolist()
print(f"   - Object columns remaining: {len(object_cols)}")
assert len(object_cols) == 0, "All columns should be numeric"
print(f"   ✓ All columns are numeric")

# 7. Separate features and target
print("\n7. Separating features (X) and target (y)...")
X = df_model.drop('Churn', axis=1)
y = df_model['Churn']
print(f"   ✓ X shape: {X.shape}")
print(f"   ✓ y shape: {y.shape}")
print(f"   ✓ Features ({X.shape[1]}): {list(X.columns)}")

print("\n" + "=" * 80)
print("STEP 4: MODEL TRAINING")
print("=" * 80)

# 8. Train-test split
print("\n8. Splitting data (80% train, 20% test, stratified)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"   ✓ Train set: {X_train.shape} | Test set: {X_test.shape}")
print(f"   ✓ Train churn rate: {y_train.mean()*100:.2f}%")
print(f"   ✓ Test churn rate: {y_test.mean()*100:.2f}%")

# 9. Train Random Forest
print("\n9. Training Random Forest Classifier...")
print(f"   - Parameters: n_estimators=100, class_weight='balanced', random_state=42")
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)
rf_model.fit(X_train, y_train)
print(f"   ✓ Model trained successfully")

# 10. Predictions
print("\n10. Making predictions...")
y_pred = rf_model.predict(X_test)
y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
print(f"   ✓ Predictions generated for {len(y_test)} samples")

print("\n" + "=" * 80)
print("STEP 5: MODEL EVALUATION")
print("=" * 80)

# 11. Calculate metrics
print("\n11. Performance Metrics:")
accuracy = accuracy_score(y_test, y_pred)
auc_score = roc_auc_score(y_test, y_pred_proba)

print(f"\n   Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"   AUC-ROC:   {auc_score:.4f}")

# 12. Confusion Matrix
print("\n12. Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"\n   True Negative (TN):  {cm[0,0]:4d} - Correctly predicted No Churn")
print(f"   False Positive (FP): {cm[0,1]:4d} - Incorrectly predicted Churn")
print(f"   False Negative (FN): {cm[1,0]:4d} - Missed Churn (Type II error)")
print(f"   True Positive (TP):  {cm[1,1]:4d} - Correctly predicted Churn")

# 13. Classification Report
print("\n13. Classification Report:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))

# 14. Feature Importance
print("\n14. Top 10 Feature Importance:")
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance.head(10).to_string(index=False))

# Save feature importance
feature_importance.to_csv('output_visual_real/feature_importance.csv', index=False)
print("\n   ✓ Saved to: output_visual_real/feature_importance.csv")

print("\n" + "=" * 80)
print("VISUALIZATIONS")
print("=" * 80)

# 15. Confusion Matrix Heatmap
print("\n15. Creating confusion matrix heatmap...")
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True,
            xticklabels=['No Churn', 'Churn'],
            yticklabels=['No Churn', 'Churn'])
plt.title('Confusion Matrix - IBM Telco Dataset', fontsize=14, fontweight='bold')
plt.ylabel('Actual', fontsize=12)
plt.xlabel('Predicted', fontsize=12)
plt.tight_layout()
plt.savefig('output_visual_real/confusion_matrix.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/confusion_matrix.png")
plt.close()

# 16. Feature Importance Plot
print("\n16. Creating feature importance plot...")
plt.figure(figsize=(10, 8))
top_15 = feature_importance.head(15)
plt.barh(range(len(top_15)), top_15['importance'], color='steelblue')
plt.yticks(range(len(top_15)), top_15['feature'])
plt.xlabel('Importance', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.title('Top 15 Feature Importance - Random Forest', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('output_visual_real/feature_importance.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved: output_visual_real/feature_importance.png")
plt.close()

print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)
print(f"\n✓ Dataset: IBM Telco Customer Churn (Real Data)")
print(f"✓ Total Samples: {len(df):,}")
print(f"✓ Total Features: {X.shape[1]} (after encoding)")
print(f"✓ Train/Test Split: {len(X_train)}/{len(X_test)} (80/20)")
print(f"\n✓ Model: Random Forest (100 estimators, balanced)")
print(f"✓ Accuracy: {accuracy*100:.2f}%")
print(f"✓ AUC-ROC: {auc_score:.4f}")
print(f"\n✓ Top 3 Important Features:")
for i, row in feature_importance.head(3).iterrows():
    print(f"   {i+1}. {row['feature']}: {row['importance']:.4f}")
print(f"\n✓ Output files in: output_visual_real/")
print("=" * 80)
