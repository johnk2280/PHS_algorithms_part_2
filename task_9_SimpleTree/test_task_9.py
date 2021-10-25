from task_9_SimpleTree import SimpleTree, SimpleTreeNode


def test_EvenTree():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('19', None)
    e = SimpleTreeNode('209', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('91', None)
    h = SimpleTreeNode('19', None)
    m = SimpleTreeNode('69', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(r, h)
    st.AddChild(h, m)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.GetAllNodes() == [r, a, c, h, b, e, d, g, m, f, ]
    assert st.GetAllNodes(a) == [a, b, e, f, ]
    assert st.GetAllNodes(c) == [c, d, g, ]
    assert st.GetAllNodes(h) == [h, m, ]
    assert st.GetAllNodes(f) == [f, ]

    assert st.EvenTrees() == []
    print(1)
