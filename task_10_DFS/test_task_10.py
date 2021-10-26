from task_10_DFS import Vertex, SimpleGraph


# def test_DepthFirstSearch():
#     g = SimpleGraph(3)
#
#     assert g.max_vertex == 3
#     assert g.m_adjacency == [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#     ]
#     assert g.vertex == [None, None, None]
#
#     assert g.AddVertex(1) is True
#     assert g.AddVertex(2) is True
#     assert g.AddVertex(3) is True
#     assert g.m_adjacency == [
#         [0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0],
#     ]
#
#     g.AddEdge(0, 1)
#     g.AddEdge(1, 2)
#     assert g.m_adjacency == [
#         [0, 1, 0],
#         [1, 0, 1],
#         [0, 1, 0],
#     ]
#
#     assert g.DepthFirstSearch(0, 2) == [g.vertex[0], g.vertex[1], g.vertex[2]]


def test_DepthFirstSearch_seven_vertexes():
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

    for i in range(1, 8):
        g.AddVertex(str(i))

    assert g.vertex[0].Value == '1'
    assert g.vertex[1].Value == '2'
    assert g.vertex[2].Value == '3'
    assert g.vertex[3].Value == '4'
    assert g.vertex[4].Value == '5'
    assert g.vertex[5].Value == '6'
    assert g.vertex[6].Value == '7'

    g.AddEdge(0, 1)
    g.AddEdge(1, 2)
    g.AddEdge(4, 2)
    g.AddEdge(4, 5)
    g.AddEdge(6, 5)
    g.AddEdge(0, 3)
    g.AddEdge(6, 3)
    assert g.m_adjacency == [
        [0, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0],
    ]
    assert g.DepthFirstSearch(0, 6) == [
        g.vertex[0],
        g.vertex[1],
        g.vertex[2],
        g.vertex[4],
        g.vertex[5],
        g.vertex[6],
        # g.vertex[3]
    ]
