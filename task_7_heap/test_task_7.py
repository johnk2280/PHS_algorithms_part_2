from task_7_heap import Heap


def test_MakeHeap():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    depth = 3
    h = Heap()
    h.MakeHeap(a, depth)

    assert len(h.HeapArray) == 15
    assert h.HeapArray == [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None]

    depth_1 = 2
    h_1 = Heap()
    h_1.MakeHeap(a, depth_1)
    assert len(h_1.HeapArray) == 7
    assert h_1.HeapArray == [7, 4, 6, 1, 3, 2, 5]

    h_2 = Heap()
    h_2.MakeHeap([], depth_1)
    assert len(h_2.HeapArray) == 7
    assert h_2.HeapArray == [None, None, None, None, None, None, None]

    h_3 = Heap()
    h_3.MakeHeap(a, 0)
    assert len(h_3.HeapArray) == 1
    assert h_3.HeapArray == [1]


def test_Add():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    h = Heap()
    h.MakeHeap(a, 3)

    assert len(h.HeapArray) == 15
    assert h.HeapArray == [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None]

    assert h.Add(55) is True
    assert h.HeapArray == [55, 11, 6, 7, 9, 2, 5, 1, 4, 3, 8, None, None, None, None]

    assert h.Add(17) is True
    assert h.HeapArray == [55, 11, 17, 7, 9, 6, 5, 1, 4, 3, 8, 2, None, None, None]

    assert h.Add(27) is True
    assert h.HeapArray == [55, 11, 27, 7, 9, 17, 5, 1, 4, 3, 8, 2, 6, None, None]

    assert h.Add(67) is True
    assert h.HeapArray == [67, 11, 55, 7, 9, 17, 27, 1, 4, 3, 8, 2, 6, 5, None]

    assert h.Add(21) is True
    assert h.HeapArray == [67, 11, 55, 7, 9, 17, 27, 1, 4, 3, 8, 2, 6, 5, 21]

    assert h.Add(221) is False
    assert h.HeapArray == [67, 11, 55, 7, 9, 17, 27, 1, 4, 3, 8, 2, 6, 5, 21]

    h_1 = Heap()
    h_1.MakeHeap(a, 2)
    assert h_1.Add(None) is False
    assert h_1.HeapArray == [7, 4, 6, 1, 3, 2, 5]

    h_2 = Heap()
    h_2.MakeHeap(a, 3)
    assert h_2.Add(None) is False
    assert h_2.HeapArray == [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None]


def test_GetMax():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    h = Heap()
    h.MakeHeap(a, 1)

    assert h.HeapArray == [3, 1, 2]
    assert h.GetMax() == 3
    assert h.HeapArray == [2, 1, None]

    h_1 = Heap()
    h_1.MakeHeap(a, 3)
    assert h_1.HeapArray == [11, 9, 6, 7, 8, 2, 5, 1, 4, 3, None, None, None, None, None]
    assert h_1.GetMax() == 11
    assert h_1.HeapArray == [9, 8, 6, 7, 3, 2, 5, 1, 4, None, None, None, None, None, None]

    assert h_1.GetMax() == 9
    assert h_1.HeapArray == [8, 7, 6, 4, 3, 2, 5, 1, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 8
    assert h_1.HeapArray == [7, 4, 6, 1, 3, 2, 5, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 7
    assert h_1.HeapArray == [6, 4, 5, 1, 3, 2, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 6
    assert h_1.HeapArray == [5, 4, 2, 1, 3, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 5
    assert h_1.HeapArray == [4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 4
    assert h_1.HeapArray == [3, 1, 2, None, None, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 3
    assert h_1.HeapArray == [2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 2
    assert h_1.HeapArray == [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == 1
    assert h_1.HeapArray == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    assert h_1.GetMax() == -1
    assert h_1.HeapArray == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
