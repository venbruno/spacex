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
    'https://api.spacexdata.com/v4/rockets'
    ]

# Extract data for a specific endpoint.
def endpoint_data(endpoint_name):

    endpoint_data = data_extraction(api_endpoints)[endpoint_name]

    return endpoint_data

# Define raw data for Launches.
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

# pprint(launches_dataset)

# Define raw data for Rockets.
rockets_raw_data = endpoint_data('rockets')

# Transform Rockets data.
def rockets_data(rockets_raw_data):

    rockets_data_transformed = []

    for d in rockets_raw_data:
        
        rockets_dataset = {
            "rocket_id" : d['id'],
            "rocket_name" : d['name'],
            "is_active" : d['active'],
            "cost_per_launch" : d['cost_per_launch'],
            "diameter_meters" : d['diameter']['meters'],
            "height_meters" : d['height']['meters'],
            "mass_kg" : d['mass']['kg'],
            "engine_type" : d['engines']['type'],
            "first_flight_date" : d['first_flight'],
            "rocket_wikipedia_url" : d['wikipedia']
        }

        rockets_data_transformed.append(rockets_dataset)
    
    return rockets_data_transformed

rockets_dataset = rockets_data(rockets_raw_data)

pprint(rockets_dataset)