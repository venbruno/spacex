import requests

# Retrieving data from the SpaceX API
def data_extraction(endpoint):

    # Data extraction
    response = requests.get(endpoint).json()

    return response

# Extract data for specific endpoints.
def endpoint_data():

    launches = data_extraction(endpoint='https://api.spacexdata.com/v4/launches')

    rockets = data_extraction(endpoint='https://api.spacexdata.com/v4/rockets')

    return launches, rockets