from LinearSearch import *

def test_linear_search():
    assert linear_search([10, 20, 30, 40, 50], 40) == 3
    assert linear_search([10, 20, 30, 40, 50], 60) == -1
    assert linear_search([], 40) == -1
    assert linear_search([40], 40) == 0
    assert linear_search([30], 40) == -1
