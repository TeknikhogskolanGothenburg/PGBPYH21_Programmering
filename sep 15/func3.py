def func_a(a, b):
    return a + b


def func_b(a, b):
    return a * b


def func_c(a, b, func):
    return func(a, b)


def main():
    result = func_c(10, 2, func_b)
    print(result)


if __name__ == '__main__':
    main()
