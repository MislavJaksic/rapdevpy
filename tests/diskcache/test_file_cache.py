from tests import context
from tests import settings

import pytest
from datetime import timedelta
from time import sleep

from rapdevpy.file_cache import FileCache


@pytest.fixture(scope="function")
def cache():
    with FileCache(settings.test_cache_path) as cache:
        yield cache


@pytest.fixture(scope="function")
def cache_with_key(cache):
    cache.set("key", "value", timedelta(seconds=1))
    yield cache
    cache.clear()


class TestFileCache:
    def test_not_exists(self, cache):
        assert cache.is_exists("key") == False

    def test_exists(self, cache_with_key):
        assert cache_with_key.is_exists("key") == True

    def test_not_get(self, cache):
        assert cache.get("key") == None

    def test_get(self, cache_with_key):
        assert cache_with_key.get("key") == "value"

    def test_set(self, cache):
        assert cache.set("key", "value", timedelta(seconds=1)) == True
        assert cache.get("key") == "value"
        cache.clear()

    def test_not_touch(self, cache):
        assert cache.touch("key", timedelta(seconds=0)) == False
        assert cache.get("key") == None

    def test_touch(self, cache_with_key):
        assert cache_with_key.touch("key", timedelta(seconds=0)) == True
        assert cache_with_key.get("key") == None

    def test_not_delete(self, cache):
        assert cache.delete("key") == False
        assert cache.get("key") == None

    def test_delete(self, cache_with_key):
        assert cache_with_key.delete("key") == True
        assert cache_with_key.get("key") == None

    def test_expiry(self, cache):
        assert cache.set("key", "value", timedelta(seconds=1)) == True
        assert cache.get("key") == "value"
        sleep(1)
        assert cache.get("key") == None
