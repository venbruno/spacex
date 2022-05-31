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

# Transform data for all endpoints.
def transform_data(launches, rockets):

    transformed_launches = launches_data(launches)

    transformed_rockets = rockets_data(rockets)

    return transformed_launches, transformed_rockets