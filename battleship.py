# Battleship game, simple as that

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print
print "Let's play B-A-T-T-L-E-S-H-I-P !"
print
print "      Instructions:      "
print "* Type 0-4 for coordinates."
print "* You have 4 turns to sink the battleship."
print "* You lose a turn if you type the same coordinates twice"
print "  or if the coordinates are out of range."
print
#print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!

for turn in range(4):
    print "Turn", turn + 1
    print
    print "---------"
    print_board(board)
    print "---------"
    # Make a guess
    print
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    print

    # Test that guess
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or  guess_col > 4):
            print "Oops, that's not even in the ocean. You lose a turn, sorry!"
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already. You lose a turn, sorry!."
        else:
            print "You missed my battleship! Hahahaha!"
            print
	    board[guess_row][guess_col] = "X"
        if turn == 3:
            print_board(board)
            print
	    print "Game Over, baby!"
            print
   
   

