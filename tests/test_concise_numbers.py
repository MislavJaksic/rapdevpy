import pytest

from rapdevpy.concise_numbers import suffix_number


class TestSuffixNumber:
    def test_zero(self):
        assert suffix_number(0.0) == "0.0"

    def test_ten(self):
        assert suffix_number(10.0) == "10.0"

    def test_thousand(self):
        assert suffix_number(1000.0) == "1.0k"

    def test_million(self):
        assert suffix_number(1000000.0) == "1.0M"

    def test_billion(self):
        assert suffix_number(1000000000.0) == "1.0B"

    def test_negative_ten(self):
        with pytest.raises(ValueError):
            suffix_number(-10.0)
