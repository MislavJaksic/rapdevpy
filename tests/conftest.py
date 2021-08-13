# For the fixtures to be found in other files, the file must be called conftest.py!

import pytest
from sqlalchemy import Integer, Column, String, Table, MetaData, ForeignKey
from sqlalchemy.orm import registry

from rapdevpy.database.sql_alchemy_operator import SqlAlchemyOperator
from tests import settings


@pytest.fixture(scope="session")
def primary_column():
    yield Column('id', Integer, primary_key=True)


@pytest.fixture(scope="function")
def metadata():
    metadata = MetaData()
    Table("user_account", metadata, Column('id', Integer, primary_key=True), Column('name', String(30)),
                       Column('fullname', String))
    Table("address", metadata, Column('id', Integer, primary_key=True),
                          Column('user_id', ForeignKey('user_account.id'), nullable=False),
                          Column('email_address', String, nullable=False))
    yield metadata


@pytest.fixture(scope="session")
def operator():
    with SqlAlchemyOperator(settings.test_in_memory_database) as operator:
        operator.execute("CREATE TABLE test_table (x int, y int)", [])
        operator.execute("INSERT INTO test_table (x, y) VALUES (:x, :y)", [{"x": 1, "y": 2}])
        operator.commit()
        yield operator


@pytest.fixture(scope="session")
def select_result(operator):
    result = operator.execute("SELECT x, y FROM test_table WHERE x=1", [])
    yield result
