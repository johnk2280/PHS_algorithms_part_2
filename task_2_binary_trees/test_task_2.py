import pytest

from .task_2_binary_trees import BST, BSTFind, BSTNode


class TestBinaryTree:
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

    def test_FindNodeByKey(self):
        search_result = self.bst.FindNodeByKey(3)
        assert search_result.Node == self.n_3
        assert search_result.NodeHasKey is True
        assert search_result.ToLeft is False

        bst_2 = BST(None)
        search_result = bst_2.FindNodeByKey(3)
        assert search_result.Node is None
        assert search_result.NodeHasKey is False
        assert search_result.ToLeft is False

        # for insert to right
        search_result = self.bst.FindNodeByKey(8)
        assert search_result.Node == self.n_7
        assert search_result.NodeHasKey is False
        assert search_result.ToLeft is False

        # for insert to left
        # self.bst.DeleteNodeByKey(5)
        search_result = self.bst.FindNodeByKey(0)
        assert search_result.Node == self.n_1
        assert search_result.NodeHasKey is False
        assert search_result.ToLeft is True

    def test_AddKeyValue(self):
        assert self.bst.AddKeyValue(5, '5') is False

        bst_2 = BST(None)
        bst_2.AddKeyValue(5, '5')
        assert bst_2.Root.NodeKey == 5

        # before adding
        search_result = self.bst.FindNodeByKey(8)
        assert search_result.Node == self.n_7
        assert search_result.NodeHasKey is False
        assert search_result.ToLeft is False

        self.bst.AddKeyValue(8, '8')

        # after adding to right
        search_result = self.bst.FindNodeByKey(8)
        assert search_result.NodeHasKey is True
        assert search_result.Node.Parent == self.n_7
        assert self.n_7.RightChild == search_result.Node

        self.bst.AddKeyValue(0, '0')

        # after adding to left
        search_result = self.bst.FindNodeByKey(8)
        assert search_result.NodeHasKey is True
        assert search_result.Node.Parent == self.n_7
        assert self.n_7.RightChild == search_result.Node

    def test_FinMinMax(self):
        max_result = self.bst.FinMinMax(self.n_4, True)
        assert max_result.NodeKey == 8

        max_result = self.bst.FinMinMax(self.n_2, True)
        assert max_result == self.n_3

        min_result = self.bst.FinMinMax(self.n_4, False)
        assert min_result.NodeKey == 0

        min_result = self.bst.FinMinMax(self.n_6, False)
        assert min_result == self.n_5

    def test_DeleteNodeByKey(self):
        assert self.bst.DeleteNodeByKey(9) is False

        self.bst.DeleteNodeByKey(4)
        assert self.n_5.LeftChild == self.n_2
        assert self.n_2.Parent == self.n_5
        assert self.n_5.RightChild == self.n_6
        assert self.n_6.Parent == self.n_5
        assert self.n_6.LeftChild is None

    def test_Count(self):
        assert self.bst.Count() == 8
