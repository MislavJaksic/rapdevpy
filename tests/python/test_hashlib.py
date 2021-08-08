import hashlib

import pytest


# Learner's tests


@pytest.fixture(scope="function")
def string():
    yield "Alice"


@pytest.fixture(scope="function")
def integer():
    yield 1


@pytest.fixture(scope="function")
def primitive_list(string, integer):
    yield [string, integer]


@pytest.fixture(scope="function")
def list_of_lists(primitive_list):
    yield [primitive_list, primitive_list]


@pytest.fixture(scope="function")
def dict(string, integer):
    yield {"string": string, "integer": integer}


@pytest.fixture(scope="function")
def tuple(string, integer):
    yield (string, integer)


class TestDigest:
    def test_string_bad(self, string):
        data = string
        with pytest.raises(TypeError):
            hashlib.sha512(string).hexdigest()

    def test_string_good(self, string):
        data = string.encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "299403b3d6b5c6244fc0ec6f278cb8c233734f0c156c6b8c214341fd6f8f7c781b9b2a137a09329032b9d58e8a37060690521a7d93631d43699efce8106085c9"
        )

    def test_int_bad(self, integer):
        data = integer
        with pytest.raises(TypeError):
            hashlib.sha512(data).hexdigest()

    def test_int_good(self, integer):
        data = str(integer).encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a"
        )

    def test_primitive_list_bad(self, primitive_list):
        data = primitive_list
        with pytest.raises(TypeError):
            hashlib.sha512(data).hexdigest()

    def test_primitive_list_good(self, primitive_list):
        data = str(primitive_list).encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "9c7e50c4ad6cc1521643165d971723bee9ff906ce3ea305a48a7d5392a98b0d24205719d37e7f6e1952d96bbe7fc64c74c85b318bc0ad45dd3a91bc95e14ccb6"
        )

    def test_list_of_lists_bad(self, list_of_lists):
        data = list_of_lists
        with pytest.raises(TypeError):
            hashlib.sha512(data).hexdigest()

    def test_list_of_lists_good(self, list_of_lists):
        data = str(list_of_lists).encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "195a473bb26cff9cd0c3951e0ab6459fb18f6c196cf8d9d08731f65d1b207c0c4607916ea0670ce493a3a3855ba9c46c43bd7adf616273c63b32e8e644b1dc68"
        )

    def test_dict_bad(self, dict):
        data = dict
        with pytest.raises(TypeError):
            hashlib.sha512(data).hexdigest()

    def test_dict_good(self, dict):
        data = str(dict).encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "2832de0e455d3bc2c03f828b612ecedd91b9270fb8db18babba2b4aa28a0602a4ede70949183327a3679ba02a8dcd2a2bd6941541200d6ed2f225292bafe2be2"
        )

    def test_tuple_bad(self, tuple):
        data = tuple
        with pytest.raises(TypeError):
            hashlib.sha512(data).hexdigest()

    def test_tuple_good(self, tuple):
        data = str(tuple).encode()
        assert (
                hashlib.sha512(data).hexdigest()
                == "fc96f28b968213739afed1acd25073ad5553b82a86eaebd7e06d0b27b0d51e2ed58687806b983cb7cdfba78d11067d72cc2181cce4904d8f0e020f4b5464902f"
        )
