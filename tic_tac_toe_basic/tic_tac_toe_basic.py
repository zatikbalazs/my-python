# Tic Tac Toe Game

# Define functions.
def print_board():
    """
    Shows the board with the current position.
    """
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    """
    Handles next move of the player.
    """
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}:".format(number))

    # Player enters next move.
    choice = int(input("Enter your move (1-9): ").strip()) - 1

    # If move is valid, we save the move to the list.
    if board[choice] == " ":
        board[choice] = icon
    else:
        print()
        print("That space is taken!")

        print_board()

        # We give the player another chance to move.
        if icon == "X":
            player_move("X")
        elif icon == "O":
            player_move("O")

def is_victory(icon):
    """
    Checks whether player has won the game or not.
    args: dict(board)
    return: bool(win)
    """
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    """
    Checks whether it's a draw or not.
    """
    if " " not in board:
        return True
    else:
        return False


# Create the board by using a list comprehension.
board = [" " for i in range(9)]

# Start the game loop.
while True:
    print_board()

    # Player "X" moves.
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break

    # Player "O" moves.
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
