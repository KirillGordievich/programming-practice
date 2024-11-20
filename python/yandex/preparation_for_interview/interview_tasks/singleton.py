class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Singleton __call__ {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            instance = cls._instances[cls]

        return instance


class BaseClass(metaclass=Singleton):

    def __init__(self):
        print(f"Initializing {type(self).__name__}")

a = BaseClass()
b = BaseClass()

print(a is b)
