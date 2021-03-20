from tests import context
from tests import settings

import pytest
from lxml import etree

import lxml_lib


@pytest.fixture(scope="module")
def tree():
    tree = etree.parse(settings.test_xml_file_path)
    yield tree


@pytest.fixture(scope="module")
def root(tree):
    root = tree.getroot()
    yield root


@pytest.fixture(scope="module")
def element(root):
    yield root[0][0]


class TestTree:
    def test_load_tree(self):
        tree = lxml_lib.load_tree(settings.test_xml_file_path)
        assert lxml_lib.tree_to_string(tree) == settings.test_xml_file_string


class TestDataElement:
    def test_get_first_element(self, element):
        assert (
            lxml_lib.element_to_string(element)
            == settings.test_xml_first_element_string
        )

    def test_get_tag(self, element):
        assert lxml_lib.get_tag(element) == "Naslov"

    def test_get_namespace(self, element):
        assert (
            lxml_lib.get_namespace(element)
            == "{http://e-porezna.porezna-uprava.hr/sheme/Metapodaci/v2-0}"
        )

    def test_get_tag_with_namespace(self, element):
        assert (
            lxml_lib.get_tag_with_namespace(element)
            == "{http://e-porezna.porezna-uprava.hr/sheme/Metapodaci/v2-0}Naslov"
        )

    def test_get_text(self, element):
        assert lxml_lib.get_text(element) == "Knjiga primljenih (ulaznih) računa"


# class TestRoot:
#     def test_get_tag(self, root):
#         pass
#
#     def test_get_tag_no_namespace(self, root):
#         pass
#
#     def test_get_sub_elements(self, root):
#         pass
#
#     def test_get_sub_elements_with_tag_filter(self, root):
#         pass


# class TestGet:
#     def test_good(self, cache):
#         assert cache["key"] == "value"
#
#     def test_bad(self, cache):
#         with pytest.raises(KeyError):
#             cache["bad"]
#
#
# class TestSet:
#     def test_dict_of_dict(self, cache, dict_of_dict):
#         cache.set("dict_of_dict", dict_of_dict, expire=60, read=False, tag="data")
#         assert cache["dict_of_dict"]["Alice"] == {"Bob": 1}
#         assert cache["dict_of_dict"]["Alice"]["Bob"] == 1
#
#     def test_class(self, cache, class_of_primitives):
#         cache.set("class", class_of_primitives, expire=60, read=False, tag="data")
#         assert cache["class"].integer == 1
#         assert cache["class"].string == "Alice"
