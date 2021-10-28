from task_11_BFS import Vertex, SimpleGraph


def test_DepthFirstSearch():
    g = SimpleGraph(3)

    assert g.max_vertex == 3
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.vertex == [None, None, None]

    for i in range(3):
        g.AddVertex(i)

    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    assert g.m_adjacency == [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]

    assert g.DepthFirstSearch(0, 2) == [g.vertex[0], g.vertex[1], g.vertex[2]]
