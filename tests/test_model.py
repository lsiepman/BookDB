import unittest

from sqlalchemy import create_engine, inspect, MetaData, Table

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import User
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

    def test_user_table_matches_model(self):
        # Reflect the actual table from the database
        reflected_metadata = MetaData()
        reflected_table = Table("user", reflected_metadata, autoload_with=self.engine)

        # Get the ORM table from model
        model_table = User.__table__

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


if __name__ == "__main__":
    unittest.main()
