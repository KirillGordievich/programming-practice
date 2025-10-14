class TypedDescriptor:
    def __init__(self, expected_type, default=None):
        self.expected_type = expected_type
        self.value = default
        self._attr_name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Attribute '{self._attr_name}' must be {self.expected_type.__name__}, got {type(value).__name__}")
        self.value = value

    def __set_name__(self, owner, name):
        self._attr_name = name


class User:
    name = TypedDescriptor(str)
    age = TypedDescriptor(int)


user = User()
user.name = "Alice"  # OK
user.age = 25        # OK
user.age = "25"    # TypeError