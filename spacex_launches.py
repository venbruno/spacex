import requests
from pprint import pprint

# Retrieving data from the SpaceX API
response = requests.get('https://api.spacexdata.com/v4/launches')

data = response.json()

launches = []

for index in range(len(data)):

    launch = {
        "launched_at" : data[index]['date_local'],
        "flight_number" : data[index]['flight_number'],
        "launch_id" : data[index]['id'],
        "launch_name" : data[index]['name'],
        "rocket_id" : data[index]['rocket'],
        "failure_struct" : data[index]['failures']
    }

    launches.append(launch)

print(launches)