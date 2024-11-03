"""

Дана упорядоченная последовательность чисел от 1 до N.
Одно из чисел удалили. Оставшиеся числа перемешали в случайном порядке. Найдите удаленное число.

"""

a = [1, 2, 3, 4, 5, 6]
b = [6, 1, 4, 2, 5]

# b_sort = [1, 2, 4, 5, 6]

# формула арифмитеческой прогрессии s = (a_1 + a_n) * n / 2
# a1, an = a[0], a[-1]
# a_sum = (a1 + an) * len(a) / 2

a_sum = sum(a)
b_sum = sum(b)
miss = a_sum - b_sum

print(miss)
