"""
Дан массив А и число k, массив можно обходить только либо сначала либо с конца
k_r + k_l = k, где k_r = количество элементов справа, k_l количество элементов слева
Надо найти максимальную сумму k элементов массива.

Пример:
a = [5, -2, 3, 1, 2] и число к=3

Все возможные варианты

5, -2, 3
5, -2, 2
5, 1, 2
2, 1, 3
2, 1, 5
2, 5, -2

Ответ: k_l = 1, k_r = 2, то есть 5 + 2 + 1 = 8
"""
from typing import List


def find_max(a: List[int], k: int) -> int:
    current_sum = sum(a[:k])
    max_sum = current_sum

    for i in range(1, k + 1):
        current_sum += -a[k - i] + a[-i]

        if max_sum < current_sum:
            max_sum = current_sum

    return max_sum


if __name__ == "__main__":
    a = [5, -2, 3, 1, 2]
    k = 3

    assert find_max(a, k) == 8
