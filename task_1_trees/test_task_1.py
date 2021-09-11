import pytest

from .task_1_trees import SimpleTreeNode, SimpleTree


def test_AddChild():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    r = SimpleTreeNode('0', None)
    st = SimpleTree(r)
    st.AddChild(a, b)
    b.Parent = a

    assert st.Root == r
    assert a.Children == [b, ]

    st.AddChild(st.Root, a)
    a.Parent = st.Root

    assert r == a.Parent
    assert st.Root.Children == [a, ]
    assert b.Parent.Parent == st.Root
    assert b.Parent.Parent == r


def test_DeleteNode():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('19', None)
    r = SimpleTreeNode('0', None)
    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)

    assert r.Children == [a, c, ]
    assert a.Children == [b, ]

    st.DeleteNode(a)

    assert st.Root.Children == [c, ]
    assert r.Children == [c, ]
    assert a.Children == []
    assert a.Parent is None


def test_GetAllNodes():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('19', None)
    e = SimpleTreeNode('209', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('9', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.GetAllNodes() == [r, a, c, b, e, d, g, f, ]


def test_FindNodesByValue():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('9', None)
    e = SimpleTreeNode('9', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('9', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.FindNodesByValue('9') == [e, d, g, ]
    assert st.FindNodesByValue('23') == [a, ]
    assert st.FindNodesByValue('15') == [c, ]


def test_MoveNode():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('9', None)
    e = SimpleTreeNode('9', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('9', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    st.MoveNode(a, d)

    assert st.GetAllNodes() == [r, c, d, g, a, b, e, f, ]
    assert r.Children == [c, ]
    assert d.Children == [a, ]


def test_Count():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('9', None)
    e = SimpleTreeNode('9', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('9', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.Count() == 8


def test_LeafCount():
    a = SimpleTreeNode('23', None)
    b = SimpleTreeNode('14', None)
    c = SimpleTreeNode('15', None)
    d = SimpleTreeNode('9', None)
    e = SimpleTreeNode('9', None)
    f = SimpleTreeNode('1', None)
    g = SimpleTreeNode('9', None)
    r = SimpleTreeNode('0', None)

    st = SimpleTree(r)
    st.AddChild(a, b)
    st.AddChild(c, d)
    st.AddChild(r, a)
    st.AddChild(r, c)
    st.AddChild(a, e)
    st.AddChild(b, f)
    st.AddChild(c, g)

    assert st.LeafCount() == 4

    st.MoveNode(a, d)

    assert st.LeafCount() == 3
