# Реализовать стек, который поддерживает метод удаления, добавления элементов и метод, который возвращает максимальный по значению элемент в стеке за О(1)

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_elements = []

    def pop(self):
        if not self.stack:
            raise Exception("Empty stack")
        last = self.stack.pop()
        if last == self.max_elements[-1]:
            self.max_elements.pop()
        return last

    def push(self, item):
        if not self.stack or item > self.max_elements[-1]:
            self.max_elements.append(item)
        self.stack.append(item)

    def max(self):
        if not self.stack:
            raise Exception("Empty stack")
        return self.max_elements[-1]


stack = MaxStack()
stack.push(10)
stack.push(1)
stack.push(5)
stack.push(7)
stack.push(15)

assert stack.max() == 15
stack.pop()
assert stack.max() == 10


