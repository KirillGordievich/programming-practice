def count_s(S, J):
    s_count = dict.fromkeys(list(S), 0)
    for j in J:
        if j in s_count:
            s_count[j] += 1
    return sum(s_count.values())


def main():
    S, J = input(), input()
    res = count_s(S, J)

    print(res)


if __name__ == "__main__":
    main()