
class MyClass:
    def __init__(self, name):
        self._name = name

    def __hash__(self):
        return hash(self._name)


a = MyClass('Kirill')
b = MyClass('Ivan')

d = {
    a, b
}

print(d)