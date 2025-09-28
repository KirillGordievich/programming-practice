def counter(maximum):
    i = 0
    while i < maximum:
        receive_from_outer = (yield i)

        if receive_from_outer is not None:
            i = receive_from_outer
        else:
            i += 1


gen_countre = counter(10)

for i in gen_countre:
    if i == 4:
        gen_countre.send(0)
    print(i)
