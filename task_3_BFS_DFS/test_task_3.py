import pytest
from task_3_BFS_DFS import BSTNode, BST


def test_WideAllNodes_tree_has_nodes():
    n_4 = BSTNode(4, '4', None)

    n_2 = BSTNode(2, '2', n_4)
    n_1 = BSTNode(1, '1', n_2)
    n_3 = BSTNode(3, '3', n_2)

    n_6 = BSTNode(6, '6', n_4)
    n_5 = BSTNode(5, '5', n_6)
    n_7 = BSTNode(7, '7', n_6)

    n_4.LeftChild = n_2
    n_4.RightChild = n_6
    n_2.LeftChild = n_1
    n_2.RightChild = n_3
    n_6.LeftChild = n_5
    n_6.RightChild = n_7

    bst = BST(n_4)

    assert bst.Count() == 7
    assert bst.WideAllNodes() == (n_4, n_2, n_6, n_1, n_3, n_5, n_7)

    bst.DeleteNodeByKey(4)
    assert bst.Count() == 6
    assert bst.WideAllNodes() == (n_5, n_2, n_6, n_1, n_3, n_7)

    bst.DeleteNodeByKey(2)
    assert bst.Count() == 5
    assert bst.WideAllNodes() == (n_5, n_3, n_6, n_1, n_7)

    bst.DeleteNodeByKey(7)
    assert bst.Count() == 4
    assert bst.WideAllNodes() == (n_5, n_3, n_6, n_1)


def test_WideAllNodes_tree_has_no_nodes():
    bst = BST(None)

    assert bst.Count() == 0
    assert bst.WideAllNodes() == tuple()


def test_WideAllNodes_tree_has_root_without_children():
    n_4 = BSTNode(4, '4', None)
    bst = BST(n_4)

    assert bst.Count() == 1
    assert bst.WideAllNodes() == (n_4,)


def test_WideAllNodes_tree_has_root_with_left_children():
    n_4 = BSTNode(4, '4', None)
    n_2 = BSTNode(2, '2', n_4)
    n_4.LeftChild = n_2
    bst = BST(n_4)

    assert bst.Count() == 2
    assert bst.WideAllNodes() == (n_4, n_2)


def test_WideAllNodes_tree_has_root_with_right_children():
    n_4 = BSTNode(4, '4', None)
    n_6 = BSTNode(6, '6', n_4)
    n_4.RightChild = n_6
    bst = BST(n_4)

    assert bst.Count() == 2
    assert bst.WideAllNodes() == (n_4, n_6)


def test_WideAllNodes_tree_has_root_with_two_children():
    n_4 = BSTNode(4, '4', None)
    n_2 = BSTNode(2, '2', n_4)
    n_6 = BSTNode(6, '6', n_4)
    n_4.LeftChild = n_2
    n_4.RightChild = n_6
    bst = BST(n_4)

    assert bst.Count() == 3
    assert bst.WideAllNodes() == (n_4, n_2, n_6)


def test_DeepAllNodes_tree_has_nodes():
    n_4 = BSTNode(4, '4', None)

    n_2 = BSTNode(2, '2', n_4)
    n_1 = BSTNode(1, '1', n_2)
    n_3 = BSTNode(3, '3', n_2)

    n_6 = BSTNode(6, '6', n_4)
    n_5 = BSTNode(5, '5', n_6)
    n_7 = BSTNode(7, '7', n_6)

    n_4.LeftChild = n_2
    n_4.RightChild = n_6
    n_2.LeftChild = n_1
    n_2.RightChild = n_3
    n_6.LeftChild = n_5
    n_6.RightChild = n_7

    bst = BST(n_4)

    assert bst.Count() == 7
    assert bst.DeepAllNodes(0) == (n_1, n_2, n_3, n_4, n_5, n_6, n_7)
    assert bst.DeepAllNodes(1) == (n_1, n_3, n_2, n_5, n_7, n_6, n_4)
    assert bst.DeepAllNodes(2) == (n_4, n_2, n_1, n_3, n_6, n_5, n_7)

    bst.DeleteNodeByKey(4)
    assert bst.Count() == 6
    assert bst.DeepAllNodes(0) == (n_1, n_2, n_3, n_5, n_6, n_7)
    assert bst.DeepAllNodes(1) == (n_1, n_3, n_2, n_7, n_6, n_5)
    assert bst.DeepAllNodes(2) == (n_5, n_2, n_1, n_3, n_6, n_7)


def test_DeepAllNodes_tree_has_no_nodes():
    bst = BST(None)

    assert bst.DeepAllNodes(0) == tuple()
    assert bst.DeepAllNodes(1) == tuple()
    assert bst.DeepAllNodes(2) == tuple()
    assert bst.Count() == 0


def test_DeepAllNodes_tree_has_root_without_children():
    n_4 = BSTNode(4, '4', None)
    bst = BST(n_4)

    assert bst.DeepAllNodes(0) == (n_4,)
    assert bst.DeepAllNodes(1) == (n_4,)
    assert bst.DeepAllNodes(2) == (n_4,)
    assert bst.Count() == 1


def test_DeepAllNodes_tree_has_root_with_left_children():
    n_4 = BSTNode(4, '4', None)
    n_2 = BSTNode(2, '2', n_4)
    n_4.LeftChild = n_2
    bst = BST(n_4)

    assert bst.DeepAllNodes(0) == (n_2, n_4,)
    assert bst.DeepAllNodes(1) == (n_2, n_4,)
    assert bst.DeepAllNodes(2) == (n_4, n_2,)
    assert bst.Count() == 2


def test_DeepAllNodes_tree_has_root_with_right_children():
    n_4 = BSTNode(4, '4', None)
    n_6 = BSTNode(6, '6', n_4)
    n_4.RightChild = n_6
    bst = BST(n_4)

    assert bst.DeepAllNodes(0) == (n_4, n_6,)
    assert bst.DeepAllNodes(1) == (n_6, n_4,)
    assert bst.DeepAllNodes(2) == (n_4, n_6,)
    assert bst.Count() == 2


def test_DeepAllNodes_tree_has_root_with_both_children():
    n_4 = BSTNode(4, '4', None)
    n_6 = BSTNode(6, '6', n_4)
    n_2 = BSTNode(2, '2', n_4)
    n_4.LeftChild = n_2
    n_4.RightChild = n_6
    bst = BST(n_4)

    assert bst.DeepAllNodes(0) == (n_2, n_4, n_6,)
    assert bst.DeepAllNodes(1) == (n_2, n_6, n_4,)
    assert bst.DeepAllNodes(2) == (n_4, n_2, n_6,)
    assert bst.Count() == 3

