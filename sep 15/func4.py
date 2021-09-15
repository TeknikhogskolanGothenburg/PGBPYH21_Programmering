def func_a(a, b):
    a += 10
    b += 5
    return a, b


def func_b(a, b):
    a -= 5
    b -= 10
    return a, b


def func_c(a, b):
    a *= 10
    b *= 5
    return a, b


def func_d(a, b):
    a //= 2
    b //= 3
    return a, b


def main():
    x = 20
    y = 50

    funcs = [func_a, func_b, func_c, func_d]
    for func in funcs:
        x, y = func(x, y)

    # x, y = func_a(x, y)
    # x, y = func_b(x, y)
    # x, y = func_c(x, y)
    # x, y = func_d(x, y)

    print(x, y)



if __name__ == '__main__':
    main()
