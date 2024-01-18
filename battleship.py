from random import randint

board = []

for i in range(5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

# print_board(board)

def rand_row(board):
    return randint(0, len(board) - 1)

def rand_col(board):
    return randint(0, len(board) - 1)

ship_row = rand_row(board)
ship_col = rand_col(board)

# print(ship_row)
# print(ship_col)

turn = 0
for turn in range(6):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row & guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col >4):
            print("Oops! That's not even in the ocean")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 6:
                print("Game Over")
    print("turn", turn + 1)
    print(print_board(board)) 