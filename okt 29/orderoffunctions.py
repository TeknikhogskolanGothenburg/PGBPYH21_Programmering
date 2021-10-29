RED = (255, 0, 0)  # OK
my_variable = 10  # Not OK


def func1(my_local_variable):
    global my_variable
    my_variable += 1
    my_local_variable += 1
    func4()
    return my_local_variable


def func2():
    global my_variable
    my_variable *= 2
    func3()


def func3():
    print('Hej')


def func4():
    func2()


def main():
    name = 'Joakim\'s'
    my_local_variable = 10
    my_local_variable = func1(my_local_variable)


if __name__ == '__main__':
    main()
