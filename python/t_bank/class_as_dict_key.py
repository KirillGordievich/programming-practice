class A:
    def __init__(self, id):
        self.id = id

    def __hash__(self):
        return 1


class B:
    def __init__(self, id):
        self.id = id

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.id == other.id


a = A(1)
a1 = A(1)
dict_a = {a: 1, a1: 2}

print(dict_a)    # {<__main__.A object at 0x7f759ef62f90>: 1, <__main__.A object at 0x7f759ee58cd0>: 2}
print(hash(a), hash(a1))  # 1, 2
print(a == a1)  # False
print(dict_a[a], dict_a[a1])

print()

b = B(1)
b1 = B(1)
dict_b = {b: 1, b1: 2}
print(dict_b)    # {<__main__.B object at 0x7fecbafc30e0>: 2}
print(hash(b), hash(b1))  # 1, 1
print(b == b1)  # True
print(dict_b[b], dict_b[b1])