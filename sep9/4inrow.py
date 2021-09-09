from terminal_color import color_print

def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0],
        [0, 2, 1, 0, 0, 0, 0],
        [1, 1, 2, 0, 0, 0, 0]
    ]

    for row in board:
        for cell in row:
            color = "white"
            if cell == 1:
                color = "red"
            elif cell == 2:
                color = "blue"
            color_print(color, "0", end=" ")
        print()
    color_print("green", "A B C D E F G")


if __name__ == '__main__':
    main()
