from task_8_SimpleGraph import Vertex, SimpleGraph


def test_init_SimpleGraph():
    g = SimpleGraph(7)

    assert g.max_vertex == 7
    assert g.m_adjacency == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    assert g.vertex == [None, None, None, None, None, None, None]


def test_AddVertex():
    g = SimpleGraph(3)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.vertex == [None, None, None]

    assert g.AddVertex(1) is True
    assert g.vertex[0].Value == 1

    assert g.AddVertex(2) is True
    assert g.vertex[1].Value == 2

    assert g.AddVertex(3) is True
    assert g.vertex[2].Value == 3

    assert g.AddVertex(4) is False

    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_IsEdge():
    g = SimpleGraph(3)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.vertex == [None, None, None]

    assert g.AddVertex(1) is True
    assert g.vertex[0].Value == 1

    assert g.AddVertex(2) is True
    assert g.vertex[1].Value == 2

    assert g.AddVertex(3) is True
    assert g.vertex[2].Value == 3

    assert g.AddVertex(4) is False

    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert g.IsEdge(0, 1) is False
    assert g.IsEdge(1, 2) is False
    assert g.IsEdge(0, 2) is False
    assert g.IsEdge(None, 1) is None
    assert g.IsEdge(1, None) is None
    assert g.IsEdge(1, 5) is None
    assert g.IsEdge(5, 1) is None


def test_AddEdge():
    g = SimpleGraph(3)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.vertex == [None, None, None]

    assert g.AddVertex(1) is True
    assert g.AddVertex(2) is True
    assert g.AddVertex(3) is True
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert g.IsEdge(0, 1) is False
    assert g.IsEdge(1, 2) is False
    assert g.IsEdge(0, 2) is False

    g.AddEdge(0, 1)
    assert g.m_adjacency[0][1] == 1
    assert g.m_adjacency[1][0] == 1
    assert g.IsEdge(0, 1) is True
    assert g.IsEdge(1, 0) is True

    g.AddEdge(0, 2)
    assert g.m_adjacency[0][2] == 1
    assert g.m_adjacency[2][0] == 1
    assert g.IsEdge(0, 2) is True
    assert g.IsEdge(2, 0) is True

    g.AddEdge(1, 2)
    assert g.m_adjacency[1][2] == 1
    assert g.m_adjacency[2][1] == 1
    assert g.IsEdge(1, 2) is True
    assert g.IsEdge(2, 1) is True

    assert g.m_adjacency == [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]


def test_RemoveEdge():
    g = SimpleGraph(3)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g.m_adjacency == [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]

    assert g.IsEdge(0, 1) is True
    g.RemoveEdge(0, 1)
    assert g.m_adjacency == [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 0],
    ]
    assert g.IsEdge(0, 1) is False

    assert g.IsEdge(0, 2) is True
    g.RemoveEdge(0, 2)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
    assert g.IsEdge(0, 2) is False

    assert g.IsEdge(1, 2) is True
    g.RemoveEdge(1, 2)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.IsEdge(1, 2) is False


def test_RemoveVertex():
    g = SimpleGraph(3)
    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    g.AddVertex(1)
    g.AddVertex(2)
    g.AddVertex(3)

    g.AddEdge(0, 1)
    g.AddEdge(0, 2)
    g.AddEdge(1, 2)

    assert g.m_adjacency == [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]
    assert g.IsEdge(1, 0) is True
    assert g.IsEdge(1, 2) is True
    assert g.IsEdge(1, 0) is True
    assert g.vertex[1].Value == 2

    g.RemoveVertex(1)

    assert g.m_adjacency == [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0],
    ]
    assert g.IsEdge(1, 0) is False
    assert g.IsEdge(1, 2) is False
    assert g.IsEdge(1, 0) is False
    assert g.vertex[1] is None

    g.RemoveVertex(1)

    assert g.IsEdge(1, 0) is False
    assert g.IsEdge(1, 2) is False
    assert g.IsEdge(1, 0) is False
    assert g.vertex[1] is None

    assert g.RemoveVertex(5) is None
    assert g.RemoveVertex(None) is None

    assert g.IsEdge(0, 2) is True
    assert g.IsEdge(1, 2) is False
    assert g.vertex[2].Value == 3

    g.RemoveVertex(2)

    assert g.m_adjacency == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert g.IsEdge(1, 0) is False
    assert g.IsEdge(1, 2) is False
    assert g.IsEdge(2, 0) is False
    assert g.vertex[2] is None

