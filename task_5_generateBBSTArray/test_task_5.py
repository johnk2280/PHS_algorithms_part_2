import pytest
from task_5_generateBBST import GenerateBBSTArray


def test_GenerateBBSTArray():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert GenerateBBSTArray(a) == [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    b = []
    assert GenerateBBSTArray(b) is None


