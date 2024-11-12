import sys


def main():
    count = int(sys.stdin.readline())

    for _ in range(count):
        input = sys.stdin.readline()
        if last is None or input != last:
            print(input)

        last = input


if __name__ == "__main__":
    main()
