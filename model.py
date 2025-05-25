from sqlalchemy import create_engine, Column, VARCHAR, INTEGER, DATE, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT, LONGTEXT
from sqlalchemy.orm import declarative_base
from app.general_functions import generate_db_string

DATABASE_URL = generate_db_string()

# Define the database engine
engine = create_engine(DATABASE_URL)

# Define the base class for ORM models
Base = declarative_base()


# Define the ORM model, same order as the init.sql


# tables without foreign keys
class Series(Base):
    """Class for the Series table ferom BookDB"""

    __tablename__ = "Series"

    ID = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR)
    Description = Column(LONGTEXT)


class User(Base):
    """Class for the User table from BookDB"""

    __tablename__ = "User"

    ID = Column(INTEGER, primary_key=True)
    Username = Column(VARCHAR)
    FirstName = Column(VARCHAR)
    FamilyNamePreposition = Column(VARCHAR)
    LastName = Column(VARCHAR)


class BookType(Base):
    """Class for the BookType table from BookDB"""

    __tablename__ = "Booktype"

    ID = Column(INTEGER, primary_key=True)
    Type = Column(VARCHAR)
    Description = Column(VARCHAR)


class Language(Base):
    """Class for the Language table from BookDB"""

    __tablename__ = "Language"

    ID = Column(INTEGER, primary_key=True)
    Language = Column(VARCHAR)


class Genre(Base):
    """Class for the Genre table from BookDB"""

    __tablename__ = "Genre"

    ID = Column(INTEGER, primary_key=True)
    Genre = Column(VARCHAR)
    Description = Column(VARCHAR)


class Role(Base):
    """Class for the Role table from BookDB"""

    __tablename__ = "Role"

    ID = Column(INTEGER, primary_key=True)
    Role = Column(VARCHAR)
    Description = Column(VARCHAR)


class Rating(Base):
    """Class for the Rating table from BookDB"""

    __tablename__ = "Rating"

    ID = Column(INTEGER, primary_key=True)
    Rating = Column(INTEGER)
    Description = Column(VARCHAR)


class Shelf(Base):
    """Class for the Shelf table from BookDB"""

    __tablename__ = "Shelf"

    ID = Column(INTEGER, primary_key=True)
    Shelf = Column(VARCHAR)
    Description = Column(VARCHAR)


class Publisher(Base):
    """Class for the Publisher table from BookDB"""

    __tablename__ = "Publisher"

    ID = Column(INTEGER, primary_key=True)
    Name = Column(VARCHAR)
    Country = Column(VARCHAR)


class Creator(Base):
    """Class for the Creator table from BookDB"""

    __tablename__ = "Creator"

    ID = Column(INTEGER, primary_key=True)
    FirstName = Column(VARCHAR)
    FamilyNamePreposition = Column(VARCHAR)
    LastName = Column(VARCHAR)
    Nationality = Column(VARCHAR)
    Birthday = Column(DATE)
    Pseudonym = Column(TINYINT)
    RealFirstName = Column(VARCHAR)
    RealFamilyNamePreposition = Column(VARCHAR)
    RealLastName = Column(VARCHAR)


# Tables with foreign keys


class Book(Base):

    __tablename__ = "Book"

    ID = Column(INTEGER, primary_key=True)
    ISBN = Column(VARCHAR)
    Title = Column(VARCHAR)
    Subtitle = Column(VARCHAR)
    Description = Column(LONGTEXT)
    OriginalPublicationDate = Column(DATE)
    EditionPublicationDate = Column(DATE)
    EditionLanguageID = Column(INTEGER, ForeignKey("Language.ID"))
    OriginalLanguageID = Column(INTEGER, ForeignKey("Language.ID"))
    PublisherID = Column(INTEGER, ForeignKey("Publisher.ID"))
    NumberOfPages = Column(INTEGER)
    BookTypeID = Column(INTEGER, ForeignKey("BookType.ID"))


class Book_Genre(Base):

    __tablename__ = "Book_Genre"

    ID = Column(INTEGER, primary_key=True)
    BookID = Column(INTEGER, ForeignKey("Book.ID"))
    GenreID = Column(INTEGER, ForeignKey("Genre.ID"))


class Book_Series(Base):

    __tablename__ = "Book_Series"

    ID = Column(INTEGER, primary_key=True)
    BookID = Column(INTEGER, ForeignKey("Book.ID"))
    SeriesID = Column(INTEGER, ForeignKey("Series.ID"))
    Entry = Column(INTEGER)


# Create the table in the database
Base.metadata.create_all(engine)
