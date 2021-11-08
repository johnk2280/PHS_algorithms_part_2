import pytest
from task_4_aBST import aBST


def test_tree_size():
    bst = aBST(0)
    assert len(bst.Tree) == 1

    bst_1 = aBST(1)
    assert len(bst_1.Tree) == 3

    bst_2 = aBST(2)
    assert len(bst_2.Tree) == 7

    bst_3 = aBST(3)
    assert len(bst_3.Tree) == 15

    bst_4 = aBST(10)
    assert len(bst_4.Tree) == 2047


def test_FindKeyIndex():
    a_bst = aBST(0)
    a_bst.Tree[0] = 55
    assert a_bst.FindKeyIndex(55) == 0
    assert a_bst.FindKeyIndex(5) is None

    a_bst_1 = aBST(3)
    assert a_bst_1.FindKeyIndex(12) == 0

    a_bst_1.Tree = [8, 4, 12, 2, 6, None, 14, 1, 3, None, 7, None, None, 13, None]
    assert a_bst_1.FindKeyIndex(14) == 6
    assert a_bst_1.FindKeyIndex(7) == 10
    assert a_bst_1.FindKeyIndex(4) == 1
    assert a_bst_1.FindKeyIndex(10) == -5
    assert a_bst_1.FindKeyIndex(5) == -9
    assert a_bst_1.FindKeyIndex(9) == -5
    assert a_bst_1.FindKeyIndex(11) == -5
    assert a_bst_1.FindKeyIndex(16) == -14

    a_bst_2 = aBST(2)
    a_bst_2.Tree = [8, 4, 12, 2, 6, 10, 14]
    assert a_bst_2.FindKeyIndex(16) is None


def test_AddKey_with_None():
    a_bst = aBST(3)
    a_bst.Tree = [8, 4, 12, 2, 6, None, 14, 1, 3, None, 7, None, None, 13, None]

    assert a_bst.AddKey(5) == 9
    assert a_bst.Tree == [8, 4, 12, 2, 6, None, 14, 1, 3, 5, 7, None, None, 13, None]

    assert a_bst.AddKey(10) == 5
    assert a_bst.Tree == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, None, None, 13, None]

    assert a_bst.AddKey(15) == 14
    assert a_bst.Tree == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, None, None, 13, 15]

    assert a_bst.AddKey(16) == -1

    a_bst_1 = aBST(0)
    assert a_bst_1.Tree == [None]

    assert a_bst_1.AddKey(8) == 0
    assert a_bst_1.Tree == [8]
