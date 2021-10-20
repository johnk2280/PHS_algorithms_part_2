class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        heap_size = pow(2, depth + 1) - 1
        self.HeapArray = [None] * heap_size
        for key in a[: heap_size]:
            self.Add(key)

    def GetMax(self):
        if self.HeapArray[0] is None:
            return -1  # если куча пуста

        # вернуть значение корня и перестроить кучу

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
            return None

    def _sift_up(self, index):
        if index < 1:
            return

        parent_index = (index - 1) // 2
        if self.HeapArray[parent_index] < self.HeapArray[index]:
            self.HeapArray[parent_index], self.HeapArray[index] = self.HeapArray[index], self.HeapArray[parent_index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        pass
