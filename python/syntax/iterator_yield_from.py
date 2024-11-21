def generator2(seconds):
    print('Task 2')
    yield seconds


def generator():
    print('Task 1')
    yield from generator2(5)


print(next(generator()))
