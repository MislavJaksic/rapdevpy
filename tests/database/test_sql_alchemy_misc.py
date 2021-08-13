class TestResult:
    def test_tuple_access(self, select_result):
        for x, y in select_result:
            assert x == 1
            assert y == 2

    def test_index_access(self, select_result):
        for row in select_result:
            assert row[0] == 1
            assert row[1] == 2

    def test_attribute_access(self, select_result):
        for row in select_result:
            assert row.x == 1
            assert row.y == 2

    def test_mapping_access(self, select_result):
        for dict_row in select_result.mappings():
            assert dict_row["x"] == 1
            assert dict_row["y"] == 2


class TestColumn:
    def test_name(self, primary_column):
        assert primary_column.name == "id"
