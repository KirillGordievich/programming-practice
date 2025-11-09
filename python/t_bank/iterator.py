from typing import Iterator, Iterable

"""
Напишите генератор для разбиения списка на чанки нужного размера
"""

def chunked_list(iterable: Iterable, chunk_size: int) -> Iterator[list]:
    chunk = []
    for i in iterable:
        chunk.append(i)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []


list_to_chunk, size = ([1, 2, 3, 4, 5, 6], 2)

print(list(chunked_list(iterable=list_to_chunk, chunk_size=size)))