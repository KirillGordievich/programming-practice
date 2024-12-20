def even_range(n):
    """Yields numbers from 0 to n, in order 0, n, 1, n-1..."""
    i = 0
    step = 2
    while i <= n:
        yield i
        i += 2


for i in even_range(10):
    print(i)