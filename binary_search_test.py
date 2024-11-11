from binary_search import *

def test_binary_search_tree():
    assert binarySearchTree([10, 20, 30, 40, 50], 40) == 3
    assert binarySearchTree([10, 20, 30, 40, 50], 58) == -1
    assert binarySearchTree([10, 20, 30, 40, 50], 50) == 4
    assert binarySearchTree([-10, -5, 0, 5, 10], -5) == 1
    assert binarySearchTree([-10, -5, 0, 5, 10], 10) == 4
