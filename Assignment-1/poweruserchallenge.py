def create_board(board):
    """
    Creates the gameboard
    :param b: the board
    :return:
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(b, p):
    """
    Checks and returns true if the player place three marks in a row horizontally or vertically.
    :param b: the board
    :param p: player's piece
    :return: true if the player scores 3 pieces in a row vertically or horizontally
    """
    for i in range(3):
        if all(b[i][j] == p for j in range(3)) or all(b[j][i] == p for j in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)) or all(b[i][2 - i] == p for i in range(3)):
        return True
    return False


def check_if_board_full(b):
    """
    Runs a check on the board to make sure it's not full of pieces
    :param b: the board
    :return: all the spaces that have a piece in them
    """
    return all(c != " " for r in b for c in r)


def play_game():

    """
    The main game loop
    Players take turns placing their piece in a valid square
    Runs checks to ensure the square exists
    Game ends once a player scores 3 piece in a row vertically or horizontally

    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    piece = ["X", "O"]
    print("Tic-Tac-Toe Game")
    create_board(board)
    for t in range(9):
        player = piece[t % 2]
        while True:
            try:
                row, col = map(int, input(f"P {player}, row col (0-2): ").split())
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        create_board(board)
        if check_winner(board, player):
            print(f"P {player} wins!")
            return
        if check_if_board_full(board):
            print("Draw!")
            return
    print("Draw!")

play_game()
