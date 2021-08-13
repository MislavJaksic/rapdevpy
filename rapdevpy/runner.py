"""
    rapdevpy.py
    ------------------

    This is a library. It does not have a Runner.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
# from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, inspect
# from sqlalchemy.future import create_engine
#
# metadata = MetaData()
# Table("user_account", metadata, Column('id', Integer, primary_key=True), Column('name', String(30)),
#       Column('fullname', String))
# Table("address", metadata, Column('id', Integer, primary_key=True),
#       Column('user_id', ForeignKey('user_account.id'), nullable=False),
#       Column('email_address', String, nullable=False))
#
# engine = create_engine("sqlite:///:memory:", echo=True, future=True)
# metadata.create_all(engine)
# connection = engine.connect()
# inspector = inspect(connection)
# print(inspector.get_table_names())
