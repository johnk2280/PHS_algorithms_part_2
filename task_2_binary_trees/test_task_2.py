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

        # for insert to right
        search_result = self.bst.FindNodeByKey(8)
        assert search_result.Node == self.n_7
        assert search_result.NodeHasKey is False
        assert search_result.ToLeft is False

        # for insert to left
        # self.bst.DeleteNodeByKey(5)
        # search_result = self.bst.FindNodeByKey(5)
        # assert search_result.Node == self.n_6
        # assert search_result.NodeHasKey is False
        # assert search_result.ToLeft is True

    def test_AddKeyValue(self):
        pass

    def FinMinMax(self):
        pass

    def test_DeleteNodeByKey(self):
        pass

    def test_Count(self):
        pass
