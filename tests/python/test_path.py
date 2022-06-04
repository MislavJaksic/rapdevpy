from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def path():
    yield Path(
        "E:/GreatRepository/Publishing/GitHubRepositories/rapdevpy/rapdevpy/cache/file_cache.py"
    )


class TestPath:
    def test_attribute_name(self, path):
        assert path.name == "file_cache.py"

    def test_attribute_root(self, path):
        assert path.root == "\\"

    def test_attribute_parts(self, path):
        assert path.parts == (
            "E:\\",
            "GreatRepository",
            "Publishing",
            "GitHubRepositories",
            "rapdevpy",
            "rapdevpy",
            "cache",
            "file_cache.py",
        )

    def test_attribute_anchor(self, path):
        assert path.anchor == "E:\\"

    def test_attribute_drive(self, path):
        assert path.drive == "E:"

    def test_attribute_stem(self, path):
        assert path.stem == "file_cache"

    def test_attribute_suffix(self, path):
        assert path.suffix == ".py"

    def test_attribute_suffixes(self, path):
        assert path.suffixes == [".py"]
