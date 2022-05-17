import requests
from pprint import pprint

# Retrieving data from the SpaceX API
def data_extraction(api_endpoints):

    data = {}

    for endpoint in api_endpoints:
        # Data extraction
        response = requests.get(endpoint).json()
        # Naming the structure (e.g. 'launches')
        endpoint_name = endpoint.split("/")[-1]

        data[endpoint_name] = response
    
    return data

# API Endpoints
api_endpoints = [
    'https://api.spacexdata.com/v4/launches',
    'https://api.spacexdata.com/v4/rockets',
    'https://api.spacexdata.com/v4/launches/latest' # To be excluded.
    ]

# Extract data for a specific endpoint.
def endpoint_data(endpoint_name):

    endpoint_data = data_extraction(api_endpoints)[endpoint_name]

    return endpoint_data

# Define raw data for Launches. It may not be necessary (?)
launches_raw_data = endpoint_data('launches')

# Transform Launches data.
def launches_data(launches_raw_data):

    launches_data_transformed = []

    for d in launches_raw_data:
        
        launches_dataset = {
            "launched_at" : d['date_local'],
            "flight_number" : d['flight_number'],
            "launch_id" : d['id'],
            "launch_name" : d['name'],
            "rocket_id" : d['rocket'],
            "failure_struct" : d['failures']
        }

        launches_data_transformed.append(launches_dataset)
    
    return launches_data_transformed

launches_dataset = launches_data(launches_raw_data)

pprint(launches_dataset)

# rockets_raw_data = endpoint_data('rockets')

# latest_raw_data = endpoint_data('latest') # To be excluded.