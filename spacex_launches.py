import requests
from pprint import pprint

# Retrieving data from the SpaceX API
def data_extraction(api_endpoints):

    data = []

    for endpoint in api_endpoints:
        # Data extraction
        response = requests.get(endpoint).json()
        # Naming the structure (e.g. 'launches')
        endpoint_name = endpoint.split("/")[-1]

        dict_ = {endpoint_name : response}

        data.append(dict_)
    
    return data

api_endpoints = [
    'https://api.spacexdata.com/v4/launches/latest'#, For testing
    #'https://api.spacexdata.com/v4/launches',
    #'https://api.spacexdata.com/v4/rockets'
    ]

data = data_extraction(api_endpoints)

launches_set = []

# Building a list for Launches. Not a function yet.
for endpoint_name in data:
    
    if "".join(endpoint_name) == "latest":

        launch = {
            "launched_at" : endpoint_name["latest"]['date_local'],
            "flight_number" : endpoint_name["latest"]['flight_number'],
            "launch_id" : endpoint_name["latest"]['id'],
            "launch_name" : endpoint_name["latest"]['name'],
            "rocket_id" : endpoint_name["latest"]['rocket'],
            "failure_struct" : endpoint_name["latest"]['failures']
            }

    launches_set.append(launch)

print(launches_set)