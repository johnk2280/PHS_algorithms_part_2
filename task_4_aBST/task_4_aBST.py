class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = pow(2, depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def FindKeyIndex(self, key):
        index = 0
        try:
            while index <= len(self.Tree):
                if self.Tree[index] is None:
                    return 0 if index == 0 else -index
                elif key == self.Tree[index]:
                    return index
                elif key > self.Tree[index]:
                    index = (index + 1) * 2
                else:
                    index = index * 2 + 1
        except IndexError:
            return None

    def AddKey(self, key):
        # добавляем ключ в массив
        return -1
        # индекс добавленного/существующего ключа или -1 если не удалось
