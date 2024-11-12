# [1,0,8,9] → [1,8,9,0]

a = [1, 0, 0, 8, 9]
zeroes_count = 0

for index in range(len(a)):
    if index - zeroes_count == len(a) - 1:
        break
    if a[index - zeroes_count] == 0:
        a.pop(index - zeroes_count)
        zeroes_count += 1

a.extend([0] * zeroes_count)
print(a)

# second solution
# сначала переназначаем все нули
# потом переписываем все последние элементы на нули

a = [1, 0, 0, 8, 9]
non_zero_count = 0

for index, item in enumerate(a):
    if item != 0:
        a[non_zero_count] = item
        non_zero_count += 1

while non_zero_count < len(a):
    a[non_zero_count] = 0
    non_zero_count += 1

print(a)
