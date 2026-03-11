#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter integers only.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = get_valid_input(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()