
class TestGetItem:
    def test___getitem__(self, temp_tables):
        key = "user_account_2"
        assert temp_tables[key].name == "user_account_2"


class TestLen:
    def test_len(self, temp_tables):
        assert len(temp_tables) == 2
