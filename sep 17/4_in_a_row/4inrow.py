from terminal_color import color_print


def print_board(board):
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


def win(sequence, player):
    for cell in range(len(sequence) - 3):
        if all([sequence[cell + i] == player for i in range(4)]):
            # if set(row[cell: cell+4]) == {player}:
            # if row[cell] == player and row[cell+1] == player and row[cell+2] == player and row[cell+3] == player:
            return True
    return False


def check_horizontal(board, player):
    for row in board:
        if win(row, player):
            return True
    return False


def check_vertical(board, player):
    for c in range(len(board[0])):
        column = [board[r][c] for r in range(len(board))]
        if win(column, player):
            return True
    return False


def check_diagonals(board, player):
    # left to right
    for row in range(3):
        for col in range(4):
            if all([board[row+i][col+i] == player for i in range(4)]):
                return True
            if all([board[row+i][col+3-i] == player for i in range(4)]):
                return True
    return False


def check_winner(board, player):
    for check in [check_horizontal, check_vertical, check_diagonals]:
        if check(board, player):
            return True
    return False


def get_player_column(player_in_turn):
    while True:
        move = input(f"Player {player_in_turn}, pick a column: ")
        if move.upper() in "ABCDEFG" and len(move) == 1:
            break
        color_print("red", f"{move.upper()} is not a valid column")

    return ord(move.upper()) - 65


def place_marker(board, col, player_in_turn):
    for row in board[::-1]:
        if row[col] == 0:
            row[col] = player_in_turn
            return True
    return False


def main():
    # board = [
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 2, 0, 0, 2, 0],
    #     [0, 1, 0, 1, 2, 0, 0],
    #     [0, 1, 1, 2, 2, 2, 0],
    #     [0, 1, 1, 2, 1, 0, 2]
    # ]

    board = [[0] * 7 for _ in range(6)]

    player_in_turn = 1
    running = True
    while running:
        print_board(board)

        col = get_player_column(player_in_turn)

        if place_marker(board, col, player_in_turn):
            if check_winner(board, player_in_turn):
                running = False
            else:
                player_in_turn = 2 if player_in_turn == 1 else 1
        else:
            color_print("red", "That column is full, try a different column")

    print_board(board)
    color_print("green", f"Player {player_in_turn} is the winner")


if __name__ == '__main__':
    main()
