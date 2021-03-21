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


class TestChildren:
    """
    <?xml version="1.0" encoding="UTF-8"?>
    <ObrazacURA ...>
        <meta:Metapodaci>
        <Zaglavlje>
        <Tijelo>
    </ObrazacURA>
    """

    def test_get_children(self, root):
        assert lxml_lib.get_tags(lxml_lib.get_children(root)) == [
            "Metapodaci",
            "Zaglavlje",
            "Tijelo",
        ]

    def test_get_descendants(self, root):
        assert (
            lxml_lib.get_tags(lxml_lib.get_descendants(root))
            == settings.test_xml_root_descendants
        )


class TestElement:
    """
    <?xml version="1.0" encoding="UTF-8"?>
    <ObrazacURA verzijaSheme="1.0" xsi:schemaLocation="none-ns-value ObrazacURA-v1-0.xsd" xmlns="none-ns-value" xmlns:meta="meta-ns-value" xmlns:xsi="xsi-ns-value">
        <meta:Metapodaci>
                <meta:Naslov dc="http://purl.org/dc/elements/1.1/title">Knjiga primljenih (ulaznih) računa</meta:Naslov>
    """

    def test_get_first_element(self, element):
        assert (
            lxml_lib.element_to_string(element)
            == settings.test_xml_first_element_string
        )

    def test_get_source_file_name(self, element):
        assert lxml_lib.get_source_file_name(element) == settings.test_xml_file_path

    def test_get_namespace_dict(self, element):
        assert lxml_lib.get_namespace_dict(element) == {
            None: "none-ns-value",
            "meta": "meta-ns-value",
            "xsi": "xsi-ns-value",
        }

    def test_get_namespace_prefix(self, element):
        assert lxml_lib.get_namespace_prefix(element) == "meta"

    def test_get_sourceline(self, element):
        lxml_lib.get_sourceline(element) == 4

    def test_get_tag(self, element):
        assert lxml_lib.get_tag(element) == "Naslov"

    def test_get_namespace(self, element):
        assert lxml_lib.get_namespace(element) == "{meta-ns-value}"

    def test_get_tag_with_namespace(self, element):
        assert lxml_lib.get_tag_with_namespace(element) == "{meta-ns-value}Naslov"

    def test_get_text(self, element):
        assert lxml_lib.get_text(element) == "Knjiga primljenih (ulaznih) računa"

    def test_filter_elements_by_tags(self, root):
        elements = lxml_lib.get_descendants(root)
        tags = ["Metapodaci"]
        filtered = lxml_lib.filter_elements_by_tags(elements, tags)
        assert lxml_lib.get_tags(filtered) == ["Metapodaci"]


class TestBooleans:
    def test_is_element(self, element):
        assert lxml_lib.is_element(element) == True
