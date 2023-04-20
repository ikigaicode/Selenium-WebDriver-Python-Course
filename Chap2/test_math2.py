def add_two_numbers(a, b):
    return a + b 


def test_small_numbers():
    assert add_two_numbers(1, 3) == 3, "The sum of 1 and 3 should be 4"


def test_large_numbers():
    assert add_two_numbers(100, 300) == 500, "The sum of 100 and 300 should be 400"

