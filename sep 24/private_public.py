class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.email = ""

    @property
    def name(self):
        print('getter')
        return self.__name

    @name.setter
    def name(self, name):
        print('setter')
        self.__name = name


def main():
    p1 = Person('Lisa', 45)
    p1._Person__name = 'Kalle'
    #p1.name = 'Anna'

    print(p1.name)


if __name__ == '__main__':
    main()
