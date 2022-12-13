class DirectedGraph:

    def __init__(self, numberofvertices):
        if numberofvertices < 1:
            raise ValueError("Liczba wierzchłków musi być większa od zera")
        self.nvertices = numberofvertices
        self.matrix = [[0 for _ in range(numberofvertices)] for _ in range(numberofvertices)]

    def __str__(self):
        result = ""
        for x in range(self.nvertices):
            result += str(self.matrix[x])
            result += '\n'
        return result

    def addEdge(self, edge):
        if not isinstance(edge, (tuple, list)):
            raise ValueError("Krawędz musi być listą lub krotką")
        if len(edge) != 3:
            raise ValueError("Krawędz musi się składać z 2 wierzchołków i pojemności")

        if edge[0] >= self.nvertices or edge[1] >= self.nvertices:
            raise ValueError("Nie istnieje taki wierzchołek")

        self.matrix[edge[0]][edge[1]] = edge[2]

    def addEdges(self, edges):
        if not isinstance(edges, (tuple, list)):
            raise ValueError("Krawędzę muszą być w liście lub krotce")

        for edge in edges:
            self.addEdge(edge)

    def bfs(self, source, sink, path):
        visited = [False for _ in range(self.nvertices)]

        queue = [source]
        visited[source] = True

        while queue:
            current = queue.pop(0)

            for index in range(self.nvertices):
                if visited[index] == False and self.matrix[current][index] > 0:
                    queue.append(index)
                    visited[index] = True
                    path[index] = current

        return visited[sink]




