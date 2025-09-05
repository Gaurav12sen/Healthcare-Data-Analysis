import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Healthcare Data Analysis Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    .insight-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ff6b6b;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the healthcare dataset"""
    try:
        # Try to load diabetes dataset first
        df = pd.read_csv('diabetes.csv')
        df['dataset_type'] = 'diabetes'
        return df
    except FileNotFoundError:
        try:
            # Try heart disease dataset
            df = pd.read_csv('heart_disease.csv')
            df['dataset_type'] = 'heart_disease'
            return df
        except FileNotFoundError:
            # Create sample data if no dataset found
            st.warning("No dataset found. Please ensure 'diabetes.csv' or 'heart_disease.csv' is in the project directory.")
            return None

def preprocess_data(df):
    """Clean and preprocess the dataset"""
    if df is None:
        return None
    
    # Create a copy to avoid modifying original
    df_clean = df.copy()
    
    # Handle missing values
    if df_clean.isnull().sum().sum() > 0:
        # For numerical columns, fill with median
        numerical_cols = df_clean.select_dtypes(include=[np.number]).columns
        df_clean[numerical_cols] = df_clean[numerical_cols].fillna(df_clean[numerical_cols].median())
        
        # For categorical columns, fill with mode
        categorical_cols = df_clean.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates()
    
    return df_clean

def create_summary_stats(df):
    """Create summary statistics"""
    if df is None:
        return None
    
    stats = {
        'Total Records': len(df),
        'Total Features': len(df.columns),
        'Missing Values': df.isnull().sum().sum(),
        'Duplicate Records': df.duplicated().sum(),
        'Memory Usage': f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
    }
    return stats

def main():
    st.markdown('<h1 class="main-header">🏥 Healthcare Data Analysis Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Understanding Disease Risk Factors through Data Analysis")
    
    # Load data
    df = load_data()
    
    if df is None:
        st.error("Please add a healthcare dataset (diabetes.csv or heart_disease.csv) to the project directory.")
        return
    
    # Preprocess data
    df_clean = preprocess_data(df)
    
    # Sidebar
    st.sidebar.header("🔧 Dashboard Controls")
    
    # Dataset selection
    if 'dataset_type' in df_clean.columns:
        dataset_type = df_clean['dataset_type'].iloc[0]
        st.sidebar.info(f"📊 Current Dataset: {dataset_type.title()}")
    
    # Filter options
    st.sidebar.subheader("📋 Data Filters")
    
    # Age filter (if age column exists)
    age_columns = [col for col in df_clean.columns if 'age' in col.lower()]
    if age_columns:
        age_col = age_columns[0]
        age_range = st.sidebar.slider(
            f"Select {age_col} range",
            min_value=int(df_clean[age_col].min()),
            max_value=int(df_clean[age_col].max()),
            value=(int(df_clean[age_col].min()), int(df_clean[age_col].max()))
        )
        df_filtered = df_clean[(df_clean[age_col] >= age_range[0]) & (df_clean[age_col] <= age_range[1])]
    else:
        df_filtered = df_clean
    
    # Gender filter (if gender column exists)
    gender_columns = [col for col in df_clean.columns if any(g in col.lower() for g in ['gender', 'sex'])]
    if gender_columns:
        gender_col = gender_columns[0]
        unique_genders = df_clean[gender_col].unique()
        selected_genders = st.sidebar.multiselect(
            f"Select {gender_col}",
            options=unique_genders,
            default=unique_genders
        )
        df_filtered = df_filtered[df_filtered[gender_col].isin(selected_genders)]
    
    # Main content
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Dataset Overview", "📈 Visual Insights", "🔍 Risk Analysis", "📋 Data Explorer"])
    
    with tab1:
        st.header("Dataset Overview")
        
        # Summary statistics
        stats = create_summary_stats(df_filtered)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Records", stats['Total Records'])
        with col2:
            st.metric("Total Features", stats['Total Features'])
        with col3:
            st.metric("Missing Values", stats['Missing Values'])
        with col4:
            st.metric("Memory Usage", stats['Memory Usage'])
        
        # Dataset info
        st.subheader("Dataset Information")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**First 5 rows:**")
            st.dataframe(df_filtered.head())
        
        with col2:
            st.write("**Dataset Info:**")
            info_df = pd.DataFrame({
                'Column': df_filtered.columns,
                'Data Type': df_filtered.dtypes,
                'Non-Null Count': df_filtered.count(),
                'Null Count': df_filtered.isnull().sum()
            })
            st.dataframe(info_df)
        
        # Basic statistics
        st.subheader("Statistical Summary")
        st.dataframe(df_filtered.describe())
    
    with tab2:
        st.header("Visual Insights")
        
        # Distribution plots
        st.subheader("Feature Distributions")
        
        # Select columns for visualization
        numerical_cols = df_filtered.select_dtypes(include=[np.number]).columns
        selected_cols = st.multiselect(
            "Select features to visualize:",
            options=numerical_cols,
            default=numerical_cols[:4] if len(numerical_cols) >= 4 else numerical_cols
        )
        
        if selected_cols:
            # Create subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            axes = axes.ravel()
            
            for i, col in enumerate(selected_cols[:4]):
                if i < len(axes):
                    axes[i].hist(df_filtered[col].dropna(), bins=30, alpha=0.7, color='skyblue', edgecolor='black')
                    axes[i].set_title(f'Distribution of {col}')
                    axes[i].set_xlabel(col)
                    axes[i].set_ylabel('Frequency')
            
            # Hide unused subplots
            for i in range(len(selected_cols), len(axes)):
                axes[i].set_visible(False)
            
            plt.tight_layout()
            st.pyplot(fig)
        
        # Correlation heatmap
        st.subheader("Feature Correlation Heatmap")
        if len(numerical_cols) > 1:
            corr_matrix = df_filtered[numerical_cols].corr()
            
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                       square=True, ax=ax, fmt='.2f')
            ax.set_title('Correlation Matrix of Numerical Features')
            st.pyplot(fig)
        
        # Box plots for outlier detection
        st.subheader("Outlier Detection")
        if selected_cols:
            fig, ax = plt.subplots(figsize=(12, 6))
            df_filtered[selected_cols].boxplot(ax=ax)
            ax.set_title('Box Plots for Outlier Detection')
            ax.set_xticklabels(selected_cols, rotation=45)
            plt.tight_layout()
            st.pyplot(fig)
    
    with tab3:
        st.header("Risk Factor Analysis")
        
        # Find target variable (disease indicator)
        target_columns = [col for col in df_filtered.columns if any(t in col.lower() for t in ['outcome', 'target', 'disease', 'diabetes', 'heart'])]
        
        if target_columns:
            target_col = target_columns[0]
            st.subheader(f"Analysis of {target_col}")
            
            # Risk factor analysis
            numerical_cols = df_filtered.select_dtypes(include=[np.number]).columns
            risk_factors = [col for col in numerical_cols if col != target_col]
            
            if risk_factors:
                # Calculate correlation with target
                correlations = df_filtered[risk_factors + [target_col]].corr()[target_col].drop(target_col).abs().sort_values(ascending=False)
                
                st.write("**Top Risk Factors (by correlation):**")
                fig, ax = plt.subplots(figsize=(10, 6))
                correlations.plot(kind='barh', ax=ax, color='coral')
                ax.set_title('Risk Factor Correlations')
                ax.set_xlabel('Absolute Correlation with Target')
                plt.tight_layout()
                st.pyplot(fig)
                
                # Detailed analysis for top risk factors
                st.subheader("Detailed Risk Factor Analysis")
                top_factors = correlations.head(3).index
                
                for factor in top_factors:
                    st.write(f"**{factor} Analysis:**")
                    
                    # Create comparison plots
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
                    
                    # Distribution by target
                    target_values = df_filtered[target_col].unique()
                    for target_val in target_values:
                        subset = df_filtered[df_filtered[target_col] == target_val]
                        ax1.hist(subset[factor].dropna(), alpha=0.7, 
                                label=f'Target = {target_val}', bins=20)
                    ax1.set_title(f'{factor} Distribution by Target')
                    ax1.set_xlabel(factor)
                    ax1.set_ylabel('Frequency')
                    ax1.legend()
                    
                    # Box plot
                    df_filtered.boxplot(column=factor, by=target_col, ax=ax2)
                    ax2.set_title(f'{factor} by Target')
                    ax2.set_xlabel('Target')
                    ax2.set_ylabel(factor)
                    
                    plt.tight_layout()
                    st.pyplot(fig)
                    
                    # Statistics
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Statistics by Target:**")
                        stats_by_target = df_filtered.groupby(target_col)[factor].describe()
                        st.dataframe(stats_by_target)
                    
                    with col2:
                        st.write("**Risk Insights:**")
                        mean_0 = df_filtered[df_filtered[target_col] == 0][factor].mean()
                        mean_1 = df_filtered[df_filtered[target_col] == 1][factor].mean()
                        diff = mean_1 - mean_0
                        st.write(f"• Average {factor} for non-disease: {mean_0:.2f}")
                        st.write(f"• Average {factor} for disease: {mean_1:.2f}")
                        st.write(f"• Difference: {diff:.2f}")
                        if diff > 0:
                            st.write("• Higher values increase disease risk")
                        else:
                            st.write("• Lower values increase disease risk")
        
        else:
            st.warning("No target variable found for risk analysis. Please ensure your dataset has a column indicating disease presence.")
    
    with tab4:
        st.header("Data Explorer")
        
        # Interactive data table
        st.subheader("Interactive Data Table")
        
        # Search functionality
        search_term = st.text_input("Search in data:", "")
        if search_term:
            # Simple search across all columns
            mask = df_filtered.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
            display_df = df_filtered[mask]
        else:
            display_df = df_filtered
        
        st.dataframe(display_df, use_container_width=True)
        
        # Download option
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="Download filtered data as CSV",
            data=csv,
            file_name=f"healthcare_data_filtered_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
