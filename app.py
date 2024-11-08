import streamlit as st
import pandas as pd

# URL of the CSV file in your GitHub repository (use the raw link)
url = "https://raw.githubusercontent.com/your-username/simple_cosmology_dashboard/main/data/your-file-name.csv"

# Load the CSV file into a DataFrame
try:
    data = pd.read_csv(url)
    st.success("Successfully loaded the data!")
except Exception as e:
    st.error(f"Failed to load the data: {e}")

# Display the first few rows of the CSV file
st.write("Preview of the Data:")
st.dataframe(data.head())
