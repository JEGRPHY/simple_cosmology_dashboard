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
import plotly.express as px

# Scatter plot of the data
st.subheader("Galaxy Distribution Scatter Plot")
fig = px.scatter(
    data,
    x="RA",
    y="Dec",
    color="Redshift",
    color_continuous_scale="Viridis",
    hover_data=["Galaxy_ID", "Redshift"],
    title="Galaxy Distribution with Redshift Coloring",
    labels={"RA": "Right Ascension (Degrees)", "Dec": "Declination (Degrees)", "Redshift": "Redshift"}
)
st.plotly_chart(fig)
