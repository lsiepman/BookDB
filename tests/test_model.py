import unittest

from sqlalchemy import create_engine, inspect, MetaData, Table

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import (
    Series,
    User,
    BookType,
    Language,
    Genre,
    Role,
    Rating,
    Shelf,
    Publisher,
    Creator,
    Book,
    Book_Genre,
    Book_Creator,
    Book_Series,
    Book_User,
    ReadCount,
)
from app.general_functions import generate_db_string

# Replace with your actual MariaDB connection string
DATABASE_URL = generate_db_string()


class TestDatabaseSchema(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL)
        cls.connection = cls.engine.connect()
        cls.metadata = MetaData()
        cls.inspector = inspect(cls.engine)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        cls.engine.dispose()

    def assert_table_matches(self, table_class, table_name: str):
        # Reflect the actual table from the database
        reflected_metadata = MetaData()
        reflected_table = Table(
            table_name, reflected_metadata, autoload_with=self.engine
        )

        # Get the ORM table from model
        model_table = table_class.__table__

        # Compare column names
        model_columns = {col.name: col for col in model_table.columns}
        reflected_columns = {col.name: col for col in reflected_table.columns}

        self.assertEqual(
            set(model_columns.keys()),
            set(reflected_columns.keys()),
            msg="Column names do not match between ORM and DB.",
        )

        # Optionally compare column types (basic check)
        for name in model_columns:
            model_type = type(model_columns[name].type).__name__
            reflected_type = type(reflected_columns[name].type).__name__

            self.assertEqual(
                model_type,
                reflected_type,
                msg=f"Type mismatch for column '{name}': {model_type} != {reflected_type}",
            )

    def test_series_table_matches_model(self):
        self.assert_table_matches(Series, "Series")

    def test_user_table_matches_model(self):
        self.assert_table_matches(User, "User")

    def test_booktype_table_matches_model(self):
        self.assert_table_matches(BookType, "BookType")

    def test_language_table_matches_model(self):
        self.assert_table_matches(Language, "Language")

    def test_genre_table_matches_model(self):
        self.assert_table_matches(Genre, "Genre")

    def test_role_table_matches_model(self):
        self.assert_table_matches(Role, "Role")

    def test_rating_table_matches_model(self):
        self.assert_table_matches(Rating, "Rating")

    def test_shelf_table_matches_model(self):
        self.assert_table_matches(Shelf, "Shelf")

    def test_publisher_table_matches_model(self):
        self.assert_table_matches(Publisher, "Publisher")

    def test_creator_table_matches_model(self):
        self.assert_table_matches(Creator, "Creator")

    def test_book_table_matches_model(self):
        self.assert_table_matches(Book, "Book")

    def test_readcount_table_matches_model(self):
        self.assert_table_matches(ReadCount, "ReadCount")

    def test_book_genre_table_matches_model(self):
        self.assert_table_matches(Book_Genre, "Book_Genre")

    def test_book_creator_table_matches_model(self):
        self.assert_table_matches(Book_Creator, "Book_Creator")

    def test_book_series_table_matches_model(self):
        self.assert_table_matches(Book_Series, "Book_Series")

    def test_book_user_table_matches_model(self):
        self.assert_table_matches(Book_User, "Book_User")


if __name__ == "__main__":
    unittest.main()
