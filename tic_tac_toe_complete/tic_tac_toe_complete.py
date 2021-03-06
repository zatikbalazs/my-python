# Tic Tac Toe Game.

# Import modules.
import random
import time

# Define functions.
def header(title):
    # Print out a nice header.
    # params: str(title)
    # return: str(header)

    # Get the length of title.
    length = len(title)

    # Concatenate header string.
    header = "=" * length + "\n" + title.upper() + "\n" + "=" * length

    return header


def show_board(board):
    # Displays the board with the current position.
    # params: dict(board)
    # return: None

    print()
    print(board["top-l"] + "|" + board["top-m"] + "|" + board["top-r"])
    print("-+-+-")
    print(board["mid-l"] + "|" + board["mid-m"] + "|" + board["mid-r"])
    print("-+-+-")
    print(board["low-l"] + "|" + board["low-m"] + "|" + board["low-r"])
    print()


def check_win(board):
    # Checks whether player has won the game or not.
    # params: dict(board)
    # return: bool

    if (board["top-l"] == "X" and board["top-m"] == "X" and board["top-r"] == "X") or \
       (board["mid-l"] == "X" and board["mid-m"] == "X" and board["mid-r"] == "X") or \
       (board["low-l"] == "X" and board["low-m"] == "X" and board["low-r"] == "X") or \
       (board["top-l"] == "X" and board["mid-l"] == "X" and board["low-l"] == "X") or \
       (board["top-m"] == "X" and board["mid-m"] == "X" and board["low-m"] == "X") or \
       (board["top-r"] == "X" and board["mid-r"] == "X" and board["low-r"] == "X") or \
       (board["top-l"] == "X" and board["mid-m"] == "X" and board["low-r"] == "X") or \
       (board["top-r"] == "X" and board["mid-m"] == "X" and board["low-l"] == "X") or \
       (board["top-l"] == "O" and board["top-m"] == "O" and board["top-r"] == "O") or \
       (board["mid-l"] == "O" and board["mid-m"] == "O" and board["mid-r"] == "O") or \
       (board["low-l"] == "O" and board["low-m"] == "O" and board["low-r"] == "O") or \
       (board["top-l"] == "O" and board["mid-l"] == "O" and board["low-l"] == "O") or \
       (board["top-m"] == "O" and board["mid-m"] == "O" and board["low-m"] == "O") or \
       (board["top-r"] == "O" and board["mid-r"] == "O" and board["low-r"] == "O") or \
       (board["top-l"] == "O" and board["mid-m"] == "O" and board["low-r"] == "O") or \
       (board["top-r"] == "O" and board["mid-m"] == "O" and board["low-l"] == "O"):
        return True
    else:
        return False


def valid_move(board, move):
    # Checks whether move is valid or not.
    # params: dict(board), str(move)
    # return: bool

    if move not in board.keys() or board[move] == "X" or board[move] == "O":
        return False
    else:
        return True



# Print header.
print(header("Tic Tac Toe Game"))

# Start the game loop.
while True:

    # Create the board as a dictionary.
    board = {"top-l": " ", "top-m": " ", "top-r": " ",
             "mid-l": " ", "mid-m": " ", "mid-r": " ",
             "low-l": " ", "low-m": " ", "low-r": " "}

    try:
        # 1 or 2 players?
        game_mode = int(input("\n1 player or 2 players? (1/2) ").strip())

        while game_mode not in [1, 2]:
            game_mode = int(input("1 player or 2 players? (1/2) ").strip())

        if game_mode == 1:
            player_1 = input("Enter your name: ").strip()
            player_2 = "Computer"

        else:
            player_1 = input("Enter name of player 1: ").strip()
            player_2 = input("Enter name of player 2: ").strip()

        # Who starts the game?
        rand_num = random.randint(1, 2)
        if rand_num == 1:
            turn = player_1
        else:
            turn = player_2

        # A game consists of 9 turns.
        for i in range(9):

            # Show the board.
            show_board(board)

            # Single player mode.
            if game_mode == 1:

                if turn == player_1:
                    # Explain syntax of moves.
                    print("Moves: (top|mid|low)-(l|m|r)")
                    print("Examples: top-l, mid-m, low-r")

                    # User enters next move.
                    move = input("\n{}'s turn. Where to move? ".format(turn)).strip().lower()

                    # If move is invalid.
                    while not valid_move(board, move):
                        move = input("Invalid move! Where to move? ").strip().lower()

                else:
                    # Computer's move.
                    print("{} is thinking...".format(player_2))
                    time.sleep(2)
                    print("{}'s move:".format(player_2))

                    # Create list of board keys.
                    moves_list = list(board.keys())

                    # Select random element from list.
                    move = random.choice(moves_list)

                    # If move is invalid.
                    while not valid_move(board, move):
                        move = random.choice(moves_list)


            # Two player mode.
            else:
                # Explain syntax of moves.
                print("Moves: (top|mid|low)-(l|m|r)")
                print("Examples: top-l, mid-m, low-r")

                # User enters next move.
                move = input("\n{}'s turn. Where to move? ".format(turn)).strip().lower()

                # If move is invalid.
                while not valid_move(board, move):
                    move = input("Invalid move! Where to move? ").strip().lower()

            # Update the board (dictionary).
            if turn == player_1:
                board[move] = "X"

            else:
                board[move] = "O"

            # Check win.
            if check_win(board):
                break

            # Switch player.
            if turn == player_1:
                turn = player_2
            else:
                turn = player_1


        # Game over.

        # Show the board.
        show_board(board)

        # Check win.
        if check_win(board):

            # Get length of winner message.
            msg_length = len(turn) + 6

            # Print winner message.
            print("*" * msg_length)
            print("{} wins!".format(turn))
            print("*" * msg_length)

        else:
            # Draw.
            print("It's a draw!".upper())

        # New game?
        new_game = input("\nWould you like to start a new game? (y/n) ").strip().lower()

        if new_game == "y" or new_game == "yes":
            continue

        else:
            # Game over.
            print("Game over. See you next time!")
            break

    except ValueError:
        print("Only numbers please.\n")
        continue
