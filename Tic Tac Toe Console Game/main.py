from random import randint

player1 = {}
player2 = {}

positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}


def setup_game():
    p1_name = input("Enter first player name: ")
    p2_name = input("Enter second player name: ")

    p1_sign = input(f"{p1_name} choose X or O: ").upper()

    # Check if the sign is X or O.
    while p1_sign not in ["X", "O"]:
        p1_sign = input(f"Incorrect sign! Choose X or O: ").upper()

    p2_sign = "X" if p1_sign == "O" else "0"

    player1["name"] = p1_name
    player1["sign"] = p1_sign
    player2["name"] = p2_name
    player2["sign"] = p2_sign

    print(f"OK! Everything is set up. \n"
          f"{p1_name} you are playing with {p1_sign}.\n"
          f"{p2_name} you are plating with {p2_sign}.\n")


def who_start_first():
    name = player1["name"]
    p1_choice = int(input(f"{name}, press 1 for heads or 2 for tails: "))

    # Check if number is valid.
    while p1_choice not in [0, 1]:
        p1_choice = int(input("Invalid number! \n"
                              "Press 1 for heads or 2 for tails"))

    coin_flip = randint(1, 2)
    result = "Heads" if coin_flip == 1 else "Tails"

    # Add key:value pair to see who start first.
    if coin_flip == p1_choice:
        player1["start"] = True
        player2["start"] = False
    else:
        name = player2["name"]
        player1["start"] = False
        player2["start"] = True

    print(f"{result}! {name} start first!")


# This function will be called only in the "play" function.
def print_board(board):
    for row in board:
        # Convert the matrix numbers to strings. 
        string_numbers = [str(n) for n in row if type(n) == int]
        print(f"|   {'   |   '.join(string_numbers)}   |")


# This function will be called only in the "play" function.
def check_for_winner(board, sign):
    pattern = [sign]*3

    primary_diagonal = []
    secondary_diagonal = []

    for row in range(len(board)):
        # Check for row win.
        if board[row] == pattern:
            return True

        # Add column symbols.
        column = []
        for col in range(len(board)):
            column.append(board[row][col])

        # Check for column win.
        if column == pattern:
            return True

        # Add diagonal symbols.
        primary_diagonal.append(board[row][row])
        secondary_diagonal.append(board[row][len(board) - row - 1])

    # Check for diagonal win.
    if primary_diagonal == pattern or secondary_diagonal == pattern:
        return True


def play(p1, p2):
    turn_count = 0

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Check who should start first.
    if p1["start"]:
        current_player = p1
        next_player = p2
    else:
        current_player = p2
        next_player = p1

    # Playing.
    while not turn_count == 9:
        name = current_player["name"]

        num = int(input(f"{name} choose a free position from 1 to 9: "))

        # Check if the chosen position is valid.
        if num not in positions:
            print("Position out of range!")
            continue

        # Set the position.
        row = positions[num][0]
        col = positions[num][1]
        position = matrix[row][col]

        # Check if the chosen position is free.
        if position in ["X", "O"]:
            print("Position is already taken!")
            continue

        sign = current_player["sign"]

        # Change the position number with the player's sign.
        matrix[row][col] = sign

        # Increase turn count.
        turn_count += 1

        # Show the board.
        print_board(matrix)

        # Check for winner.
        winner = check_for_winner(matrix, sign)

        if winner:
            print(f"Congratulations, {name}!\n"
                  f"You won!")
            exit(0)
        else:
            # Swap players for next turn.
            current_player, next_player = next_player, current_player

    # This will be executed if the game is tie.
    print("It's a tie! Nobody win.")
