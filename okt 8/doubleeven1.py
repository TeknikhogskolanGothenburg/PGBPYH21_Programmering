def main():
    arr = [1, 2, 3, 4, 5, 6]

    new_arr = []
    for value in arr:
        if value % 2 == 0:
            value *= 2
        new_arr.append(value)

    print(arr)


if __name__ == '__main__':
    main()
