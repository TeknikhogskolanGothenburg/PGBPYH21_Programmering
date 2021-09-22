class Person:
    def __init__(self, **data):
        self.__dict__ = data



def main():
    #p1 = Person('Rune', 53)
    #p2 = Person('Stina', 34)
    data = {'name': 'Lisa', 'age': 24}
    p3 = Person(**data)


    #print(p1.__dict__)
    #print(p2.__dict__)
    print(p3.name, p3.age)


if __name__ == '__main__':
    main()
