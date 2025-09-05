"""
Test script to verify the healthcare analysis setup
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import warnings

warnings.filterwarnings('ignore')

def test_imports():
    """Test if all required libraries are imported successfully"""
    print("🧪 Testing library imports...")
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
        
        import numpy as np
        print("✅ NumPy imported successfully")
        
        import matplotlib.pyplot as plt
        print("✅ Matplotlib imported successfully")
        
        import seaborn as sns
        print("✅ Seaborn imported successfully")
        
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        import plotly.express as px
        print("✅ Plotly imported successfully")
        
        from sklearn.ensemble import RandomForestClassifier
        print("✅ Scikit-learn imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_loading():
    """Test if datasets can be loaded"""
    print("\n🧪 Testing data loading...")
    
    try:
        # Test diabetes dataset
        df_diabetes = pd.read_csv('diabetes.csv')
        print(f"✅ Diabetes dataset loaded: {df_diabetes.shape}")
        
        # Test heart disease dataset
        df_heart = pd.read_csv('heart_disease.csv')
        print(f"✅ Heart disease dataset loaded: {df_heart.shape}")
        
        return True
    except FileNotFoundError as e:
        print(f"❌ Dataset not found: {e}")
        return False

def test_basic_analysis():
    """Test basic analysis functions"""
    print("\n🧪 Testing basic analysis...")
    
    try:
        # Load diabetes dataset
        df = pd.read_csv('diabetes.csv')
        
        # Test basic statistics
        stats = df.describe()
        print("✅ Basic statistics calculated")
        
        # Test correlation
        corr = df.corr()
        print("✅ Correlation matrix calculated")
        
        # Test visualization
        plt.figure(figsize=(8, 6))
        plt.hist(df['Glucose'], bins=20, alpha=0.7)
        plt.title('Test Histogram')
        plt.close()  # Close to avoid display
        print("✅ Visualization test passed")
        
        return True
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        return False

def test_streamlit_app():
    """Test if Streamlit app can be imported"""
    print("\n🧪 Testing Streamlit app...")
    
    try:
        # This is a basic test - we can't actually run the app in this context
        with open('app.py', 'r') as f:
            content = f.read()
        
        if 'streamlit' in content and 'def main()' in content:
            print("✅ Streamlit app structure looks good")
            return True
        else:
            print("❌ Streamlit app structure issues")
            return False
    except Exception as e:
        print(f"❌ Streamlit app error: {e}")
        return False

def main():
    """Run all tests"""
    print("🏥 Healthcare Analysis Setup Test")
    print("=" * 40)
    
    tests = [
        ("Library Imports", test_imports),
        ("Data Loading", test_data_loading),
        ("Basic Analysis", test_basic_analysis),
        ("Streamlit App", test_streamlit_app)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    print("\n📊 Test Results Summary:")
    print("-" * 30)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! Your healthcare analysis setup is ready.")
        print("\nNext steps:")
        print("1. Run 'jupyter notebook healthcare_analysis.ipynb' for detailed analysis")
        print("2. Run 'streamlit run app.py' for interactive dashboard")
    else:
        print("\n⚠️ Some tests failed. Please check the errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    main()
