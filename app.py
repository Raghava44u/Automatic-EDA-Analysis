import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from eda_tool.data_loader import load_data
from eda_tool.eda_summary import dataset_summary
from eda_tool.missing_values import plot_missing_values
from eda_tool.visualization import (
    plot_histograms, plot_correlation_matrix, plot_countplots, 
    plot_boxplots, plot_violinplots, plot_pairplot, plot_kde
)

st.title("Automatic EDA Tool")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    
    if df is not None:
        st.subheader("Click Below to Explore the Dataset")

        with st.expander("Show Dataset Shape"):
            st.write(f"Shape: {df.shape}")

        with st.expander("Show Column Names"):
            st.write(f"Columns: {list(df.columns)}")

        with st.expander("Show Missing Values"):
            st.write(df.isnull().sum())

        with st.expander("Show Data Types"):
            st.write(df.dtypes)

        with st.expander("Show Summary Statistics"):
            st.write(df.describe())

        with st.expander("Show Missing Values Heatmap"):
            st.pyplot(plot_missing_values(df))

        with st.expander("Show Feature Distributions (Histogram)"):
            st.pyplot(plot_histograms(df))

        with st.expander("Show Correlation Matrix"):
            st.pyplot(plot_correlation_matrix(df))

        with st.expander("Show Count Plots for Categorical Features"):
            for fig in plot_countplots(df):
                st.pyplot(fig)

        with st.expander("Show Box Plots for Outlier Detection"):
            for fig in plot_boxplots(df):
                st.pyplot(fig)

        with st.expander("Show Violin Plots"):
            for fig in plot_violinplots(df):
                st.pyplot(fig)

        with st.expander("Show Pair Plot (Feature Relationships)"):
            st.pyplot(plot_pairplot(df))

        with st.expander("Show KDE (Density) Plots"):
            for fig in plot_kde(df):
                st.pyplot(fig)

    else:
        st.error("Error while loading the dataset.")
