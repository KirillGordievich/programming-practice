import sys


def main():
    count = int(sys.stdin.readline().strip())

    max_seq = 0
    seq = 0
    for _ in range(count):
        input = int(sys.stdin.readline().strip())
        if input == 1:
            seq += 1
        else:
            seq = 0
        if seq > max_seq:
            max_seq = seq
    print(max_seq)


if __name__ == "__main__":
    main()
