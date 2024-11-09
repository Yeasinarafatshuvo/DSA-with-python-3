from Tree import *


def test_pre_order(capsys):
    binary_tree = BinaryTree()
    root = binary_tree.create_tree() #Create Binary Tree
    binary_tree.pre_order(root)
    #capsys is a special built-in fixture provided by pytest  It allows you to capture and retrieve output
    captured = capsys.readouterr().out # this line is used to capture and retrieve any output that was printed to the console during the execution of a test
    # The expected pre-order traversal for the tree is: 2, 7, 1, 6, 5, 10, 9, 8, 3, 4
    expected_output = "2\n7\n1\n6\n5\n10\n9\n8\n3\n4\n"
    assert captured == expected_output

def test_post_order(capsys):
    binary_tree = BinaryTree()
    root = binary_tree.create_tree()
    binary_tree.post_order(root)
    captured = capsys.readouterr().out
    # The expected post-order traversal for the tree is: 1, 5, 10, 6, 7, 3, 4, 8, 9, 2
    expected_output = "1\n5\n10\n6\n7\n3\n4\n8\n9\n2\n"
    assert captured == expected_output

def test_in_order(capsys):
    binary_tree = BinaryTree()
    root = binary_tree.create_tree()
    binary_tree.in_order(root)
    captured = capsys.readouterr().out
    # The expected in-order traversal for the tree is: 1, 7, 5, 6, 10, 2, 9, 3, 8, 4
    expected_output = "1\n7\n5\n6\n10\n2\n9\n3\n8\n4\n"
    assert captured == expected_output
