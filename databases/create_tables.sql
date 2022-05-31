
DROP TABLE IF EXISTS public.rocket_launches ;

 CREATE TABLE public.rocket_launches (
     launch_id VARCHAR(255) PRIMARY KEY NOT NULL,
    launched_at TIMESTAMP,
    flight_number INTEGER,
    launch_name VARCHAR(255),
    rocket_id INTEGER, 
    failure_struct CHARACTER VARYING
    ) ;

DROP TABLE IF EXISTS public.rockets ;

CREATE TABLE public.rockets (
    rocket_id VARCHAR(255) PRIMARY KEY NOT NULL,
    rocket_name VARCHAR(255),
    is_active BOOLEAN,
    engine_type VARCHAR(255),
    first_flight_date DATE,
    diameter_meters INTEGER,
    mass_kg INTEGER,
    cost_per_launch INTEGER,
    height_meters INTEGER,
    rocket_wikipedia_url VARCHAR(255)
    ) ;
