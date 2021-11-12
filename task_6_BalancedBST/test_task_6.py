from task_6_BalancedBST import BSTNode, BalancedBST


def test_GenerateTree():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    bbst = BalancedBST()
    bbst.GenerateTree(a)
    # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    assert bbst.Root.NodeKey == 8
    assert bbst.Root.Level == 0
    assert bbst.Root.LeftChild.NodeKey == 4
    assert bbst.Root.LeftChild.Level == 1
    assert bbst.Root.LeftChild.LeftChild.NodeKey == 2
    assert bbst.Root.LeftChild.LeftChild.Level == 2
    assert bbst.Root.LeftChild.RightChild.NodeKey == 6
    assert bbst.Root.LeftChild.RightChild.Level == 2
    assert bbst.Root.LeftChild.RightChild.LeftChild.NodeKey == 5
    assert bbst.Root.LeftChild.RightChild.LeftChild.Level == 3
    assert bbst.Root.LeftChild.RightChild.RightChild.NodeKey == 7
    assert bbst.Root.LeftChild.RightChild.RightChild.Level == 3
    assert bbst.Root.LeftChild.LeftChild.LeftChild.NodeKey == 1
    assert bbst.Root.LeftChild.LeftChild.LeftChild.Level == 3
    assert bbst.Root.LeftChild.LeftChild.RightChild.NodeKey == 3
    assert bbst.Root.LeftChild.LeftChild.RightChild.Level == 3
    assert bbst.Root.RightChild.NodeKey == 12
    assert bbst.Root.RightChild.Level == 1
    assert bbst.Root.RightChild.LeftChild.NodeKey == 10
    assert bbst.Root.RightChild.LeftChild.Level == 2
    assert bbst.Root.RightChild.LeftChild.LeftChild.NodeKey == 9
    assert bbst.Root.RightChild.LeftChild.LeftChild.Level == 3
    assert bbst.Root.RightChild.LeftChild.RightChild.NodeKey == 11
    assert bbst.Root.RightChild.LeftChild.RightChild.Level == 3
    assert bbst.Root.RightChild.RightChild.NodeKey == 14
    assert bbst.Root.RightChild.RightChild.Level == 2
    assert bbst.Root.RightChild.RightChild.LeftChild.NodeKey == 13
    assert bbst.Root.RightChild.RightChild.LeftChild.Level == 3
    assert bbst.Root.RightChild.RightChild.RightChild.NodeKey == 15
    assert bbst.Root.RightChild.RightChild.RightChild.Level == 3

    assert bbst.Root.LeftChild.LeftChild.LeftChild.Parent.NodeKey == 2
    assert bbst.Root.LeftChild.LeftChild.RightChild.Parent.NodeKey == 2
    assert bbst.Root.LeftChild.RightChild.LeftChild.Parent.NodeKey == 6
    assert bbst.Root.LeftChild.RightChild.RightChild.Parent.NodeKey == 6
    assert bbst.Root.RightChild.LeftChild.LeftChild.Parent.NodeKey == 10
    assert bbst.Root.RightChild.LeftChild.RightChild.Parent.NodeKey == 10
    assert bbst.Root.RightChild.RightChild.LeftChild.Parent.NodeKey == 14
    assert bbst.Root.RightChild.RightChild.RightChild.Parent.NodeKey == 14
    assert bbst.Root.LeftChild.LeftChild.Parent.NodeKey == 4
    assert bbst.Root.LeftChild.RightChild.Parent.NodeKey == 4
    assert bbst.Root.RightChild.LeftChild.Parent.NodeKey == 12
    assert bbst.Root.RightChild.RightChild.Parent.NodeKey == 12
    assert bbst.Root.LeftChild.Parent.NodeKey == 8
    assert bbst.Root.RightChild.Parent.NodeKey == 8
    assert bbst.Root.Parent is None

    a_1 = []
    bbst_1 = BalancedBST()
    assert bbst_1.GenerateTree(a_1) is None

    a_2 = [1, 2, 4, 5, 6, 7, 11, 12, 14, 15]
    bbst_2 = BalancedBST()
    bbst_2.GenerateTree(a_2)
    assert bbst_2.Root.NodeKey == 7
    assert bbst_2.Root.Level == 0
    assert bbst_2.Root.LeftChild.NodeKey == 4
    assert bbst_2.Root.LeftChild.Level == 1
    assert bbst_2.Root.LeftChild.LeftChild.NodeKey == 2
    assert bbst_2.Root.LeftChild.LeftChild.Level == 2
    assert bbst_2.Root.LeftChild.LeftChild.LeftChild.NodeKey == 1
    assert bbst_2.Root.LeftChild.LeftChild.LeftChild.Level == 3
    assert bbst_2.Root.LeftChild.LeftChild.RightChild is None
    assert bbst_2.Root.LeftChild.RightChild.NodeKey == 6
    assert bbst_2.Root.LeftChild.RightChild.Level == 2
    assert bbst_2.Root.LeftChild.RightChild.LeftChild.NodeKey == 5
    assert bbst_2.Root.LeftChild.RightChild.LeftChild.Level == 3
    assert bbst_2.Root.LeftChild.RightChild.RightChild is None
    assert bbst_2.Root.RightChild.NodeKey == 14
    assert bbst_2.Root.RightChild.Level == 1
    assert bbst_2.Root.RightChild.LeftChild.NodeKey == 12
    assert bbst_2.Root.RightChild.LeftChild.Level == 2
    assert bbst_2.Root.RightChild.LeftChild.LeftChild.NodeKey == 11
    assert bbst_2.Root.RightChild.LeftChild.LeftChild.Level == 3
    assert bbst_2.Root.RightChild.LeftChild.RightChild is None
    assert bbst_2.Root.RightChild.RightChild.NodeKey == 15
    assert bbst_2.Root.RightChild.RightChild.Level == 2
    assert bbst_2.Root.RightChild.RightChild.LeftChild is None
    assert bbst_2.Root.RightChild.RightChild.RightChild is None


def test_GenerateTree_with_equal_keys():
    a = [2, 2, 2, 2, 2, 2]
    bbst = BalancedBST()
    bbst.GenerateTree(a)

    assert bbst.Root.NodeKey == 2
    assert bbst.Root.LeftChild is None
    assert bbst.Root.RightChild.NodeKey == 2
    assert bbst.Root.RightChild.LeftChild is None
    assert bbst.Root.RightChild.RightChild.NodeKey == 2
    assert bbst.Root.RightChild.RightChild.RightChild.NodeKey == 2
    assert bbst.Root.RightChild.RightChild.LeftChild is None
    assert bbst.Root.RightChild.RightChild.RightChild.RightChild.NodeKey == 2
    assert bbst.Root.RightChild.RightChild.RightChild.LeftChild is None
    assert bbst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.NodeKey == 2
    assert bbst.Root.RightChild.RightChild.RightChild.RightChild.LeftChild is None
    assert bbst.Root.RightChild.RightChild.RightChild.RightChild.RightChild.RightChild is None

    a_1 = [1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4]
    bbst_1 = BalancedBST()
    bbst_1.GenerateTree(a_1)

    assert bbst_1.Root.NodeKey == 2
    assert bbst_1.Root.Level == 0
    assert bbst_1.Root.LeftChild.NodeKey == 1
    assert bbst_1.Root.LeftChild.Level == 1
    assert bbst_1.Root.LeftChild.LeftChild is None
    assert bbst_1.Root.LeftChild.RightChild.Level == 2
    assert bbst_1.Root.RightChild.NodeKey == 4
    assert bbst_1.Root.RightChild.Level == 1

    assert bbst_1.Root.RightChild.LeftChild.NodeKey == 2
    assert bbst_1.Root.RightChild.LeftChild.Level == 2
    assert bbst_1.Root.RightChild.LeftChild.LeftChild is None
    assert bbst_1.Root.RightChild.LeftChild.RightChild.NodeKey == 2
    assert bbst_1.Root.RightChild.LeftChild.RightChild.Level == 3
    assert bbst_1.Root.RightChild.LeftChild.RightChild.RightChild.NodeKey == 3
    assert bbst_1.Root.RightChild.LeftChild.RightChild.RightChild.Level == 4
    assert bbst_1.Root.RightChild.LeftChild.RightChild.RightChild.LeftChild.NodeKey == 2
    assert bbst_1.Root.RightChild.LeftChild.RightChild.RightChild.LeftChild.Level == 5
    assert bbst_1.Root.RightChild.LeftChild.RightChild.RightChild.RightChild is None

    assert bbst_1.Root.RightChild.RightChild.NodeKey == 4
    assert bbst_1.Root.RightChild.RightChild.RightChild.NodeKey == 4
    assert bbst_1.Root.RightChild.RightChild.RightChild.RightChild.NodeKey == 4
    assert bbst_1.Root.RightChild.RightChild.RightChild.RightChild.RightChild is None


def test_IsBalanced():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    bbst = BalancedBST()
    bbst.GenerateTree(a)

    assert bbst.IsBalanced(bbst.Root) is True
    assert bbst.IsBalanced(bbst.Root.LeftChild) is True
    assert bbst.IsBalanced(bbst.Root.RightChild) is True
    assert bbst.IsBalanced(bbst.Root.LeftChild.LeftChild) is True
    assert bbst.IsBalanced(bbst.Root.LeftChild.RightChild) is True

    a_2 = [1, 2, 4, 5, 6, 7, 11, 12, 14, 15]
    bbst_2 = BalancedBST()
    bbst_2.GenerateTree(a_2)
    assert bbst_2.IsBalanced(bbst_2.Root) is True
    assert bbst_2.IsBalanced(bbst_2.Root.LeftChild) is True
    assert bbst_2.IsBalanced(bbst_2.Root.RightChild) is True
    assert bbst_2.IsBalanced(bbst_2.Root.LeftChild.LeftChild) is True
    assert bbst_2.IsBalanced(bbst_2.Root.LeftChild.RightChild) is True

    a_3 = [2, 2, 2, 2, 2, 2]
    bbst_3 = BalancedBST()
    bbst_3.GenerateTree(a_3)
    assert bbst_3.IsBalanced(bbst_3.Root) is False
    assert bbst_3.IsBalanced(bbst_3.Root.LeftChild) is False
    assert bbst_3.IsBalanced(bbst_3.Root.RightChild) is False

    a_4 = [1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 4]
    bbst_4 = BalancedBST()
    bbst_4.GenerateTree(a_4)
    assert bbst_4.IsBalanced(bbst_4.Root) is False
