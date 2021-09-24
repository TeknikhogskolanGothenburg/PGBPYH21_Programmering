from abc import abstractmethod, ABC


class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.height * self.width / 2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def area(self):
        return self.height * self.width


def main():
    t1 = Triangle(10, 15)
    r1 = Rectangle(10, 15)
    shapes = [t1, r1]
    #s1 = Shape(10, 15)

    for shape in shapes:
        print(shape.area())


if __name__ == '__main__':
    main()
