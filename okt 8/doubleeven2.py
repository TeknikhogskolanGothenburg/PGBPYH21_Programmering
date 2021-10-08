def main():
    arr = [value * 2 if value % 2 == 0 else value for value in range(1, 7)]
    print(arr)


if __name__ == '__main__':
    main()
