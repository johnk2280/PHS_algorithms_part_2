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


@pytest.mark.parametrize(
    'keys, expected_result',
    [14, 2, 10, 3, 1, 7, 6, 4, 13, 0],
    [0, 1, 2, 3, 4, None, 6, 7, None, None, 10, None, None, 13, 14],
)
def test_AddKey_with_None(keys, expected_result):
    a_bst = aBST(3)
    for key in keys:
        a_bst.AddKey(key)

    assert a_bst.Tree == expected_result


@pytest.mark.parametrize(
    'keys, expected_result',
    [55, 62, 25, 84, 37, 43, 31, 50, 84, 92],
    [50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92],
)
def test_AddKey_with_None_1(keys, expected_result):
    a_bst = aBST(3)
    for key in keys:
        a_bst.AddKey(key)

    assert a_bst.Tree == expected_result


@pytest.mark.parametrize(
    'keys, expected_result',
    [],
    [],
)
def test_AddKey_without_None(keys, expected_result):
    pass
