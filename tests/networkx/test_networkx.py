from tests import context
from tests import settings

import pytest

from rapdevpy import networkx_lib


@pytest.fixture(scope="module")
def graph():
    edge_graph = networkx_lib.read_graph_edges(settings.test_edges_file_path)
    yield edge_graph


class TestSummary:
    def test_get_graph_summary(self, graph):
        assert networkx_lib.get_graph_summary(graph) == "V:3334; E:4232"


class TestAtDistance:
    def test_get_graph_vertices_at_distance_0(self, graph):
        assert networkx_lib.get_graph_vertices_at_distance(graph, "30000219", 0) == [
            "30000219"
        ]

    def test_get_graph_vertices_at_distance_1(self, graph):
        assert networkx_lib.get_graph_vertices_at_distance(graph, "30000219", 1) == [
            "30000215",
            "30000216",
        ]

    def test_get_graph_vertices_at_distance_2(self, graph):
        assert networkx_lib.get_graph_vertices_at_distance(graph, "30000219", 2) == [
            "30000217",
            "30000221",
            "30000251",
        ]


class TestUpToDistance:
    def test_get_graph_vertices_up_to_distance_0(self, graph):
        assert networkx_lib.get_graph_vertices_up_to_distance(
            graph, "30000219", 0
        ) == ["30000219"]

    def test_get_graph_vertices_up_to_distance_1(self, graph):
        assert networkx_lib.get_graph_vertices_up_to_distance(
            graph, "30000219", 1
        ) == [
            "30000215",
            "30000216",
            "30000219",
        ]

    def test_get_graph_vertices_up_to_distance_2(self, graph):
        assert networkx_lib.get_graph_vertices_up_to_distance(
            graph, "30000219", 2
        ) == [
            "30000215",
            "30000216",
            "30000217",
            "30000219",
            "30000221",
            "30000251",
        ]
