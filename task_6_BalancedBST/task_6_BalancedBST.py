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

    def GenerateTree(self, a, parent=None, level=0):
        level += 1 if parent else 0
        if len(a) < 1:
            return
        elif len(a) == 1:
            leaf = BSTNode(a[0], parent)
            leaf.Level = level
            return leaf

        a.sort()
        root_index = len(a) // 2
        root_index = a.index(a[root_index])
        sub_tree_root = BSTNode(a[root_index], parent)
        if not parent:
            self.Root = sub_tree_root

        sub_tree_root.Level = level
        sub_tree_root.LeftChild = self.GenerateTree(a[: root_index], sub_tree_root, level)
        sub_tree_root.RightChild = self.GenerateTree(a[root_index + 1:], sub_tree_root, level)
        return sub_tree_root

    def IsBalanced(self, root_node):
        return False  # сбалансировано ли дерево с корнем root_node
