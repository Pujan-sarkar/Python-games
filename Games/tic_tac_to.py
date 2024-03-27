def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "-":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != "-":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "-" or \
       board[0][2] == board[1][1] == board[2][0] != "-":
        return True

    return False


def tic_tac_toe():
    board = [["-" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not game_over:
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))

        if board[row][col] == "-":
            board[row][col] = player
            print_board(board)

            if check_winner(board):
                print(f"Player {player} wins!")
                game_over = True
            elif all(all(cell != "-" for cell in row) for row in board):
                print("It's a tie!")
                game_over = True
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That position is already taken! Try again.")


tic_tac_toe()
