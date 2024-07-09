import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the data
def load_data(file):
    if file is not None:
        try:
            df = pd.read_csv(file)
        except Exception as e:
            df = pd.read_excel(file)
        return df
    return None

# Function to display basic statistics
def display_statistics(df):
    st.write("## Data Overview")
    st.write(df.head())
    st.write("## Data Statistics")
    st.write(df.describe())

# Function to display visualizations
def display_visualizations(df):
    st.write("## Data Visualizations")
    
    st.write("### Pairplot")
    st.write(sns.pairplot(df))
    st.pyplot()

    st.write("### Correlation Heatmap")
    corr = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, ax=ax)
    st.write(fig)
    st.pyplot()

# Streamlit app main function
def main():
    st.title("Exploratory Data Analysis App")
    
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        
        if df is not None:
            display_statistics(df)
            display_visualizations(df)
        else:
            st.write("Error loading the file. Please upload a CSV or Excel file.")
    else:
        st.write("Please upload a file to get started.")

if __name__ == "__main__":
    main()
