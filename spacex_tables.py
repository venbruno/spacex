import psycopg2

def create_tables():

    commands = (

        """
        DROP TABLE IF EXISTS rocket_launches ;

        CREATE TABLE rocket_launches (
            launch_id VARCHAR(255) PRIMARY KEY NOT NULL,
            launched_at TIMESTAMP,
            flight_number INTEGER,
            launch_name VARCHAR(255),
            rocket_id INTEGER, 
            failure_struct CHARACTER VARYING
            )
        """,

        """
        DROP TABLE IF EXISTS rockets ;

        CREATE TABLE rockets (
            rocket_id VARCHAR(255) PRIMARY KEY NOT NULL,
            rocket_name VARCHAR(255),
            is_active BOOLEAN
            engine_type VARCHAR(255),
            first_flight_date DATE,
            diameter_meters INTEGER,
            mass_kg INTEGER,
            cost_per_launch INTEGER,
            height_meters INTEGER,
            rocket_wikipedia_url VARCHAR(255)
            )
        """
    )

    # Establishing the connection with the PosgresSQL database (spacex_database)
    conn = psycopg2.connect(
        database = "POSTGRES_DB",
        user = "POSTGRES_USER",
        password = "POSTGRES_PASSWORD",
        host = "127.0.0.1",
        port = "5432"
    )

    cur = conn.cursor()

    for command in commands:
        cur.execute(command)

    # Commit the changes
    conn.commit()

    # Close the communication with the PostgreSQL database
    cur.close()

if __name__ == '__main__':
    create_tables()