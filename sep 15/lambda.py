def f(x):
    return x['age']

def main():
    persons = [
        {
            "name": "John",
            "age": 34
        },
        {
            "name": "Anna",
            "age": 76
        },
        {
            "name": "Sara",
            "age": 156
        }
    ]

    print(max(persons, key=lambda x: x['age']))
    func = lambda a, b, c: a + b + c
    print(func(1, 2, 3))

    sum_age = 0
    for person in persons:
        sum_age += person['age']
    print(sum_age)


if __name__ == '__main__':
    main()
