import pytest


class Blank:
    def __init__(self):
        self.one = 1
        self.two = 2

    def __str__(self):
        return "{}({})".format(
            type(self).__name__,
            ", ".join("%s:%s" % item for item in vars(self).items()),
        )


@pytest.fixture(scope="function")
def blank():
    yield Blank()


class TestStr:
    def test_str(self, blank):
        assert str(blank) == "Blank(one:1, two:2)"
