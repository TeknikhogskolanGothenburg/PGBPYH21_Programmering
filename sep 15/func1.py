def func1(a: int, b: int) -> tuple:   # a och b är funktionens parametrar
    a += 10
    b += 20
    return a, b, 23, 34, 99


def main():
    for _ in range(45):
        print()
    first, second, *_, almost_last, last = func1(1, 4) # 3 och 5 är argument till funktionen
    print(first)
    print(second)
    print(almost_last)
    print(last)

    tuple_values = (15, 24, 17, 45)
    first, *_, last = tuple_values
    print(first)
    #print(rest)
    print(last)


if __name__ == '__main__':
    main()
