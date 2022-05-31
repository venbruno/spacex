from pprint import pprint

from extract.extract import endpoint_data
from transform.transform import transform_data
from load.load import insert_data

if __name__ == "__main__":
    
    # Extracting data from endpoints.
    launches, rockets = endpoint_data()

    # Transforming data.
    transformed_launches, transformed_rockets = transform_data(launches, rockets)

    # Inserting data into tables.
    insert_launches, insert_rockets = insert_data(transformed_launches, transformed_rockets)

pprint(insert_launches)