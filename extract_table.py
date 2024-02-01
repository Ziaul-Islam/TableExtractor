#!/usr/bin/env python3

#Add a shebang line that points to your Python interpreter

import pandas as pd
import requests
import json

# Step 1: Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Step 2: Fetch HTML content using requests
response = requests.get(config['website_url'])

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 3: Extract tables using pandas
    tables = pd.read_html(response.text)

    # Check if there are tables on the page
    if tables:
        # Extract the first table
        first_table = tables[0]

        # Step 4: Save the table to a CSV file
        csv_file_path = config['csv_file_path']
        first_table.to_csv(csv_file_path, index=False)

        print(f'The first table has been extracted and saved to {csv_file_path}.')
    else:
        print('No tables found on the provided website.')
else:
    print(f'Failed to fetch the website. Status Code: {response.status_code}')
