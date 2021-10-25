class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        try:
            NodeToDelete.Children.clear()
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None
        except (ValueError, AttributeError) as errors:
            return

    def GetAllNodes(self, root=None):
        if root is None:
            root = self.Root

        nodes = [root, ]
        for node in nodes:
            if node.Children:
                nodes.extend(node.Children)

        return nodes

    def FindNodesByValue(self, val):
        nodes = self.GetAllNodes()
        nodes_by_value = []
        for node in nodes:
            if node.NodeValue == val:
                nodes_by_value.append(node)

        return nodes_by_value

    def MoveNode(self, OriginalNode, NewParent):
        try:
            OriginalNode.Parent.Children.remove(OriginalNode)
            OriginalNode.Parent = NewParent
            NewParent.Children.append(OriginalNode)
        except (ValueError, AttributeError) as errors:
            return

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len([node for node in self.GetAllNodes() if node.Children == []])

    def EvenTrees(self, root=None, roots: list = None):
        if roots is None:
            roots = []

        if root is None:
            root = self.Root

        sub_tree = self.GetAllNodes(root)
        if len(sub_tree) % 2 != 0:
            return []
        elif len(sub_tree) == 2:
            return [root, ]
        else:
            for child in sub_tree[1:]:
                self.EvenTrees(child)
