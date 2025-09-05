"""
Data Downloader for Healthcare Analysis Project
Downloads sample healthcare datasets for analysis
"""

import pandas as pd
import numpy as np
import requests
import io
import os

def download_diabetes_data():
    """Download diabetes dataset from UCI ML Repository"""
    print("📥 Downloading diabetes dataset...")
    
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv"
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
               'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), names=columns)
        df.to_csv('diabetes.csv', index=False)
        print(f"✅ Diabetes dataset downloaded successfully! Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Error downloading diabetes dataset: {e}")
        return None

def download_heart_disease_data():
    """Download heart disease dataset from UCI ML Repository"""
    print("📥 Downloading heart disease dataset...")
    
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
    columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
               'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text), names=columns)
        
        # Clean the data - replace '?' with NaN
        df = df.replace('?', np.nan)
        
        # Convert numeric columns
        numeric_columns = ['age', 'trestbps', 'chol', 'fbs', 'restecg', 
                          'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df.to_csv('heart_disease.csv', index=False)
        print(f"✅ Heart disease dataset downloaded successfully! Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Error downloading heart disease dataset: {e}")
        return None

def create_sample_data():
    """Create sample healthcare data if downloads fail"""
    print("📊 Creating sample healthcare data...")
    
    np.random.seed(42)
    n_samples = 1000
    
    # Generate sample diabetes data
    diabetes_data = {
        'Pregnancies': np.random.poisson(3, n_samples),
        'Glucose': np.random.normal(120, 30, n_samples),
        'BloodPressure': np.random.normal(80, 15, n_samples),
        'SkinThickness': np.random.normal(25, 10, n_samples),
        'Insulin': np.random.normal(150, 100, n_samples),
        'BMI': np.random.normal(30, 8, n_samples),
        'DiabetesPedigreeFunction': np.random.exponential(0.5, n_samples),
        'Age': np.random.randint(20, 80, n_samples),
        'Outcome': np.random.binomial(1, 0.35, n_samples)
    }
    
    # Ensure realistic ranges
    diabetes_data['Glucose'] = np.clip(diabetes_data['Glucose'], 50, 300)
    diabetes_data['BloodPressure'] = np.clip(diabetes_data['BloodPressure'], 50, 120)
    diabetes_data['BMI'] = np.clip(diabetes_data['BMI'], 15, 50)
    diabetes_data['SkinThickness'] = np.clip(diabetes_data['SkinThickness'], 0, 50)
    diabetes_data['Insulin'] = np.clip(diabetes_data['Insulin'], 0, 500)
    
    df_diabetes = pd.DataFrame(diabetes_data)
    df_diabetes.to_csv('diabetes.csv', index=False)
    print(f"✅ Sample diabetes dataset created! Shape: {df_diabetes.shape}")
    
    return df_diabetes

if __name__ == "__main__":
    print("🏥 Healthcare Data Downloader")
    print("=" * 40)
    
    # Try to download real datasets
    diabetes_df = download_diabetes_data()
    heart_df = download_heart_disease_data()
    
    # If downloads fail, create sample data
    if diabetes_df is None:
        diabetes_df = create_sample_data()
    
    print("\n📋 Available datasets:")
    if os.path.exists('diabetes.csv'):
        df = pd.read_csv('diabetes.csv')
        print(f"• diabetes.csv: {df.shape[0]} records, {df.shape[1]} features")
    
    if os.path.exists('heart_disease.csv'):
        df = pd.read_csv('heart_disease.csv')
        print(f"• heart_disease.csv: {df.shape[0]} records, {df.shape[1]} features")
    
    print("\n✅ Data preparation complete! You can now run the analysis.")
