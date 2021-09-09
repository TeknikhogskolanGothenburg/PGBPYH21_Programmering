def color_print(color, text, end="\n"):
    color_dict = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }

    color_string = f"\033[{color_dict[color]}m"
    reset_string = f"\033[0m"
    print(f"{color_string}{text}{reset_string}", end=end)


def main():
    color_print("blue", "blue")
    color_print("red", "red")
    color_print("green", "green")
    color_print("yellow", "yellow")
    color_print("black", "black")
    color_print("yellow", "Ok detta", end=" ")
    color_print("red", "var", end=" ")
    print("ju snyggt")


if __name__ == '__main__':
    main()
