import random
from Player import Player

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def choose_marks():
    marks = ["X", "O"]
    first_mark = random.choice(marks)
    marks.remove(first_mark)

    player1 = Player(first_mark)
    player2 = Player(marks[0])

    return player1, player2


def choose_first():
    return random.choice([player1, player2])


def display_board(board):
    print("\n")
    print(board[0] + " || " + board[1] + " || " + board[2])
    print("____________")
    print(board[3] + " || " + board[4] + " || " + board[5])
    print("____________")
    print(board[6] + " || " + board[7] + " || " + board[8])
    print("\n")


def update_board(position, value):
    board[position] = value


def check_if_win(board):
    if board[0] == board[1] and board[0] == board[2]:
        print("Player with mark " + board[0] + " wins!")
        return True
    elif board[3] == board[4] and board[3] == board[5]:
        print("Player with mark " + board[3] + " wins!")
        return True
    elif board[6] == board[7] and board[6] == board[8]:
        print("Player with mark " + board[6] + " wins!")
        return True
    elif board[1] == board[4] and board[1] == board[7]:
        print("Player with mark " + board[1] + " wins!")
        return True
    elif board[0] == board[3] and board[0] == board[6]:
        print("Player with mark " + board[0] + " wins!")
        return True
    elif board[2] == board[5] and board[2] == board[8]:
        print("Player with mark " + board[2] + " wins!")
        return True

    elif board[0] == board[4] and board[0] == board[8]:
        print("Player with mark " + board[0] + " wins!")
        return True
    elif board[6] == board[4] and board[6] == board[2]:
        print("Player with mark " + board[6] + " wins!")
        return True


def check_if_has_value(position):
    if board[position] == "X" or board[position] == "O":
        print("This position has already a value")
        return True


player1, player2 = choose_marks()

turn = choose_first()
print("Game started, " + turn.__str__() + " plays first")
while True:
    display_board(board)

    if turn == player1:
        position = int(input("Please insert position for your mark:   " + turn.mark + "  "))
        if check_if_has_value(position):
            continue
        update_board(position, turn.mark)
        turn = player2

    elif turn == player2:
        position = int(input("Please insert position for your mark:   " + turn.mark + "  "))
        if check_if_has_value(position):
            continue
        update_board(position, turn.mark)
        turn = player1

    if check_if_win(board):
        display_board(board)
        break
