import random


def add(a, b):
    return a + b


def get_value():
    return random.randrange(1, 10)


def get_third_letter_from_input():
    text = input("Enter something: ")
    if len(text) < 3:
        raise ValueError
    return text[2]


def print_third_letter():
    letter = get_third_letter_from_input()
    print("The value we got was:")
    print(letter)


def main():
    print(add(3, 4))


if __name__ == '__main__':
    main()
