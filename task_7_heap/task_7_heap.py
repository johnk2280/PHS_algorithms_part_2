class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        heap_size = pow(2, depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for key in a[: heap_size]:
            self.Add(key)

    def GetMax(self):
        if not self.HeapArray or not self.HeapArray[0]:
            return -1  # если куча пуста

        largest_key = self.HeapArray[0]
        edge_key_index = self.HeapArray.index(None) - 1 if None in self.HeapArray else len(self.HeapArray) - 1
        self.HeapArray[0] = self.HeapArray[edge_key_index]
        self.HeapArray[edge_key_index] = None
        self._sift_down()
        return largest_key

    def Add(self, key):
        if key is not None:
            new_key_index = self._get_index()
            try:
                self.HeapArray[new_key_index] = key
            except TypeError:
                return False

            if new_key_index > 0:
                self._sift_up(new_key_index)
                return True

        return False

    def _get_index(self):
        try:
            return self.HeapArray.index(None)
        except ValueError:
            return

    def _sift_up(self, index):
        if index < 1:
            return

        parent_index = (index - 1) // 2
        if self.HeapArray[parent_index] < self.HeapArray[index]:
            self.HeapArray[parent_index], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent_index]
            self._sift_up(parent_index)

    def _sift_down(self, index=0):
        root = self.HeapArray[index]
        try:
            left_child = self.HeapArray[index * 2 + 1]
            right_child = self.HeapArray[index * 2 + 2]
        except IndexError:
            return

        if left_child and right_child:
            if left_child > right_child and left_child > root:
                self.HeapArray[index * 2 + 1], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[index * 2 + 1]
                self._sift_down(index * 2 + 1)
            elif right_child > left_child and right_child > root:
                self.HeapArray[index * 2 + 2], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[index * 2 + 2]
                self._sift_down(index * 2 + 2)

