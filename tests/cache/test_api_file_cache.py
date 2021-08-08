import pytest

from rapdevpy.api_file_cache import ApiFileCache
from tests import settings


@pytest.fixture(scope="function")
def api_cache():
    api_cache = ApiFileCache(settings.test_cache_path)
    yield api_cache

# class TestGetData:  # ToDo
#     def test_get_data(self, cache):
#         api_function = None
#         expire_timedelta = None
#         *args = None
#         **kwargs = None
#         assert cache.get_data(api_function, expire_timedelta, *args, **kwargs) == None
# 
# class TestGetResponse:
#     def test_get_response(self, cache):
#         api_function = None
#         expire_timedelta = None
#         *args = None
#         **kwargs = None
#         assert cache.get_response(api_function, expire_timedelta, *args, **kwargs) == None
# 
# class TestGetFromEtag:
#     def test_get_from_etag(self, cache):
#         api_function = None
#         expire_timedelta = None
#         *args = None
#         **kwargs = None
#         assert cache.get_from_etag(api_function, expire_timedelta, *args, **kwargs) == None
# 
# class TestExtractEtag:
#     def test_extract_etag(self, cache):
#         response = None
#         assert cache.extract_etag(response) == None
# 
# class TestGetFromCache:
#     def test_get_from_cache(self, cache):
#         api_function = None
#         expire_timedelta = None
#         *args = None
#         **kwargs = None
#         assert cache.get_from_cache(api_function, expire_timedelta, *args, **kwargs) == None


class TestFormKey:
    def test_form_key(self, api_cache):
        api_function = api_cache.form_key
        assert api_cache.form_key(api_function, 1, page=2) == ('form_key', (1,), {'page': 2})
