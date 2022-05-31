
def insert_rockets_data(transformed_rockets):

    rockets_insert_string = 'INSERT INTO {} '.format('rockets')

    # Grab the first potential Postgres record.
    if type(transformed_rockets) == list:
        first_record = transformed_rockets[0]

    # Retrieve column names.
    columns = list(first_record.keys())

    rockets_insert_string += "(" + ', '.join(columns) + ")\nVALUES "

    # Enumerate over the record.
    for i, record_dict in enumerate(transformed_rockets):

        # Iterate over the values of each record dict object
        values = []
        for col_names, val in record_dict.items():

            # Postgres strings must be enclosed with single quotes.
            if type(val) == str:
                # Escape apostrophies with two single quotations.
                val = val.replace("'", "''")
                val = "'" + val + "'"

            values += [ str(val) ]

        # Join the list of values and enclose record in parenthesis
        rockets_insert_string += "(" + ', '.join(values) + "),\n"

    # Remove the last comma and end statement with a semicolon
    rockets_insert_string = rockets_insert_string[:-2] + ";"

    return rockets_insert_string


def insert_launches_data(transformed_launches):

    launches_insert_string = 'INSERT INTO {} '.format('rocket_launches')

    if type(transformed_launches) == list:
        first_record = transformed_launches[0]

    columns = list(first_record.keys())

    launches_insert_string += "(" + ', '.join(columns) + ")\nVALUES "

    for i, record_dict in enumerate(transformed_launches):

        values = []
        for col_names, val in record_dict.items():

            if type(val) == str:
                val = val.replace("'", "''")
                val = "'" + val + "'"

            values += [ str(val) ]

        launches_insert_string += "(" + ', '.join(values) + "),\n"

    launches_insert_string = launches_insert_string[:-2] + ";"

    return launches_insert_string

def insert_data(transformed_launches, transformed_rockets):

    insert_launches = insert_launches_data(transformed_launches)

    insert_rockets = insert_rockets_data(transformed_rockets)

    return insert_launches, insert_rockets