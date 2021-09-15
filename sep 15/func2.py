def func(a, b, c, d=10, e=11):
    print(a, b, c, d, e)


def func3(a, b, c, d=10, *, e=11):
    print(a, b, c, d, e)


def func2(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


def my_print(*args, sep=' ', end='\n'):
    # str_to_print = sep.join([str(arg) for arg in args])
    str_to_print = ""
    for arg in args:
        str_to_print += str(arg) + sep
    print(str_to_print, end=end)


def main():
    result = ' * '.join(["hej", "hopp", str(47)])
    print(result)


    values = 1, 2, 3, 4
    values = (1, 2, "tjo")
    func(*values)
    func3(1, 2, 3, 4, e=5)




    func2(1, 2, 3, 4, 5, 6, 7, 8, name='sue', color='pink')
    func2("Hej", "på", "dig")
    x = 10
    my_print("hej", "på", "dig", 12, sep='**', end="?")



if __name__ == '__main__':
    main()
