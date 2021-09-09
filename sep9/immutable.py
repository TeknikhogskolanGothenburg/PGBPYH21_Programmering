def main():
    x = 10
    y = 9

    print(id(x))
    print(id(y))

    y += 1
    print(id(x))
    print(id(y))


if __name__ == '__main__':
    main()
