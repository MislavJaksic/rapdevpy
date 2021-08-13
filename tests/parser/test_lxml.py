from pathlib import Path

import pytest
from lxml import etree

from rapdevpy.parser import lxml_lib
from tests import settings


@pytest.fixture(scope="module")
def tree():
    tree = etree.parse(Path(settings.test_xml_file_path).as_posix())
    yield tree


@pytest.fixture(scope="module")
def root(tree):
    """
    <?xml version="1.0" encoding="UTF-8"?>
    <ObrazacURA ...>
        <meta:Metapodaci>
        <Zaglavlje>
        <Tijelo>
    </ObrazacURA>
    """
    root = tree.getroot()
    yield root


@pytest.fixture(scope="module")
def element(root):
    """
    <?xml version="1.0" encoding="UTF-8"?>
    <ObrazacURA verzijaSheme="1.0" xsi:schemaLocation="none-ns-value ObrazacURA-v1-0.xsd" xmlns="none-ns-value" xmlns:meta="meta-ns-value" xmlns:xsi="xsi-ns-value">
        <meta:Metapodaci>
                <meta:Naslov dc="http://purl.org/dc/elements/1.1/title">Knjiga primljenih (ulaznih) računa</meta:Naslov>
    """
    yield root[0][0]


class TestLoadTree:
    def test_load_xml_tree(self):
        tree = lxml_lib.load_tree(Path(settings.test_xml_file_path))
        assert lxml_lib.stringify(tree) == settings.test_xml_file_string

    def test_load_html_tree(self):
        tree = lxml_lib.load_tree(Path(settings.test_html_file_path))
        assert lxml_lib.stringify(tree) == settings.test_html_file_string


class TestGetFileParser:
    def test_get_xml_parser(self):
        file_path = Path(settings.test_xml_file_path)
        assert lxml_lib.get_file_parser(file_path) is None

    # def test_get_html_parser(self):  # ToDo cannot test model presence
    #     file_path = Path(settings.test_html_file_path)
    #     assert lxml_lib.get_file_parser(file_path) == "HTMLParser"


class TestGetChildren:
    def test_get_children(self, root):
        assert lxml_lib.get_tags(lxml_lib.get_children(root)) == [
            "Metapodaci",
            "Zaglavlje",
            "Tijelo",
        ]


class TestGetDescendants:
    def test_get_descendants(self, root):
        assert (
                lxml_lib.get_tags(lxml_lib.get_descendants(root))
                == settings.test_xml_root_descendants
        )


class TestGetRoot:
    def test_get_root(self, tree):
        assert lxml_lib.get_tag(lxml_lib.get_root(tree)) == "ObrazacURA"


class TestGetElementAttribute:
    def test_get_element_attribute(self, element):
        assert (
                lxml_lib.get_element_attribute(element, "dc")
                == "http://purl.org/dc/elements/1.1/title"
        )


class TestGetSourceFileName:
    def test_get_source_file_name(self, element):
        assert lxml_lib.get_source_file_name(element) == settings.test_xml_file_path


class TestGetNamespaceDict:
    def test_get_namespace_dict(self, element):
        assert lxml_lib.get_namespace_dict(element) == {
            None: "none-ns-value",
            "meta": "meta-ns-value",
            "xsi": "xsi-ns-value",
        }


class TestGetNamespacePrefix:
    def test_get_namespace_prefix(self, element):
        assert lxml_lib.get_namespace_prefix(element) == "meta"


class TestGetSourceline:
    def test_get_sourceline(self, element):
        assert lxml_lib.get_sourceline(element) == 5


class TestGetTag:
    def test_get_tag(self, element):
        assert lxml_lib.get_tag(element) == "Naslov"


# model TestGetTags:
#     def test_get_tags(self):
#         elements = None
#         assert lxml_lib.get_tags(elements) == None

class TestGetNamespace:
    def test_get_namespace(self, element):
        assert lxml_lib.get_namespace(element) == "{meta-ns-value}"


class TestGetTagWithNamespace:
    def test_get_tag_with_namespace(self, element):
        assert lxml_lib.get_tag_with_namespace(element) == "{meta-ns-value}Naslov"


class TestGetText:
    def test_get_text(self, element):
        assert lxml_lib.get_text(element) == "Knjiga primljenih (ulaznih) računa"


class TestFilterElementsByTags:
    def test_filter_elements_by_tags(self, root):
        elements = lxml_lib.get_descendants(root)
        tags = ["Metapodaci"]
        filtered = lxml_lib.filter_elements_by_tags(elements, tags)
        assert lxml_lib.get_tags(filtered) == ["Metapodaci"]


class TestFindByXpath:
    def test_find_by_xpath(self, tree, root):
        element = lxml_lib.find_by_xpath(
            tree,
            "/meta:Metapodaci/meta:Naslov",
            {
                "meta": "meta-ns-value",
            },
        )
        assert lxml_lib.get_tag(element) == "Naslov"


class TestFindAllByXpath:
    def test_find_all_by_xpath(self, tree):
        elements = lxml_lib.find_all_by_xpath(
            tree,
            "/Zaglavlje/Razdoblje",
            {
                None: "none-ns-value",
            },
        )
        assert elements != []
        assert lxml_lib.get_tag(elements[0]) == "Razdoblje"


class TestIsElement:
    def test_is_element(self, element):
        assert lxml_lib.is_element(element) == True


class TestStringify:
    def test_get_first_element(self, element):
        assert lxml_lib.stringify(element) == settings.test_xml_first_element_string

# model TestTreeToFile:
#     def test_tree_to_file(self):
#         tree = None
#         file = None
#         assert lxml_lib.tree_to_file(tree, file) == None
