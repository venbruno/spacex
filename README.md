# Project
<h1 align="center">
    <a href="https://docs.spacexdata.com/">🚀 SpaceX API</a>
</h1>

# Definition of Done
Upload a relational database and create a table containing all SpaceX launches available on the public API and details on the rockets used in each event.
We're going to perform data exploration afterward in the PostgreSQL database.

# Install

```bash
sudo apt install python3.9-distutils libpq-dev python3.9-dev postgresql-server-dev-all

python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
```

## Install on Mac

```bash
brew install python@3.9
brew install postgresql
brew install libpq
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
```

# How do I run my scripts?

- Run Docker desktop
- Start the container in the background (enables connection with the PostgreSQL database):
```bash
docker-compose up
```
- Open new Terminal
- Run scripts, e.g.:
```bash
python3 spacex_tables.py
```