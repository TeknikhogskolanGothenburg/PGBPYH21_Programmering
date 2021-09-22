def main():
    p1 = {
        'name': 'Bengt',
        'age': 34
    }

    p2 = {
        'name': 'Anna',
        'age': 45
    }
    values = [p1, p2]
    #values.sort()
    a = sorted(values, key=lambda p: p['age'])
    print(a)


if __name__ == '__main__':
    main()
