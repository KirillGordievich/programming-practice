class A:
    pass


class B:
    pass


class D(B, A):
    pass


class E(D):
    pass


print(E.__mro__)
