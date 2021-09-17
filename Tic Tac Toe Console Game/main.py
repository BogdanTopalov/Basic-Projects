from random import randint

player1 = {}
player2 = {}

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

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

