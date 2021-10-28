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

    def DepthFirstSearch(self, VFrom, VTo, stack=None):
        if stack is None:
            self._clear_visit_flag()
            stack = []

        try:
            self.vertex[VFrom].Hit = True
            stack.append(self.vertex[VFrom])
            if self.m_adjacency[VFrom][VTo]:
                self.vertex[VTo].Hit = True
                stack.append(self.vertex[VTo])
            else:
                for i in range(len(self.m_adjacency[VFrom])):
                    if self.m_adjacency[VFrom][i] and not self.vertex[i].Hit:
                        stack = self.DepthFirstSearch(i, VTo, stack)
                        if stack[-1] is self.vertex[VTo]:
                            break

                if stack[-1] is not self.vertex[VTo]:
                    stack.pop()

            return stack
        except (IndexError, TypeError) as errors:
            return

    def BreadthFirstSearch(self, VFrom, VTo):
        self._clear_visit_flag()
        queue = self._set_queue(VFrom)
        parents = self._set_parents(VFrom)
        self.vertex[VFrom].Hit = True

        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        pass

    def _clear_visit_flag(self):
        for v in self.vertex:
            v.Hit = False

    def _set_queue(self, VFrom: int, queue: list = None) -> list:
        if queue is None:
            queue = []

        neighbors = self.m_adjacency[VFrom]
        queue.extend([i for i in range(len(neighbors)) if neighbors[i]])
        return queue

    def _set_parents(self, VFrom: int, parents: list = None) -> list:
        if parents is None:
            parents = [None] * self.max_vertex

        neighbors = self.m_adjacency[VFrom]
        for i in range(len(neighbors)):
            if neighbors[i]:
                parents[i] = VFrom

        return parents
