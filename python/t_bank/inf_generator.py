# Напиши бесконечный генератор, которые принимает итерабальный объект и постоянно его итерирует
import time


def gen_inf(items):
    data = list(items)
    while True:
        for i in data:
            yield i


def gen_inf_2(items):
    data = list(items)
    while True:
        yield from data


g = gen_inf_2((i for i in range(3)))

for i in g:
    print(i)
    time.sleep(0.5)