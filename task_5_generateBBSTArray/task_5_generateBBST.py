def GenerateBBSTArray(a, bst_array=None, index=0):
    if len(a) < 1:
        return

    if bst_array is None:
        bst_array = [None] * len(a)

    a.sort()
    root_index = len(a) // 2
    bst_array[index] = a[root_index]
    GenerateBBSTArray(a[: root_index], bst_array, index * 2 + 1)
    GenerateBBSTArray(a[root_index + 1:], bst_array, index * 2 + 2)
    return bst_array


