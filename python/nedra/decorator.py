import time

def decorator(func):
    def newfunc(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        duration = time.time() - start
        print(duration)
        return res

    return newfunc


@decorator
def test():
    time.sleep(1)
    print('hello')

test()