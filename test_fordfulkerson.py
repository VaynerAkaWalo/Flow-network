import pytest
from directedgraph import DirectedGraph
from fordfulkerson import ford_fulkerson

class TestFordFulkerson:
    def test_max_flow_1(self):
        graph = DirectedGraph(7)
        graph.addEdges(((0, 1, 7), (0, 2, 3), (1, 2, 4), (1, 6, 6), (2, 4, 2), (2, 6, 9), (3, 2, 3), (3, 4, 6), (4, 6, 8), (5, 0, 9), (5, 3, 9)))
        assert ford_fulkerson(graph, 5, 6) == 18