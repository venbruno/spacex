from pprint import pprint

from extract.extract import endpoint_data
from transform.transform import transform_data

if __name__ == "__main__":
    
    # Extracting data from endpoints.
    launches, rockets = endpoint_data()

    # Transforming data.
    transformed_launches, transformed_rockets = transform_data(launches, rockets)

    pprint(transformed_rockets)