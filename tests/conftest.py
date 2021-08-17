# For the fixtures to be found in other files, the file must be called conftest.py!

import pytest
from sqlalchemy import Integer, Column, String, MetaData, ForeignKey, insert

from rapdevpy.database.sql_alchemy_operator import SqlAlchemyOperator
from rapdevpy.database.sql_alchemy_tables import SqlAlchemyTables
from tests import settings
from tests.database.model.address import Address
from tests.database.model.user import User


@pytest.fixture(scope="session")
def primary_column():
    yield Column('id', Integer, primary_key=True)


@pytest.fixture(scope="session")
def temp_tables():
    tables = SqlAlchemyTables(MetaData())
    tables.add_table("user_account_2", Column('id', Integer, primary_key=True), Column('name', String(30)),
                     Column('fullname', String))
    tables.add_table("address_2", Column('id', Integer, primary_key=True),
                     Column('user_id', ForeignKey('user_account_2.id'), nullable=False),
                     Column('email_address', String, nullable=False))
    yield tables


@pytest.fixture(scope="session")
def tables():
    tables = SqlAlchemyTables(MetaData())
    tables.add_table("user_account", Column('id', Integer, primary_key=True), Column('name', String(30)),
                     Column('fullname', String))
    tables.add_table("address", Column('id', Integer, primary_key=True),
                     Column('user_id', ForeignKey('user_account.id'), nullable=False),
                     Column('email_address', String, nullable=False))
    yield tables


@pytest.fixture(scope="session")
def operator(tables):
    with SqlAlchemyOperator(settings.test_in_memory_database) as operator:
        operator.execute_text("CREATE TABLE test_table (x int, y int)", [])
        operator.execute_text("INSERT INTO test_table (x, y) VALUES (:x, :y)", [{"x": 1, "y": 2}])
        operator.create_all_tables(tables.metadata)
        operator.execute_core(insert(User), [{"name": "sandy", "fullname": "Sandy Cheeks"}])
        operator.execute_core(insert(Address), [{"email_address": "sandy@squirrelpower.org", "user_id": 1}])
        operator.commit()
        yield operator


@pytest.fixture(scope="session")
def select_result(operator):
    result = operator.execute_text("SELECT x, y FROM test_table WHERE x=1", [])
    yield result
