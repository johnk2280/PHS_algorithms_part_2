class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        new_vertex = Vertex(v)
        index_to_insert = self._get_index()
        if index_to_insert is not None:
            self.vertex[index_to_insert] = new_vertex
            return True

        return False

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        try:
            if self.vertex[v]:
                self.vertex[v] = None
                for i in range(self.max_vertex):
                    self.RemoveEdge(v, i)
        except (TypeError, IndexError) as errors:
            return

    def IsEdge(self, v1, v2):
        try:
            return self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1
        except (TypeError, IndexError) as errors:
            return

    def AddEdge(self, v1, v2):
        try:
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        except (TypeError, IndexError) as errors:
            return

    def RemoveEdge(self, v1, v2):
        try:
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0
        except (TypeError, IndexError) as errors:
            return

    def _get_index(self):
        try:
            return self.vertex.index(None)
        except ValueError:
            return

    def DepthFirstSearch(self, VFrom, VTo):
        stack = []
        self.vertex[VFrom].Hit = True
        neighbors = self.m_adjacency[VFrom]
        if self.vertex[VFrom] is self.vertex[VTo] or self.vertex[VTo] in self.m_adjacency[VFrom]:
            self.vertex[VTo].Hit = True
            return [self.vertex[VTo], ]

        stack.append(self.vertex[VFrom])
        for i in range(len(neighbors)):
            if neighbors[i] and self.vertex[i].Hit is False:
                stack.extend(self.DepthFirstSearch(i, VTo))

        return stack

        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
