from typing import List, Dict

import sqlalchemy
from sqlalchemy import text, inspect, MetaData
from sqlalchemy.engine import Result
from sqlalchemy.future import create_engine, Engine
from sqlalchemy.orm import Session, DeclarativeMeta


class SqlAlchemyOperator:
    engine: Engine
    session: Session

    def __init__(self, database_url: str):
        """
        :param database_url "sqlite:///C:\\path\\to\\foo.db" or "sqlite:///:memory:"

        Engine: central source of connections to a database, a global object
        Connection: unit of connectivity
        """
        self.engine = create_engine(database_url, echo=True, future=True)
        self.session = Session(self.engine)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def execute(self, sql: str, non_column_non_table_placeholders: List[Dict]) -> Result:
        return self.session.execute(text(sql), non_column_non_table_placeholders)

    def commit(self) -> None:
        self.session.commit()

    def create_all_tables(self, metadata: MetaData):
        metadata.create_all(self.engine)

    def drop_all_tables(self, metadata: MetaData):
        metadata.drop_all(self.engine)

    def get_tables(self) -> List[str]:
        with self.engine.connect() as connection:
            inspector = inspect(connection)
            return inspector.get_table_names()

    def get_table_columns(self, table: str) -> List[Dict]:
        with self.engine.connect() as connection:
            inspector = inspect(connection)
            return inspector.get_columns(table)

    def get_table(self, table: str) -> Table:
        return Table(table, metadata, autoload_with=engine)

    def get_alchemy_version(self) -> str:
        return sqlalchemy.__version__

    def close(self):
        self.session.close()

