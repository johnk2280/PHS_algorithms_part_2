from task_12_WV import SimpleGraph, Vertex


def test_WeakVertices():
    g = SimpleGraph(9)

    for i in range(9):
        g.AddVertex(str(i))

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(3, 2)
    g.AddEdge(3, 1)
    g.AddEdge(2, 1)
    g.AddEdge(4, 0)
    g.AddEdge(4, 5)
    g.AddEdge(2, 5)
    g.AddEdge(7, 5)
    g.AddEdge(8, 5)
    g.AddEdge(8, 7)
    g.AddEdge(8, 6)
    assert g.m_adjacency == [
        [0, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
    ]

    assert g.WeakVertices() == [
        g.vertex[4],
        g.vertex[6],
    ]

    g.AddEdge(5, 6)
    assert g.WeakVertices() == [
        g.vertex[4]
    ]

    g.AddEdge(4, 2)
    assert g.WeakVertices() == []

    g.RemoveEdge(0, 2)
    assert g.WeakVertices() == [
        g.vertex[0]
    ]

    g.RemoveEdge(1, 2)
    assert g.WeakVertices() == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[3],
    ]
    g.RemoveEdge(5, 2)
    assert g.WeakVertices() == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[3],
        g.vertex[2],
    ]
    g.RemoveEdge(5, 8)
    assert g.WeakVertices() == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[4],
        g.vertex[3],
        g.vertex[2],
        g.vertex[5],
        g.vertex[6],
        g.vertex[7],
        g.vertex[8],
    ]
