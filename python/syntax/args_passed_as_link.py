a_list = [1, 2]
a_str = "Hello"


def test_is_list(a):
    print(a is a_list)


def test_is_str(a):
    print(a is a_str)


test_is_list(a_list)
test_is_str(a_str)
