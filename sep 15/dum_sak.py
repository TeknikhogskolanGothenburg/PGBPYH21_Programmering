p = print


def a(*args, **kwargs):
    p("BINGO!")
    p(*args, **kwargs)


print = a


def main():
    print("hej")
    values = [1, 2, 3]
    print(values)


if __name__ == '__main__':
    main()
