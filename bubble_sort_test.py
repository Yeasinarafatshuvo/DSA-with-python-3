from bubble_sort import *

def test_bubble_sort():
    input_list = [6, 1, 4, 9, 2]
    expected = [1, 2, 4, 6, 9]
    bubble_sort(input_list)
    assert input_list == expected

    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    bubble_sort(input_list)
    assert input_list == expected


    input_list = []
    expected = []
    bubble_sort(input_list)
    assert input_list == expected

    input_list = [1]
    expected = [1]
    bubble_sort(input_list)
    assert input_list == expected
