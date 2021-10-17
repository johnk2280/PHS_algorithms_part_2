from task_6_BalancedBST import BSTNode, BalancedBST


def test_GenerateTree():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    bbst = BalancedBST()
    bbst.GenerateTree(a)
    # [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    assert bbst.Root.NodeKey == 8
    assert bbst.Root.LeftChild.NodeKey == 4
    assert bbst.Root.LeftChild.LeftChild.NodeKey == 2
    assert bbst.Root.LeftChild.RightChild.NodeKey == 6
    assert bbst.Root.LeftChild.RightChild.LeftChild.NodeKey == 5
    assert bbst.Root.LeftChild.RightChild.RightChild.NodeKey == 7
    assert bbst.Root.LeftChild.LeftChild.LeftChild.NodeKey == 1
    assert bbst.Root.LeftChild.LeftChild.RightChild.NodeKey == 3
    assert bbst.Root.RightChild.NodeKey == 12
    assert bbst.Root.RightChild.LeftChild.NodeKey == 10
    assert bbst.Root.RightChild.LeftChild.LeftChild.NodeKey == 9
    assert bbst.Root.RightChild.LeftChild.RightChild.NodeKey == 11
    assert bbst.Root.RightChild.RightChild.NodeKey == 14
    assert bbst.Root.RightChild.RightChild.LeftChild.NodeKey == 13
    assert bbst.Root.RightChild.RightChild.RightChild.NodeKey == 15

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
    assert bbst_2.Root.LeftChild.NodeKey == 4
    assert bbst_2.Root.LeftChild.LeftChild.NodeKey == 2
    assert bbst_2.Root.LeftChild.LeftChild.LeftChild.NodeKey == 1
    assert bbst_2.Root.LeftChild.LeftChild.RightChild is None
    assert bbst_2.Root.LeftChild.RightChild.NodeKey == 6
    assert bbst_2.Root.LeftChild.RightChild.LeftChild.NodeKey == 5
    assert bbst_2.Root.LeftChild.RightChild.RightChild is None
    assert bbst_2.Root.RightChild.NodeKey == 14
    assert bbst_2.Root.RightChild.LeftChild.NodeKey == 12
    assert bbst_2.Root.RightChild.LeftChild.LeftChild.NodeKey == 11
    assert bbst_2.Root.RightChild.LeftChild.RightChild is None
    assert bbst_2.Root.RightChild.RightChild.NodeKey == 15
    assert bbst_2.Root.RightChild.RightChild.LeftChild is None
    assert bbst_2.Root.RightChild.RightChild.RightChild is None

