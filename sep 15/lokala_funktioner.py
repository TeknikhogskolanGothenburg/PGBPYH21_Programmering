#LEGB

a = 44


def outer(a, b):
    x = 10

    def inner(c, d):
        return a + b + c + d * x

    return inner


def func_fact(exp):
    def inner(base):
        return base**exp
    return inner


def main():
    square = func_fact(2)
    cube = func_fact(3)

    print(square(10))
    print(cube(10))


if __name__ == '__main__':
    main()
