import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit App
st.title("📊 Data Analytics & Visualization App")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Read the file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Display basic info
    st.subheader("📌 Dataset Overview")
    st.write(df.head())
    st.write("Shape of dataset:", df.shape)
    
    # Data Summary
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())
    
    # Missing values
    st.subheader("⚠️ Missing Values")
    st.write(df.isnull().sum())
    
    # Select columns for visualization
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_cols:
        st.subheader("📈 Data Visualization")
        
        # Histogram
        col_hist = st.selectbox("Select column for histogram", numeric_cols)
        fig, ax = plt.subplots()
        sns.histplot(df[col_hist], bins=30, kde=True, ax=ax)
        st.pyplot(fig)
        
        # Scatter Plot
        col_x = st.selectbox("X-axis for scatter plot", numeric_cols)
        col_y = st.selectbox("Y-axis for scatter plot", numeric_cols)
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax)
        st.pyplot(fig)
        
        # Line Chart
        st.line_chart(df[numeric_cols])
        
        # Correlation Heatmap
        st.subheader("🔗 Correlation Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns found for visualization.")
    
    st.success("✅ Analysis Complete!")
