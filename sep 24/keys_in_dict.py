class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    my_tuple = ([1, 2], [3, 4])
    my_tuple[1].append(33)

    p1 = "sdfs"
    p2 = "sdfs"

    my_dict = {
        p1: 1,
        p2: 2
    }


if __name__ == '__main__':
    main()
