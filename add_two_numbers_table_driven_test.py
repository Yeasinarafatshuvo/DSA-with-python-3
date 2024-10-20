from index import add


def test_add():
    test_cases = [
        {
            "name": 'simple case 1',
            'input': [1,2],
            'expected': 3
        },
        {
            "name": 'simple case 2',
            'input': [5,2],
            'expected': 7
        },
        {
            "name": 'simple case 3',
            'input': [5,-2],
            'expected': 3
        }
    ]

    for test_case in test_cases:
        assert test_case['expected'] == add(*test_case['input']), test_case['name'] #The * operator unpacks the list [a, b] into individual arguments

