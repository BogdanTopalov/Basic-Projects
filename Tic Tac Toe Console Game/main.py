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
