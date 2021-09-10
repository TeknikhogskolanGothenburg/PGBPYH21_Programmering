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
    player_in_turn = 1
    running = True
    while running:
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

        move = input(f"Player {player_in_turn}, pick a column: ")

        player_in_turn = 2 if player_in_turn == 1 else 1




if __name__ == '__main__':
    main()
