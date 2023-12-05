import json
import requests
import pandas as pd

# File path of the excel file
file_path = '/Users/taoran/Desktop/St Jude/Copy of Data Analyst Dataset.xlsx'

# I hide my API_KEY for safety
API_KEY = ''

# Read the Excel file
df = pd.read_excel(file_path)

# Get the coordinate
coordinates_list = df['Coordinates '].str.strip().tolist()

# Process the coordinates list to remove spaces between latitude and longitude
processed_coordinates_list = [','.join(coord.split(', ')) for coord in coordinates_list]

# Get a list of neighbor from JSON 
neighbor_lst = []

for latlng in processed_coordinates_list:
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlng+'&key='+API_KEY

    neighbor_name = requests.get(url).json()['results'][0]['address_components'][2]['long_name']
    neighbor_lst.append(neighbor_name)

# Add a new column in this data frame
df['neighbor'] = neighbor_lst

# Write this data frame into excel file
df.to_excel(file_path, index=False)

