import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 1000

data = {
    'CustomerID': [f'CUST{i:04d}' for i in range(1, n_samples + 1)],
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Age': np.random.randint(18, 65, n_samples),
    'Subscription_Type': np.random.choice(['Prepaid', 'Postpaid'], n_samples),
    'Monthly_Bill': np.round(np.random.uniform(50000, 200000, n_samples), 2),
    'Total_Usage_Minutes': np.random.randint(50, 1000, n_samples),
    'Customer_Service_Calls': np.random.randint(0, 6, n_samples),
    'Past_Due_Days': np.random.randint(0, 30, n_samples),
}

df = pd.DataFrame(data)

# Logika untuk membuat variabel Churn realistis berdasarkan probabilitas fitur lainnya
churn_prob = (df['Customer_Service_Calls'] * 0.1) + (df['Past_Due_Days'] * 0.02) - (df['Total_Usage_Minutes'] * 0.0001)
churn_prob = np.clip(churn_prob, 0, 1)

df['Churn_Status'] = [np.random.choice(['Yes', 'No'], p=[prob, 1-prob]) if prob > 0.5 else np.random.choice(['Yes', 'No'], p=[0.1, 0.9]) for prob in churn_prob]

df.to_csv('telecom_churn.csv', index=False)
print(f"Dataset telecom_churn.csv berhasil dibuat dengan {n_samples} baris.")
