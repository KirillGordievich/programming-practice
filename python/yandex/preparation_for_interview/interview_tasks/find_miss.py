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

print("Only missed: ", miss)

"""

Дана упорядоченная последовательность чисел от 1 до N.
Два из чисел удалили. Оставшиеся числа перемешали в случайном порядке. Найдите удаленные числа.

"""

a = [1, 2, 3, 4, 5, 6]
b = [6, 4, 2, 5]

b.sort()

first_miss = second_miss = None

for index, item in enumerate(a):
    if item != b[index if first_miss is None else index - 1]:
        if not first_miss:
            first_miss = item
        else:
            second_miss = item
            break
        # first_miss = item
        # # мы можем также найти второе число
        # break

# a_sum = sum(a)
# b_sum = sum(b) + first_miss
# second_miss = a_sum - b_sum


print(f"Two missed: {first_miss}, {second_miss}")
