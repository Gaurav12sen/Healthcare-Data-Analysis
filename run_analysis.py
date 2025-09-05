"""
Healthcare Data Analysis - Quick Start Script
Run this script to quickly start the analysis
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if all requirements are installed"""
    print("🔍 Checking requirements...")
    
    try:
        import pandas
        import numpy
        import matplotlib
        import seaborn
        import streamlit
        import plotly
        import sklearn
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_datasets():
    """Check if datasets are available"""
    print("\n📊 Checking datasets...")
    
    datasets = ['diabetes.csv', 'heart_disease.csv']
    available = []
    
    for dataset in datasets:
        if os.path.exists(dataset):
            print(f"✅ {dataset} found")
            available.append(dataset)
        else:
            print(f"❌ {dataset} not found")
    
    if not available:
        print("\n📥 Downloading datasets...")
        try:
            subprocess.run([sys.executable, 'download_data.py'], check=True)
            print("✅ Datasets downloaded successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to download datasets")
            return False
    
    return len(available) > 0

def show_menu():
    """Show the main menu"""
    print("\n🏥 Healthcare Data Analysis - Main Menu")
    print("=" * 50)
    print("1. 📊 Run Jupyter Notebook Analysis")
    print("2. 🌐 Launch Streamlit Dashboard")
    print("3. 🧪 Run Test Suite")
    print("4. 📋 Show Project Info")
    print("5. ❌ Exit")
    print("=" * 50)

def run_jupyter():
    """Launch Jupyter notebook"""
    print("\n📊 Launching Jupyter Notebook...")
    try:
        subprocess.run(['jupyter', 'notebook', 'healthcare_analysis.ipynb'])
    except FileNotFoundError:
        print("❌ Jupyter not found. Please install it first:")
        print("pip install jupyter")
    except Exception as e:
        print(f"❌ Error launching Jupyter: {e}")

def run_streamlit():
    """Launch Streamlit dashboard"""
    print("\n🌐 Launching Streamlit Dashboard...")
    try:
        subprocess.run(['streamlit', 'run', 'app.py'])
    except FileNotFoundError:
        print("❌ Streamlit not found. Please install it first:")
        print("pip install streamlit")
    except Exception as e:
        print(f"❌ Error launching Streamlit: {e}")

def run_tests():
    """Run test suite"""
    print("\n🧪 Running Test Suite...")
    try:
        subprocess.run([sys.executable, 'test_setup.py'])
    except Exception as e:
        print(f"❌ Error running tests: {e}")

def show_info():
    """Show project information"""
    print("\n📋 Project Information")
    print("=" * 30)
    print("🏥 Healthcare Data Analysis - Understanding Disease Risk")
    print("\n📁 Project Structure:")
    
    files = [
        ("app.py", "Streamlit dashboard"),
        ("healthcare_analysis.ipynb", "Jupyter notebook analysis"),
        ("download_data.py", "Data downloader script"),
        ("test_setup.py", "Test suite"),
        ("requirements.txt", "Python dependencies"),
        ("README.md", "Project documentation"),
        ("diabetes.csv", "Diabetes dataset"),
        ("heart_disease.csv", "Heart disease dataset")
    ]
    
    for filename, description in files:
        status = "✅" if os.path.exists(filename) else "❌"
        print(f"  {status} {filename:<25} - {description}")
    
    print(f"\n📊 Available Datasets:")
    if os.path.exists('diabetes.csv'):
        import pandas as pd
        df = pd.read_csv('diabetes.csv')
        print(f"  • diabetes.csv: {df.shape[0]} records, {df.shape[1]} features")
    
    if os.path.exists('heart_disease.csv'):
        import pandas as pd
        df = pd.read_csv('heart_disease.csv')
        print(f"  • heart_disease.csv: {df.shape[0]} records, {df.shape[1]} features")
    
    print(f"\n🚀 Quick Start:")
    print("  1. Run this script and choose option 1 for Jupyter analysis")
    print("  2. Or choose option 2 for interactive Streamlit dashboard")
    print("  3. Check README.md for detailed documentation")

def main():
    """Main function"""
    print("🏥 Healthcare Data Analysis - Quick Start")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Check datasets
    if not check_datasets():
        print("❌ Cannot proceed without datasets")
        return
    
    print("\n✅ Setup complete! Ready to analyze healthcare data.")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                run_jupyter()
            elif choice == '2':
                run_streamlit()
            elif choice == '3':
                run_tests()
            elif choice == '4':
                show_info()
            elif choice == '5':
                print("\n👋 Goodbye! Happy analyzing!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Happy analyzing!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
