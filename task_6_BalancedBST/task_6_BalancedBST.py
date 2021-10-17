class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a, parent=None):
        if len(a) < 1:
            return
        elif len(a) == 1:
            return BSTNode(a[0], parent)

        a.sort()
        root_index = len(a) // 2
        sub_tree_root = BSTNode(a[root_index], parent)

        if not parent:
            self.Root = sub_tree_root

        sub_tree_root.LeftChild = self.GenerateTree(a[: root_index], sub_tree_root)
        sub_tree_root.RightChild = self.GenerateTree(a[root_index + 1:], sub_tree_root)
        return sub_tree_root

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node
