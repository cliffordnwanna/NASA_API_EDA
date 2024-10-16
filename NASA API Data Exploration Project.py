# -*- coding: utf-8 -*-
"""GOMYCODE CHECKPOINT 27 [API to Pandas Dataframe checkpoint].ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/109qmCzRtyWFu7FpEp4BkIK2sOXTesNtB

Checkpoint Objective
In this checkpoint, I am going to practice consuming public APIs through the NASA public APIs portal.

Portal description : The objective of this portal is to make NASA data, including imagery, eminently accessible to application developers and data professionals. Before starting to use its APIs endpoints, it's mandatory that you generate your API KEY and store it somewhere for later use. The API key acts as the user identifier when requesting the API. To get your KEY, fill in the provided form with your personal information, and then we shall receive an email containing your personal API KEY.

NASA API PORTAL : https://api.nasa.gov/




Instructions
Go to the NASA API portal and generate your API KEY

Import the requests package and store your API KEY in variable

Go back to portal website and click on 'browse APIs'

Click on the first dropdown menu, named 'APOD' and read its documentation

Follow the provided documentation to ask the API endpoint for the astronomy picture of the day. Get then display the image on your notebook.

Go through the list of the provided API endpoints once again and select 'Astronomy Picture of the Day' option. Store the results in a pandas dataframe

Do the necessary data pre-processing tasks on the previous result in order to get a clean dataframe with the following columns :
Asteroid ID
Asteroid name
The Minimal estimated diameter in Kilometre
Absolute_magnitude
Relative_velocity(km/s)

Try to export the new dataframe into a CSV file and share it with your colleagues
"""

import requests #This is how python connects to any website

url = "https://api.nasa.gov/planetary/apod?api_key=GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR" # Give it the url to be connected to

api_key = "GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR" # Most websites have api_keys. you will need to get the api key

response = requests.get(url)
response.json()

from IPython.display import Image, display

# NASA APOD API endpoint
apod_url = "https://api.nasa.gov/planetary/apod"

# Your NASA API key (get yours from: https://api.nasa.gov/)
api_key = "GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR"

# Parameters for the API request
params = {
    "api_key": api_key,
    "hd": True  # Set to True if you want high-resolution images when available
}

try:
    # Sending a GET request to NASA APOD API
    response = requests.get(apod_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting JSON data from the response
        data = response.json()

        # Retrieving the image URL
        image_url = data['url']

        # Displaying the image in the notebook
        display(Image(url=image_url))
    else:
        print(f"Failed to retrieve data. Error: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

"""Sometimes the APOD service returns a video URL instead of an image URL, leading to this error.Let's enhance the code to handle this by checking if the fetched content is an image before attempting to display it.
The code below checks if the media type of the fetched content is an image before attempting to display it. If the media type is not an image, it will print a message indicating that today's APOD is not an image. This should help in handling different types of content that might be returned by the APOD service.

"""

import requests
from PIL import Image
import io
from IPython.display import display

# NASA APOD API endpoint
apod_url = "https://api.nasa.gov/planetary/apod"

# Your NASA API key (get yours from: https://api.nasa.gov/)
api_key = "GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR"

# Parameters for the API request
params = {
    "api_key": api_key,
    "hd": True  # Set to True if you want high-resolution images when available
}

try:
    # Sending a GET request to NASA APOD API
    response = requests.get(apod_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting JSON data from the response
        data = response.json()

        # Check if the media type is an image
        if data['media_type'] == 'image':
            # Retrieving the image URL
            image_url = data['url']

            # Fetching the image data
            image_response = requests.get(image_url)
            image_data = Image.open(io.BytesIO(image_response.content))

            # Displaying the image in the notebook
            display(image_data)
        else:
            print("Today's APOD is not an image. It might be a video or other media.")
    else:
        print(f"Failed to retrieve data. Error: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

"""# Alternatively, we can also use matplotlib library"""

import requests
import matplotlib.pyplot as plt
from PIL import Image
import io

# NASA APOD API endpoint
apod_url = "https://api.nasa.gov/planetary/apod"

# Your NASA API key (get yours from: https://api.nasa.gov/)
api_key = "GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR"

# Parameters for the API request
params = {
    "api_key": api_key,
    "hd": True  # Set to True if you want high-resolution images when available
}

try:
    # Sending a GET request to NASA APOD API
    response = requests.get(apod_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting JSON data from the response
        data = response.json()

        # Check if the media type is an image
        if data['media_type'] == 'image':
            # Retrieving the image URL
            image_url = data['url']

            # Fetching the image data and displaying it using matplotlib
            image_response = requests.get(image_url)
            image_data = Image.open(io.BytesIO(image_response.content))

            plt.imshow(image_data)
            plt.axis('off')  # Turn off axis labels
            plt.show()
        else:
            print("Today's APOD is not an image. It might be a video or other media.")
    else:
        print(f"Failed to retrieve data. Error: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

import pandas as pd
import requests

# NASA NeoWs API endpoint for retrieving Asteroid data
neo_ws_url = "https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR"

# Your NASA API key (get yours from: https://api.nasa.gov/)
api_key = "GZ7c3rxcQfZVr3KV8oAnGd0NlvztT4FVuvq5kxRR"

# Parameters for the API request
params = {
    "api_key": api_key
}

try:
    # Sending a GET request to NASA NeoWs API to fetch asteroid data
    response = requests.get(neo_ws_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extracting JSON data from the response
        data = response.json()

        # Extracting relevant information and storing it in a list
        asteroids_data = []
        for asteroid in data['near_earth_objects']:
            asteroid_id = asteroid['id']
            asteroid_name = asteroid['name']
            min_diameter_km = asteroid['estimated_diameter']['kilometers']['estimated_diameter_min']
            abs_magnitude = asteroid['absolute_magnitude_h']
            relative_velocity = asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second']

            asteroids_data.append({
                'Asteroid ID': asteroid_id,
                'Asteroid name': asteroid_name,
                'Minimal estimated diameter (km)': min_diameter_km,
                'Absolute magnitude': abs_magnitude,
                'Relative velocity (km/s)': relative_velocity
            })

        # Creating a DataFrame from the extracted data
        asteroids_df = pd.DataFrame(asteroids_data)

        print("DataFrame successfully created")
    else:
        print(f"Failed to retrieve data. Error: {response.status_code}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

# Displaying the DataFrame
asteroids_df.head(20)

# exploring the dataframe
asteroids_df.shape

#Exporting the DataFrame to a CSV file

# Save DataFrame as CSV file in the root directory of Google Colab
file_name = 'asteroids_df'
asteroids_df.to_csv(file_name, index=False)

# Check if the file is saved in the root directory
import os
root_path = '/content/'
file_path = os.path.join(root_path, file_name)

# Verify the file existence
if os.path.exists(file_path):
    print(f"File '{file_name}' has been saved in the root directory.")
else:
    print(f"File '{file_name}' was not saved. Please check for errors.")