from directedgraph import DirectedGraph


def ford_fulkerson(graph, source, sink):
    if not isinstance(graph, DirectedGraph):
        raise ValueError("Pierwszy argument musi być grafem skierowanym")

    if source < 0 or sink < 0:
        raise ValueError("Źródło i ujście muszą być nieujemne")

    if source > graph.nvertices or sink > graph.nvertices:
        raise ValueError("Wierzchołek źródła bądz ujścia nie istnieje w tym grafie")

    path = [-1 for _ in range(graph.nvertices)]
    max_flow = 0

    while graph.bfs(source, sink, path):
        current_flow = float("Inf")
        current_node = sink

        while current_node != source:
            current_flow = min(current_flow, graph.matrix[path[current_node]][current_node])
            current_node = path[current_node]

        max_flow += current_flow

        current_node = sink
        while current_node != source:
            parent_current_node = path[current_node]
            graph.matrix[parent_current_node][current_node] -= current_flow
            graph.matrix[current_node][parent_current_node] += current_flow
            current_node = parent_current_node

    return max_flow