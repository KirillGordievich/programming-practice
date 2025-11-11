"""
Написать функцию, которая принимает аргументом словарь и возвращает новый словарь,
в котором ключи и значения входного словаря заменены местами (входной словарь измениться не должен)

"""


def swap_keys_values(d: dict) -> dict:
    new_dict = {}
    for k, v in d.items():
        try:
            new_dict[v] = k
        except Exception:
            continue

    return new_dict

    # return { v: k for k, v in d.items()}
