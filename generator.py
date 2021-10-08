def my_bad_range(n):
    values = []
    cnt = 0
    while cnt < n:
        values.append(cnt)
        cnt += 1
    return values


def my_good_range(n):
    print("Starting...")
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


def main():
    x = my_good_range(3)
    for i in x:
        print(i)
    print(next(x))


if __name__ == '__main__':
    main()
