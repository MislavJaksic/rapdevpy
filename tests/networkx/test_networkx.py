import pytest

from rapdevpy import networkx_lib
from tests import settings


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


class TestGetGraphOriginTargetShortestPath:
    def test_poitot_poitot(self, graph):
        assert networkx_lib.get_graph_origin_target_shortest_path(graph, "30003271", "30003271") == ["30003271"]

    def test_poitot_f67eq(self, graph):
        assert networkx_lib.get_graph_origin_target_shortest_path(graph, "30003271", "30003269") == ["30003271","30003269"]

    def test_poitot_3mogv(self, graph):
        assert networkx_lib.get_graph_origin_target_shortest_path(graph, "30003271", "30003324") == ["30003271",'30003274','30003276','30003278','30003279','30003320','30003321','30003323',"30003324"]