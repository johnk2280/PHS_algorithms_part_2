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
        # добавляем ключ-значение в дерево
        return False  # если ключ уже есть

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        return None

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        return False  # если узел не найден

    def Count(self):
        return 0  # количество узлов в дереве
