def check_value(value):
    # Early exit
    if value < 0:
        return False
    if 0 < value < 10:
        return True

    # Normal operation of the function
    # ...
    # ...
    return True


def is_even(value):
    # Don't use variables if you don't have to
    result = False
    if value % 2 == 0:
        result = True
    return result


def better_is_even(value):
    # Do this instead
    return value % 2 == 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    # Don't do this!
    better_is_even2 = lambda value: value % 2 == 0
    better_is_even2(12)

    # Use lambdas like this
    p1 = Point(10, 15)
    p2 = Point(23, 13)
    p3 = Point(16, 27)
    p4 = Point(8, 97)

    points = [p1, p2, p3, p4]

    points.sort(key=lambda obj: obj.x)

    value = 10

    value = (lambda x: x + 1)(value)


if __name__ == '__main__':
    main()
