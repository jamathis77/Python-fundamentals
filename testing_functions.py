# bring in pytest in a virtual environment (via pip)
# Define tests with test_<whateever here>

def find_largest(x, y):
    # or return max(x, y)
    if x > y:
        return x
    else:
        return y


def test_find_largest():
    assert find_largest(1, 2) == 2

def test_something():
    assert "test" == "test"
