import streamlit as st
import pandas as pd
import plotly.express as px
from random_data import generate_random_galaxy_data, generate_random_cmb_data

# Set up the page title
st.title("Enhanced Cosmology Dashboard 🌌")
st.write("Explore enhanced visualizations for galaxy distribution and CMB radiation.")

# Load random datasets
galaxy_data = generate_random_galaxy_data()
cmb_data = generate_random_cmb_data()

# Sidebar for user controls
st.sidebar.header("Select Data Layers")
show_galaxies = st.sidebar.checkbox("Show Galaxy Distribution", value=True)
show_cmb = st.sidebar.checkbox("Show CMB Radiation", value=True)

# Enhanced Galaxy Distribution Plot
if show_galaxies:
    st.subheader("Galaxy Distribution with Enhanced Visuals")
    st.write("This plot shows galaxies with color indicating redshift (distance from Earth).")
    fig_galaxy = px.scatter(
        galaxy_data,
        x="RA",
        y="Dec",
        color="Redshift",
        color_continuous_scale="Plasma",
        hover_data=["Galaxy_ID", "Redshift"],
        title="Enhanced Random Galaxy Distribution",
        labels={"RA": "Right Ascension (Degrees)", "Dec": "Declination (Degrees)", "Redshift": "Redshift"}
    )
    st.plotly_chart(fig_galaxy)

# Enhanced CMB Radiation Plot
if show_cmb:
    st.subheader("CMB Radiation Map with Enhanced Visuals")
    st.write("This plot shows temperature variations in the CMB data with improved color mapping.")
    fig_cmb = px.scatter(
        cmb_data,
        x="Longitude",
        y="Latitude",
        color="Temperature",
        color_continuous_scale="Viridis",
        hover_data=["Temperature"],
        title="Enhanced CMB Temperature Variations",
        labels={"Longitude": "Longitude (Degrees)", "Latitude": "Latitude (Degrees)", "Temperature": "Temperature (µK)"}
    )
    st.plotly_chart(fig_cmb)
