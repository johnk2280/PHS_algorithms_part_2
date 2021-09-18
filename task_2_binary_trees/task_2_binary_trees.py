class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        node = self.Root
        search_result = BSTFind()
        if self.Root:
            while True:
                if key == node.NodeKey:
                    search_result.NodeHasKey = True
                    break
                elif key > node.NodeKey:
                    if node.RightChild:
                        node = node.RightChild
                    else:
                        break
                else:
                    if node.LeftChild:
                        node = node.LeftChild
                    else:
                        search_result.ToLeft = True
                        break

            search_result.Node = node

        return search_result

    def AddKeyValue(self, key, val):
        search_result = self.FindNodeByKey(key)
        if search_result.NodeHasKey:
            return False

        if self.Root:
            new_node = BSTNode(key, val, None)
            if search_result.ToLeft:
                search_result.Node.LeftChild = new_node
            else:
                search_result.Node.RightChild = new_node

            new_node.Parent = search_result.Node
        else:
            self.Root = BSTNode(key, val, None)

    def FinMinMax(self, FromNode, FindMax):
        if FromNode:
            node = FromNode
            if FindMax:
                while True:
                    if node.RightChild:
                        node = node.RightChild
                    else:
                        return node
            else:
                while True:
                    if node.LeftChild:
                        node = node.LeftChild
                    else:
                        return node

    def DeleteNodeByKey(self, key):
        search_result = self.FindNodeByKey(key)
        removed_node = search_result.Node
        if not search_result.NodeHasKey:
            return False

        new_node = self.FinMinMax(removed_node.RightChild, False)

        if removed_node is self.Root:
            self.Root = new_node

        if new_node:
            if new_node.RightChild:
                new_node.RightChild.Parent = new_node.Parent

            new_node.Parent.LeftChild = new_node.RightChild

            new_node.Parent = removed_node.Parent
            if removed_node.Parent:
                if removed_node.Parent.NodeKey > removed_node.NodeKey:
                    removed_node.Parent.LeftChild = new_node
                else:
                    removed_node.Parent.RightChild = new_node

            if removed_node.LeftChild:
                removed_node.LeftChild.Parent = new_node
                new_node.LeftChild = removed_node.LeftChild

            removed_node.RightChild.Parent = new_node
            new_node.RightChild = removed_node.RightChild
        else:
            self.Root = None

    def Count(self):
        nodes = [self.Root, ]
        for node in nodes:
            if node.LeftChild:
                nodes.append(node.LeftChild)

            if node.RightChild:
                nodes.append(node.RightChild)

        return len(nodes)
