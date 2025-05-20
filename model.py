from sqlalchemy import create_engine, Column, VARCHAR, INTEGER
from sqlalchemy.orm import declarative_base
from app.general_functions import generate_db_string

DATABASE_URL = generate_db_string()

# Define the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for ORM models
Base = declarative_base()


# Define the ORM model
class User(Base):
    """Class for the user table from BookDB"""

    __tablename__ = "user"

    ID = Column(INTEGER, primary_key=True)
    Username = Column(VARCHAR)
    FirstName = Column(VARCHAR)
    FamilyNamePreposition = Column(VARCHAR)
    LastName = Column(VARCHAR)


# Create the table in the database
Base.metadata.create_all(engine)
