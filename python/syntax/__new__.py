from typing import Optional


class MyClass:
    _instance: Optional["MyClass"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        if not cls._instance:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, val: int = 1):
        if hasattr(self, "_instanced"):
            return
        print(f"__init__ called {val}")
        self.val = val
        self._instanced = True


obj1 = MyClass(5)
print(obj1.val)
obj2 = MyClass(6)

print(obj1, obj2, obj1 is obj2, obj1.val, obj2.val)
