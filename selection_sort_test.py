from selection_sort import *

def test_selection_sort():
    # Test with a normal list
    input_list = [6, 1, 4, 9, 2]
    expected_output = [1, 2, 4, 6, 9]
    assert selection_sort(input_list) == expected_output

    # Test with an already sorted list
    input_list = [1, 2, 3, 4, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected_output

    # Test with a reverse sorted list
    input_list = [5, 4, 3, 2, 1]
    expected_output = [1, 2, 3, 4, 5]
    assert selection_sort(input_list) == expected_output

    # Test with a list containing duplicates
    input_list = [3, 1, 4, 3, 2]
    expected_output = [1, 2, 3, 3, 4]
    assert selection_sort(input_list) == expected_output

    # Test with an empty list
    input_list = []
    expected_output = []
    assert selection_sort(input_list) == expected_output

    # Test with a single element
    input_list = [1]
    expected_output = [1]
    assert selection_sort(input_list) == expected_output
