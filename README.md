# 🏥 Healthcare Data Analysis - Understanding Disease Risk

A comprehensive data analytics project that analyzes healthcare datasets to understand disease risk factors and build interactive visualizations.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://healthcare-data-analysis.streamlit.app)

**Try the interactive dashboard:** [https://healthcare-data-analysis.streamlit.app](https://healthcare-data-analysis-b9azjtfrpoweatk3fts8pp.streamlit.app/)

### Quick Demo Features
- 📊 **Real-time Data Exploration**: Filter by age, gender, and other factors
- 📈 **Interactive Visualizations**: Distribution plots, correlation heatmaps, risk analysis
- 🔍 **Risk Factor Analysis**: Identify key health indicators for disease prediction
- 📋 **Data Export**: Download filtered datasets for further analysis

## 🎯 Project Goals

- Analyze health datasets (diabetes, heart disease) to identify risk factors
- Perform comprehensive data cleaning and exploratory data analysis (EDA)
- Build interactive visualizations to understand health trends
- Create a Streamlit dashboard for real-time data exploration
- Provide actionable insights about disease risk factors

## 🛠️ Tech Stack

- **Python 3.8+**
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Dashboard**: Streamlit
- **Machine Learning**: Scikit-learn
- **Notebook**: Jupyter

## 📊 Features

### 1. Data Preprocessing
- ✅ Handle missing values, duplicates, and outliers
- ✅ Data type optimization and memory efficiency
- ✅ Automated data cleaning pipeline

### 2. Exploratory Data Analysis (EDA)
- ✅ Statistical summaries and data profiling
- ✅ Distribution analysis of health features
- ✅ Correlation analysis and heatmaps
- ✅ Outlier detection and visualization
- ✅ Age group and demographic analysis

### 3. Risk Factor Analysis
- ✅ Identify key risk factors for disease
- ✅ Statistical significance testing
- ✅ Feature importance ranking
- ✅ Risk factor correlation analysis

### 4. Interactive Dashboard
- ✅ Real-time data filtering and exploration
- ✅ Interactive visualizations
- ✅ Risk factor analysis tools
- ✅ Data export functionality

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download the project
cd "Healthcare Data Analysis"

# Install dependencies
pip install -r requirements.txt
```

### 2. Download Sample Data

```bash
# Download sample healthcare datasets
python download_data.py
```

### 3. Run the Analysis

#### Option A: Jupyter Notebook
```bash
# Start Jupyter notebook
jupyter notebook healthcare_analysis.ipynb
```

#### Option B: Streamlit Dashboard
```bash
# Launch interactive dashboard
streamlit run app.py
```

#### Option C: Live Demo (No Installation Required)

Visit the live demo at: [https://healthcare-data-analysis.streamlit.app](https://healthcare-data-analysis.streamlit.app)

## 📁 Project Structure

```
Healthcare Data Analysis/
├── app.py                          # Streamlit dashboard
├── healthcare_analysis.ipynb       # Jupyter notebook analysis
├── download_data.py                # Data downloader script
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── diabetes.csv                    # Diabetes dataset (downloaded)
└── heart_disease.csv              # Heart disease dataset (downloaded)
```

## 📈 Dataset Information

### Diabetes Dataset
- **Source**: UCI ML Repository (Pima Indians Diabetes)
- **Records**: 768
- **Features**: 8 health indicators + outcome
- **Target**: Binary (0 = No Diabetes, 1 = Diabetes)

**Features:**
- Pregnancies: Number of pregnancies
- Glucose: Plasma glucose concentration
- BloodPressure: Diastolic blood pressure
- SkinThickness: Triceps skin fold thickness
- Insulin: 2-Hour serum insulin
- BMI: Body mass index
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age in years

### Heart Disease Dataset
- **Source**: UCI ML Repository (Cleveland Heart Disease)
- **Records**: 303
- **Features**: 13 health indicators + target
- **Target**: Binary (0 = No Heart Disease, 1 = Heart Disease)

## 🔍 Analysis Features

### Data Preprocessing
- Missing value imputation using median/mode
- Duplicate record removal
- Outlier detection and capping using IQR method
- Data type optimization for memory efficiency

### Exploratory Data Analysis
- **Distribution Analysis**: Histograms and density plots
- **Correlation Analysis**: Heatmaps and correlation matrices
- **Statistical Summaries**: Mean, median, standard deviation
- **Outlier Detection**: Box plots and statistical methods
- **Demographic Analysis**: Age groups, gender distributions

### Risk Factor Analysis
- **Feature Importance**: Random Forest feature ranking
- **Correlation Analysis**: Risk factor correlations with disease
- **Statistical Testing**: Significance tests for risk factors
- **Comparative Analysis**: Disease vs non-disease groups

### Interactive Dashboard
- **Data Overview**: Dataset statistics and information
- **Visual Insights**: Interactive plots and charts
- **Risk Analysis**: Risk factor identification and analysis
- **Data Explorer**: Interactive data table with filtering

## 📊 Key Insights

### Diabetes Risk Factors (Typical Findings)
1. **Glucose Level**: Strongest predictor of diabetes
2. **BMI**: Higher BMI increases diabetes risk
3. **Age**: Risk increases with age
4. **Insulin**: Abnormal insulin levels indicate risk
5. **Blood Pressure**: Hypertension correlates with diabetes

### Heart Disease Risk Factors (Typical Findings)
1. **Age**: Risk increases significantly with age
2. **Cholesterol**: High cholesterol levels
3. **Blood Pressure**: Hypertension is a major risk factor
4. **Exercise**: Lack of exercise increases risk
5. **Gender**: Males generally at higher risk

## 🎨 Dashboard Features

### Tab 1: Dataset Overview
- Dataset statistics and information
- Data quality metrics
- Basic statistical summaries
- Data type information

### Tab 2: Visual Insights
- Feature distribution plots
- Correlation heatmaps
- Outlier detection visualizations
- Interactive filtering options

### Tab 3: Risk Analysis
- Risk factor identification
- Feature importance ranking
- Comparative analysis by disease status
- Statistical significance testing

### Tab 4: Data Explorer
- Interactive data table
- Search and filter functionality
- Data export options
- Real-time data exploration

## 🔧 Customization

### Adding New Datasets
1. Place your dataset in the project directory
2. Update the `load_data()` function in `app.py`
3. Modify column mappings if needed
4. Run the analysis with your dataset

### Modifying Visualizations
- Edit the plotting functions in the notebook
- Customize colors and styles in `app.py`
- Add new chart types using Plotly/Matplotlib

### Extending Analysis
- Add new statistical tests
- Implement additional ML models
- Create new risk factor calculations
- Add more demographic breakdowns

## 📚 Dependencies

```
pandas==2.1.4
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
streamlit==1.28.1
plotly==5.17.0
scikit-learn==1.3.2
jupyter==1.0.0
openpyxl==3.1.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the error messages
3. Ensure all dependencies are installed
4. Verify dataset format and location

## 🔮 Future Enhancements

- [ ] Add more healthcare datasets
- [ ] Implement advanced ML models
- [ ] Add predictive modeling capabilities
- [ ] Create automated report generation
- [ ] Add real-time data integration
- [ ] Implement user authentication
- [ ] Add data validation tools

---

**Happy Analyzing! 🏥📊**
