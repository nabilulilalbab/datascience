import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

def load_and_inspect_data(filepath):
    print("=========================================")
    print(" LANGKAH 1 & 2: MEMUAT DAN INSPEKSI DATA ")
    print("=========================================")
    
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} tidak ditemukan!")
        return None
    
    df = pd.read_csv(filepath)
    print("✅ Data berhasil dimuat.")
    print(f"Bentuk data (Baris, Kolom): {df.shape}")
    return df

def perform_eda(df):
    print("\n=========================================")
    print(" LANGKAH 3: ANALISIS STATISTIKA DESKRIPTIF ")
    print("=========================================")
    
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    print("--- 1. Central Tendency & Spread ---")
    desc = df[num_cols].describe()
    desc.loc['range'] = desc.loc['max'] - desc.loc['min']
    print(desc)
    
    os.makedirs('output_visual', exist_ok=True)
    
    # Histogram
    plt.figure(figsize=(12, 8))
    df[num_cols].hist(bins=20, figsize=(12,8), color='skyblue', edgecolor='black')
    plt.suptitle("Distribusi Fitur Numerik", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('output_visual/histogram_numerik.png')
    plt.close('all')
    print(">> Histogram distribusi fitur numerik disimpan di 'output_visual/histogram_numerik.png'")
    
    # Distribusi Target
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Churn_Status', data=df, hue='Churn_Status', palette='Set2')
    plt.title('Distribusi Status Churn')
    plt.savefig('output_visual/distribusi_churn.png')
    plt.close('all')
    print(">> Bar chart distribusi churn disimpan di 'output_visual/distribusi_churn.png'")
    
    # Heatmap
    df_corr = df.copy()
    df_corr['Churn_Status'] = df_corr['Churn_Status'].map({'Yes': 1, 'No': 0})
    df_corr['Gender'] = df_corr['Gender'].map({'Male': 1, 'Female': 0})
    df_corr['Subscription_Type'] = df_corr['Subscription_Type'].map({'Postpaid': 1, 'Prepaid': 0})
    df_corr = df_corr.drop(columns=['CustomerID'])
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Heatmap Korelasi Fitur")
    plt.tight_layout()
    plt.savefig('output_visual/korelasi_heatmap.png')
    plt.close('all')
    print(">> Heatmap korelasi disimpan di 'output_visual/korelasi_heatmap.png'")

def preprocess_and_split(df):
    print("\n=========================================")
    print(" LANGKAH 4 & 5: PREPROCESSING & SPLIT DATA ")
    print("=========================================")
    
    df_clean = df.copy()
    
    # Drop CustomerID karena tidak ada nilai prediktif
    df_clean = df_clean.drop(columns=['CustomerID'])
    
    # Encoding Variabel Kategorikal
    le = LabelEncoder()
    df_clean['Gender'] = le.fit_transform(df_clean['Gender'])
    df_clean['Subscription_Type'] = le.fit_transform(df_clean['Subscription_Type'])
    df_clean['Churn_Status'] = df_clean['Churn_Status'].map({'Yes': 1, 'No': 0})
    
    print("✅ Encoding selesai (Kategorikal -> Numerik).")
    
    # Split Fitur (X) dan Target (y)
    X = df_clean.drop(columns=['Churn_Status'])
    y = df_clean['Churn_Status']
    
    # Train-Test Split (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"✅ Data di-split (80/20):")
    print(f"   Train data: {X_train.shape[0]} baris")
    print(f"   Test data:  {X_test.shape[0]} baris")
    
    return X_train, X_test, y_train, y_test

def train_and_evaluate(X_train, X_test, y_train, y_test):
    print("\n=========================================")
    print(" LANGKAH 6 & 7: MODELING & EVALUASI MODEL ")
    print("=========================================")
    
    # Membuat model Random Forest (metode Ensemble sesuai Jurnal)
    print("⏳ Melatih model Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)
    print("✅ Model berhasil dilatih.")
    
    # Prediksi
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Evaluasi
    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_proba)
    
    print("\n--- Hasil Evaluasi ---")
    print(f"Accuracy : {acc:.4f} ({(acc*100):.2f}%)")
    print(f"AUC Score: {auc:.4f}")
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    filepath = 'telecom_churn.csv'
    df = load_and_inspect_data(filepath)
    if df is not None:
        perform_eda(df)
        X_train, X_test, y_train, y_test = preprocess_and_split(df)
        train_and_evaluate(X_train, X_test, y_train, y_test)
