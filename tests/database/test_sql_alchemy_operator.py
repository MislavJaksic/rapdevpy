import pytest
from sqlalchemy import insert, select, and_, or_, delete
from sqlalchemy.exc import OperationalError, CompileError, IntegrityError, NoSuchTableError

from tests.database.model import Base2
from tests.database.model.address import Address  # noqa
from tests.database.model.address2 import Address2  # noqa
from tests.database.model.user import User
from tests.database.model.user2 import User2  # noqa


class TestExecuteText:
    def test_create_new_table(self, operator):
        sql = """CREATE TABLE test_table_2 (x int, y int)"""
        values = []
        operator.execute_text(sql, values)
        assert "test_table_2" in operator.get_table_list()

    def test_create_existing_table(self, operator):
        sql = """CREATE TABLE test_table (x int, y int)"""
        values = []
        with pytest.raises(OperationalError):
            operator.execute_text(sql, values)

    def test_single_insert_into(self, operator):
        sql = "INSERT INTO test_table (x, y) VALUES (:x, :y)"
        values = [{"x": 1, "y": 2}]
        operator.execute_text(sql, values)
        assert (1, 2) in operator.execute_text("SELECT x, y FROM test_table", []).all()
        operator.execute_text("DELETE FROM test_table WHERE x = 1 AND y = 2", [])

    def test_many_insert_into(self, operator):
        sql = "INSERT INTO test_table (x, y) VALUES (:x, :y)"
        values = [{"x": 3, "y": 4}, {"x": 5, "y": 6}]
        operator.execute_text(sql, values)
        rows = operator.execute_text("SELECT x, y FROM test_table", []).all()
        assert (3, 4) in rows
        assert (5, 6) in rows
        operator.execute_text("DELETE FROM test_table WHERE x = 3 AND y = 4", [])
        operator.execute_text("DELETE FROM test_table WHERE x = 5 AND y = 6", [])


class TestExecuteCoreInsert:
    def test_insert_into_table(self, operator, tables):
        values = [{"name": "kilo", "fullname": "Kilo Milo"}, {"name": "patrick", "fullname": "Patrick Star"}]
        operator.execute_core(insert(tables["user_account"]), values)
        rows = operator.execute_text("SELECT name, fullname FROM user_account", []).all()
        assert ("kilo", "Kilo Milo") in rows
        operator.execute_core(delete(User).where(User.name == "kilo"), [])
        operator.execute_core(delete(User).where(User.name == "patrick"), [])

    def test_insert_orm(self, operator, tables):
        values = [{"name": "a"}]
        operator.execute_core(insert(User), values)
        rows = operator.execute_text("SELECT name, fullname FROM user_account", []).all()
        assert ("a", None) in rows
        operator.execute_core(delete(User).where(User.name == "a"), [])

    def test_insert_existing_primary_key(self, operator, tables):
        values = [{"id": 1, "name": "sandy", "fullname": "Sandy Cheeks"}]
        with pytest.raises(IntegrityError):
            operator.execute_core(insert(User), values)

    # def test_insert_from_select(self, operator, tables):  # ToDo
    #     values = [{"name": "sandy", "fullname": "Sandy Cheeks"}, {"name": "patrick", "fullname": "Patrick Star"}]
    #     operator.execute_core(insert(tables["user_account"]), values)
    #     rows = operator.execute_text("SELECT name, fullname FROM user_account", []).all()
    #     assert ("sandy", "Sandy Cheeks") in rows

    def test_insert_returning_sqlite(self, operator, tables):
        """
        SQLite does not support RETURNING.
        """
        values = [{"name": "imigen", "fullname": "Imigen Fitzroy"}]
        user = tables["user_account"]
        with pytest.raises(CompileError):
            operator.execute_core(insert(user).returning(user.c.name, user.c.fullname), values).all()


class TestExecuteCoreSelect:
    def test_select_user_orm(self, operator):
        rows = operator.execute_core(select(User).where(User.name == "sandy"), []).all()
        assert rows[0][0].name == "sandy"
        assert rows[0][0].fullname == "Sandy Cheeks"

    def test_select_orm_column(self, operator):
        row = operator.execute_core(select(User.fullname).where(User.name == "sandy"), []).first()
        assert row[0] == "Sandy Cheeks"

    def test_where_orm(self, operator):
        rows = operator.execute_core(select(Address.email_address).where(
            and_(or_(User.name == 'squidward', User.name == 'sandy'), Address.user_id == User.id)), []).all()
        assert rows[0][0] == "sandy@squirrelpower.org"

    def test_filter_by_orm(self, operator):
        rows = operator.execute_core(select(User).filter_by(name='sandy', fullname='Sandy Cheeks'), []).all()
        assert rows[0][0].name == "sandy"
        assert rows[0][0].fullname == "Sandy Cheeks"


class TestExecuteCoreJoin:
    def test_inner_join_from_orm(self, operator):
        rows = operator.execute_core(select(User.name, Address.email_address).join_from(User, Address), []).all()
        assert rows[0] == ('sandy', 'sandy@squirrelpower.org')

    def test_inner_join_from_with_on_orm(self, operator):  # ToDo look at the example above
        rows = operator.execute_core(
            select(User.name, Address.email_address).join_from(User, Address, User.id == Address.user_id), []).all()
        assert rows[0] == ('sandy', 'sandy@squirrelpower.org')

    def test_inner_join_orm(self, operator):
        rows = operator.execute_core(select(User.name, Address.email_address).join(Address), []).all()
        assert rows[0] == ('sandy', 'sandy@squirrelpower.org')

    def test_outer_left_join_orm(self, operator):
        rows = operator.execute_core(select(User.name, Address.email_address).join_from(User, Address, isouter=True),
                                     []).all()
        assert rows[0] == ('sandy', 'sandy@squirrelpower.org')
        assert rows[1] == ('mint', None)

    def test_outer_right_join_orm(self, operator):
        rows = operator.execute_core(select(User.name, Address.email_address).join_from(Address, User, isouter=True),
                                     []).all()
        assert rows[0] == ('sandy', 'sandy@squirrelpower.org')
        assert rows[1] == (None, 'hello@world.org')

    def test_right_full_outer_join_orm(self, operator):
        with pytest.raises(OperationalError):
            operator.execute_core(select(User.name, Address.email_address).join_from(Address, User, full=True),
                                  []).all()

    # def test_select(self, operator):  # ToDo finish the tutorial; stopped at https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    #     sql = None
    #     values = []
    #     assert operator.execute(sql, values) == None


class TestCreateAllTables:
    def test_with_metadata(self, operator, temp_tables):
        operator.create_all_tables(temp_tables.metadata)
        assert "user_account_2" in operator.get_table_list()
        assert "address_2" in operator.get_table_list()
        operator.drop_all_tables(temp_tables.metadata)

    def test_with_registry(self, operator):
        """
        ToDo Special imports are required for this test to pass!
        """
        operator.create_all_tables(Base2.metadata)
        assert "user_account_2" in operator.get_table_list()
        assert "address_2" in operator.get_table_list()
        operator.drop_all_tables(Base2.metadata)


class TestGetTableList:
    def test_get_tables(self, operator):
        assert "test_table" in operator.get_table_list()


class TestGetTableColumnList:
    def test_get_not_table_columns(self, operator):
        table = "nothing"
        assert operator.get_table_column_list(table) == []


# class TestTableToOrmFile: # ToDo
#     def test_table_to_orm_file(self, operator, tmp_path):
#         table = "test_table"
#         file_path = tmp_path / "test_table.py"
#         operator.table_to_orm_file(table, file_path)
#         assert True

class TestGetTableMetadata:
    def test_get_existing_table_metadata(self, operator):
        test_table = operator.get_table_metadata("test_table")
        assert test_table.name == "test_table"

    def test_get_non_existing_table_metadata(self, operator):
        with pytest.raises(NoSuchTableError):
            operator.get_table_metadata("test_table_not_exist")


class TestGetAlchemyVersion:
    def test_get_alchemy_version(self, operator):
        assert operator.get_alchemy_version() == "1.4.22"


class TestIsTableExist:
    def test_true(self, operator):
        assert operator.is_table_exist("test_table") is True

    def test_false(self, operator):
        assert operator.is_table_exist("test_table_not-exist") is False
