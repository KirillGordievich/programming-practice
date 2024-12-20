def even_range(n):
    """Yields numbers from 0 to n, in order 0, n, 1, n-1..."""
    i = 0
    while i <= n:
        yield i
        i += 2

even_range_10 = even_range(10)
for i in even_range_10:
    print(i)