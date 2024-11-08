import streamlit as st
import pandas as pd
import plotly.express as px
from random_data import generate_random_galaxy_data, generate_random_cmb_data

# Page title and introduction
st.title("Simple Cosmology Dashboard 🌌")
st.write("Explore random datasets for galaxy distribution and CMB radiation.")

# Generate random datasets
galaxy_data = generate_random_galaxy_data()
cmb_data = generate_random_cmb_data()

# Sidebar for user controls
st.sidebar.header("Select Data Layers")
show_galaxies = st.sidebar.checkbox("Show Galaxy Distribution", value=True)
show_cmb = st.sidebar.checkbox("Show CMB Radiation", value=True)

# Display Galaxy Distribution
if show_galaxies:
    st.subheader("Galaxy Distribution")
    st.write("This scatter plot shows random galaxies with Right Ascension (RA), Declination (Dec), and Redshift.")
    fig_galaxy = px.scatter(
        galaxy_data,
        x="RA",
        y="Dec",
        color="Redshift",
        color_continuous_scale="Viridis",
        title="Random Galaxy Distribution",
        labels={"RA": "Right Ascension (Degrees)", "Dec": "Declination (Degrees)", "Redshift": "Redshift"}
    )
    st.plotly_chart(fig_galaxy)

# Display CMB Radiation Data
if show_cmb:
    st.subheader("CMB Radiation Map")
    st.write("This scatter plot shows random temperature variations in the Cosmic Microwave Background (CMB).")
    fig_cmb = px.scatter(
        cmb_data,
        x="Longitude",
        y="Latitude",
        color="Temperature",
        color_continuous_scale="Cividis",
        title="Random CMB Temperature Variations",
        labels={"Longitude": "Longitude (Degrees)", "Latitude": "Latitude (Degrees)", "Temperature": "Temperature (µK)"}
    )
    st.plotly_chart(fig_cmb)

