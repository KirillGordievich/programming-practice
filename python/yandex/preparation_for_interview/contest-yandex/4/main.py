import sys


def generate_brackets_recursive(n: int):
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


def generate_brackets_circle(n: int):
    result = []
    stack = [("", 0, 0)]  # (current seq, open count, close count)

    while stack:
        current, open_left, close_right = stack.pop()

        if close_right == n:
            result.append(current)
            continue

        if close_right < open_left:
            stack.append((current + ")", open_left, close_right + 1))

        if open_left < n:
            stack.append((current + "(", open_left + 1, close_right))

    return result


def main():
    count = int(sys.stdin.readline())

    recursive_result = generate_brackets_recursive(count)
    circle_result = generate_brackets_circle(count)

    print(recursive_result == circle_result)
    print(recursive_result, circle_result)


if __name__ == "__main__":
    main()
