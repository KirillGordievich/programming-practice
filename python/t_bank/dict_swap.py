"""
Написать функцию, которая принимает аргументом словарь и возвращает новый словарь,
в котором ключи и значения входного словаря заменены местами (входной словарь измениться не должен)

"""


class A:
    def __init__(self, id):
        self.id = id

    def __hash__(self):
        return 1

def swap_keys_values(d: dict) -> dict:
    new_dict = {}
    for k, v in d.items():
        try:
            new_dict[v] = k
        except Exception:
            continue

    return new_dict

    # return { v: k for k, v in d.items()}


a = A(1)
a1 = A(1)
print({a: 1, a1: 2})    # Чтобы объект
print(hash(a))  # 1
print(hash(a1))  # 1

print(a == a1)  # False

# {1: (1, [2])}