import pytest
from sqlalchemy.exc import OperationalError

from tests.database.model import Base
from tests.database.model.user import User  # must be imported for Base import to work
from tests.database.model.address import Address  # must be imported for Base import to work


class TestExecute:
    def test_create_new_table(self, operator):
        sql = """CREATE TABLE test_table_2 (x int, y int)"""
        non_column_non_table_placeholders = []
        operator.execute(sql, non_column_non_table_placeholders)
        assert "test_table_2" in operator.get_tables()

    def test_create_existing_table(self, operator):
        sql = """CREATE TABLE test_table (x int, y int)"""
        non_column_non_table_placeholders = []
        with pytest.raises(OperationalError):
            operator.execute(sql, non_column_non_table_placeholders)

    def test_single_insert_into(self, operator):
        sql = "INSERT INTO test_table (x, y) VALUES (:x, :y)"
        non_column_non_table_placeholders = [{"x": 1, "y": 2}]
        operator.execute(sql, non_column_non_table_placeholders)
        assert (1, 2) in operator.execute("SELECT x, y FROM test_table", []).all()

    def test_many_insert_into(self, operator):
        sql = "INSERT INTO test_table (x, y) VALUES (:x, :y)"
        non_column_non_table_placeholders = [{"x": 3, "y": 4}, {"x": 5, "y": 6}]
        operator.execute(sql, non_column_non_table_placeholders)
        rows = operator.execute("SELECT x, y FROM test_table", []).all()
        assert (3, 4) in rows
        assert (5, 6) in rows

    # def test_select(self, operator):
    #     sql = None
    #     non_column_non_table_placeholders = []
    #     assert operator.execute(sql, non_column_non_table_placeholders) == None


class TestCreateAllTables:
    def test_with_metadata(self, operator, metadata):
        operator.create_all_tables(metadata)
        assert "user_account" in operator.get_tables()
        assert "address" in operator.get_tables()
        operator.drop_all_tables(metadata)

    def test_with_registry(self, operator):
        """
        ToDo Special imports are required for this test to pass!
        """
        operator.create_all_tables(Base.metadata)
        assert "user_account_2" in operator.get_tables()
        assert "address_2" in operator.get_tables()
        operator.drop_all_tables(Base.metadata)


class TestGetTables:
    def test_get_tables(self, operator):
        assert "test_table" in operator.get_tables()


class TestGetTableColumns:
    def test_get_not_table_columns(self, operator):
        table = "nothing"
        assert operator.get_table_columns(table) == []


class TestGetAlchemyVersion:
    def test_get_alchemy_version(self, operator):
        assert operator.get_alchemy_version() == "1.4.22"
