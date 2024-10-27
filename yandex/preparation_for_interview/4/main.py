import sys


def generate_brackets(n: int):
    result = []
    generate_brackets_iter(result, "", 0, 0, n)
    return result


def generate_brackets_iter(result: list[str], current: str, open_left: int, close_right: int, max_seq: int):
    if close_right == max_seq:
        result.append(current)
        return

    if open_left < max_seq:
        generate_brackets_iter(result, current + "(", open_left + 1, close_right, max_seq)

    if close_right < open_left:
        generate_brackets_iter(result, current + ")", open_left, close_right + 1, max_seq)


def main():
    count = int(sys.stdin.readline())

    print(generate_brackets(count))


if __name__ == "__main__":
    main()
