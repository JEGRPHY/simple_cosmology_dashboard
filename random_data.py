import pandas as pd
import numpy as np

# Function to generate random galaxy data
def generate_random_galaxy_data():
    num_points = 200
    data = {
        "Galaxy_ID": np.arange(num_points),
        "RA": np.random.uniform(0, 360, num_points),  # Right Ascension (0-360 degrees)
        "Dec": np.random.uniform(-90, 90, num_points),  # Declination (-90 to 90 degrees)
        "Redshift": np.random.uniform(0, 3, num_points)  # Redshift values (0 to 3)
    }
    return pd.DataFrame(data)

# Function to generate random CMB temperature data
def generate_random_cmb_data():
    num_points = 200
    data = {
        "Point_ID": np.arange(num_points),
        "Longitude": np.random.uniform(0, 360, num_points),
        "Latitude": np.random.uniform(-90, 90, num_points),
        "Temperature": np.random.uniform(-300, 300, num_points)  # Temperature variation in microkelvin
    }
    return pd.DataFrame(data)

