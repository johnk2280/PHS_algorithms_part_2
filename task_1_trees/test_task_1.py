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
    pass


def test_GetAllNodes():
    pass


def test_FindNodesByValue():
    pass


def test_MoveNode():
    pass


def test_Count():
    pass


def test_LeafCount():
    pass
