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

        n_0 = BSTNode(0, '0', None)
        bst_1 = BST(n_0)
        assert bst_1.FinMinMax(n_0.RightChild, True) is None
        assert bst_1.FinMinMax(n_0.RightChild, False) is None

    def test_DeleteNodeByKey(self):
        assert self.bst.DeleteNodeByKey(9) is False

        assert self.bst.Count() == 9

        assert self.bst.DeleteNodeByKey(3) is True
        assert self.bst.Root == self.n_4
        assert self.n_2.RightChild is None
        assert self.n_2.LeftChild == self.n_1
        assert self.n_3.Parent is None
        assert self.n_3.LeftChild is None
        assert self.n_3.RightChild is None
        assert self.n_1.LeftChild.NodeKey == 0
        assert self.n_1.RightChild is None
        assert self.bst.Count() == 8

        assert self.bst.DeleteNodeByKey(2) is True
        assert self.bst.Root == self.n_4
        assert self.n_2.Parent is None
        assert self.n_2.LeftChild is None
        assert self.n_2.RightChild is None
        assert self.n_1.Parent == self.n_4
        assert self.n_1.LeftChild.NodeKey == 0
        assert self.n_1.RightChild is None
        assert self.n_4.LeftChild == self.n_1
        assert self.n_4.RightChild == self.n_6
        assert self.bst.Count() == 7

        assert self.bst.DeleteNodeByKey(6) is True
        assert self.bst.Root == self.n_4
        assert self.n_4.LeftChild == self.n_1
        assert self.n_4.RightChild == self.n_7
        assert self.n_1.Parent == self.n_4
        assert self.n_1.LeftChild.NodeKey == 0
        assert self.n_1.RightChild is None
        assert self.n_7.Parent == self.n_4
        assert self.n_5.Parent == self.n_7
        assert self.n_5.LeftChild is None
        assert self.n_5.RightChild is None
        assert self.n_7.LeftChild == self.n_5
        assert self.n_7.RightChild.NodeKey == 8
        assert self.n_6.Parent is None
        assert self.n_6.LeftChild is None
        assert self.n_6.RightChild is None
        assert self.bst.Count() == 6

        assert self.bst.DeleteNodeByKey(4) is True
        assert self.n_5.LeftChild == self.n_1
        assert self.n_1.Parent == self.n_5
        assert self.n_1.LeftChild.NodeKey == 0
        assert self.n_1.RightChild is None
        assert self.n_5.RightChild == self.n_7
        assert self.n_7.RightChild.NodeKey == 8
        assert self.n_7.LeftChild is None
        assert self.n_6.Parent is None
        assert self.n_6.LeftChild is None
        assert self.n_6.RightChild is None
        assert self.bst.Root == self.n_5
        assert self.n_5.Parent is None
        assert self.n_4.Parent is None
        assert self.n_4.LeftChild is None
        assert self.n_4.RightChild is None
        assert self.bst.Count() == 5

        assert self.bst.DeleteNodeByKey(8) is True
        assert self.n_5.LeftChild == self.n_1
        assert self.n_1.Parent == self.n_5
        assert self.n_1.LeftChild.NodeKey == 0
        assert self.n_1.RightChild is None
        assert self.n_5.RightChild == self.n_7
        assert self.n_7.RightChild is None
        assert self.n_7.LeftChild is None
        assert self.n_6.Parent is None
        assert self.n_6.LeftChild is None
        assert self.n_6.RightChild is None
        assert self.bst.Root == self.n_5
        assert self.n_5.Parent is None
        assert self.n_4.Parent is None
        assert self.n_4.LeftChild is None
        assert self.n_4.RightChild is None
        assert self.bst.Count() == 4

        assert self.bst.DeleteNodeByKey(0) is True
        assert self.n_5.LeftChild == self.n_1
        assert self.n_1.Parent == self.n_5
        assert self.n_1.LeftChild is None
        assert self.n_1.RightChild is None
        assert self.n_5.RightChild == self.n_7
        assert self.n_7.RightChild is None
        assert self.n_7.LeftChild is None
        assert self.n_6.Parent is None
        assert self.n_6.LeftChild is None
        assert self.n_6.RightChild is None
        assert self.bst.Root == self.n_5
        assert self.n_5.Parent is None
        assert self.n_4.Parent is None
        assert self.n_4.LeftChild is None
        assert self.n_4.RightChild is None
        assert self.bst.Count() == 3

        self.bst.DeleteNodeByKey(1)

        assert self.bst.DeleteNodeByKey(7) is True
        assert self.bst.Root == self.n_5
        assert self.n_5.RightChild is None
        assert self.n_5.LeftChild is None
        assert self.n_7.Parent is None
        assert self.n_7.LeftChild is None
        assert self.n_7.RightChild is None
        assert self.n_1.Parent is None

        assert self.bst.DeleteNodeByKey(5) is True
        assert self.bst.Root is None
        assert self.n_5.LeftChild is None
        assert self.n_5.RightChild is None
        assert self.n_5.Parent is None
        assert self.bst.Count() == 0

        assert self.bst.DeleteNodeByKey(5) is False

    def test_Count(self):
        bst_2 = BST(None)
        assert bst_2.Count() == 0
