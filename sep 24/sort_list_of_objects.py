class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __str__(self):
        return f"{self.name} is {self.age} years old"


def compare(person):
    return person.name


def main():
    p1 = {'name': 'A', 'age': 8}
    p2 = {'name': 'B', 'age': 7}
    p3 = {'name': 'C', 'age': 6}
    p4 = {'name': 'D', 'age': 5}
    p5 = {'name': 'E', 'age': 4}
    p6 = {'name': 'F', 'age': 3}
    p7 = {'name': 'G', 'age': 2}
    p8 = {'name': 'H', 'age': 1}

    persons = [p3, p2, p1, p4, p5, p6, p7, p8]
    sorted_persons = sorted(persons, key=lambda p: p.name)
    print(sorted_persons)


if __name__ == '__main__':
    main()
