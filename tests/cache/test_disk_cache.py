import pytest
from diskcache import Cache

from tests import settings


class Primitives:
    def __init__(self, integer, string):
        self.integer = integer
        self.string = string


@pytest.fixture(scope="function")
def cache():
    cache = Cache(settings.test_cache_path)
    cache.set("key", "value", expire=60, read=False, tag="data")
    yield cache
    cache.clear()
    cache.close()


@pytest.fixture(scope="function")
def dict_of_dict():
    yield {"Alice": {"Bob": 1}}


@pytest.fixture(scope="function")
def class_of_primitives():
    integer = 1
    string = "Alice"
    yield Primitives(integer, string)


class TestGet:
    def test_good(self, cache):
        assert cache["key"] == "value"

    def test_bad(self, cache):
        with pytest.raises(KeyError):
            cache["bad"]


class TestSet:
    def test_dict_of_dict(self, cache, dict_of_dict):
        cache.set("dict_of_dict", dict_of_dict, expire=60, read=False, tag="data")
        assert cache["dict_of_dict"]["Alice"] == {"Bob": 1}
        assert cache["dict_of_dict"]["Alice"]["Bob"] == 1

    def test_class(self, cache, class_of_primitives):
        cache.set("class", class_of_primitives, expire=60, read=False, tag="data")
        assert cache["class"].integer == 1
        assert cache["class"].string == "Alice"
