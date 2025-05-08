import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# load credentials
with open("credentials.json", "r") as f:
    creds = json.load(f)

db_creds = creds["database"]
# Define the database engine
engine = create_engine(
    f"mariadb+mariadbconnector://{db_creds['user']}:{db_creds['password']}@{db_creds['host']}:{db_creds['port']}/{db_creds['default_database']}"
)
