def create_board(board):
    """
    Creates the gameboard
    :param board: the board
    """
    for row in board:
        print(" | ".join(row))
        print("- " * 5)

def get_player_input(board, player):
    """
    Handles user input, checks if the move is valid and, if valid, checks if a piece is not already in the selected
    slot

    :param board: The board
    :param player: the player making the move
    """
    while True:
        try:
            row, col = map(int, input(f"P {player}, row col (1-3): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3:
                if board[row - 1][col - 1] == " ":
                    board[row - 1][col - 1] = player
                    break
                else:
                    print("Nope. Again.")
            else:
                print("Invalid slot")
        except ValueError:
            print("The input must be nums between 1-3")

def check_winner(board, piece):
    """
    Checks and returns true if the player place three pieces in a row, column, or diagonal.
    :param board: the board
    :param piece: the player's piece
    :return: true if the player scores 3 pieces in a row, column, or diagonal
    """
    for i in range(3):
        if all(board[i][j] == piece for j in range(3)) or all(board[j][i] == piece for j in range(3)):
            return True
    if all(board[i][i] == piece for i in range(3)) or all(board[i][2 - i] == piece for i in range(3)):
        return True
    return False


def check_if_board_full(board):
    """
    Checks if the board is completely filled
    :param board: the board
    :return: True if there are no empty spaces. Otherwise, false
    """
    return all(col != " " for row in board for col in row)


def play_game():

    """
    The main game loop
    :return: ends the game after the conditions are met
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    piece = ["X", "O"]
    print("Tic-Tac-Toe Game")
    create_board(board)
    for t in range(9):
        player = piece[t % 2]

        get_player_input(board, player)

        create_board(board)
        if check_winner(board, player):
            print(f"P {player} wins!")
            return
        if check_if_board_full(board):
            print("Draw!")
            return
    print("Draw!")

play_game()
