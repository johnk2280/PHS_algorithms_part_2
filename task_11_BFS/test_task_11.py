from task_11_BFS import Vertex, SimpleGraph


def test_DepthFirstSearch():
    g = SimpleGraph(6)

    assert g.max_vertex == 6
    assert g.m_adjacency == [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    assert g.vertex == [None, None, None, None, None, None]

    for i in range(6):
        g.AddVertex(i)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 3)
    g.AddEdge(1, 4)
    g.AddEdge(5, 4)
    assert g.m_adjacency == [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0]
    ]

    assert g.DepthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5],
    ]

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[5],
    ]

    g.AddEdge(2, 5)
    g.AddEdge(3, 5)
    assert g.m_adjacency == [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0]
    ]

    assert g.DepthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[3],
        g.vertex[5],
    ]

    assert g.BreadthFirstSearch(0, 5) == [
        g.vertex[0],
        g.vertex[2],
        g.vertex[5],
    ]

    assert g.DepthFirstSearch(4, 0) == [
        g.vertex[4],
        g.vertex[1],
        g.vertex[0],
    ]

    assert g.BreadthFirstSearch(4, 0) == [
        g.vertex[4],
        g.vertex[1],
        g.vertex[0],
    ]

    assert g.DepthFirstSearch(4, 5) == [
        g.vertex[4],
        g.vertex[5],
    ]

    assert g.BreadthFirstSearch(4, 5) == [
        g.vertex[4],
        g.vertex[5],
    ]