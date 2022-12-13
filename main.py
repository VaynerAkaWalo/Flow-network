from directedgraph import DirectedGraph

a = DirectedGraph(5)
print(str(a))
a.addEdge((1, 2, 5))
print(str(a))
a.addEdges(((0, 1, 1), (4, 3, 5), (2, 4, 2)))
print(str(a))
