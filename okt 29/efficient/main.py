import string

import lorem
from take_time import timing


@timing
def comp():
    values = [i ** 2 for i in range(10_000_000)]


@timing
def no_comp():
    values = []
    for i in range(10_000_000):
        values.append(i**2)

@timing
def no_join(in_text):
    #in_text = lorem.text() * 4_000
    line = ""
    for c in in_text:
        line += ','+c
    return line[1:]


@timing
def with_join(in_text):
    #in_text = lorem.text() * 4_000
    line = ','.join(in_text)
    return line


@timing
def set_in(values):
    for _ in set(values):
        pass


@timing
def set_out(values):
    values = set(values)
    for _ in values:
        pass


@timing
def no_set(values):
    for _ in values:
        pass

def no_match(text):
    upper = 0
    lower = 0
    other = 0
    for c in text:
        if c in string.ascii_uppercase:
            upper += 1
        elif c in string.ascii_lowercase:
            lower += 1
        else:
            other += 1
    print(upper)
    print(lower)
    print(other)



def main():
    a = lorem.text() * 4000
    no_match(a)
    return
    #one = list(range(100_000_000))
    #values = one + one

    #set_in(values)
    #set_out(values)
    #no_set(values)
    l1 = no_join(a)
    l2 = with_join(a)
    print(l1 == l2)
    no_comp()
    comp()


if __name__ == '__main__':
    main()