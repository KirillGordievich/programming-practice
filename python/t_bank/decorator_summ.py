#
# Напишите декоратор, который умножает результат summ на 2, не используя @
#

def summ(a, b):
    return a + b


def multiply(mulptilpyer: int):
    def decorator(func):
        def newfunc(*args, **kwargs):
            return mulptilpyer * func(*args, **kwargs)

        return newfunc

    return decorator


summ = multiply(2)(summ)

assert summ(3, 7) == 20
