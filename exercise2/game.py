import random


'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. number of empty cells
'''

VIC = 10 ** 20          # The value of a winning board (for max)
LOSS = -VIC             # The value of a losing board (for max)
TIE = 0                 # The value of a tie
SIZE = 8
COMPUTER = 1            # Marks the computer's cells on the board
HUMAN = 2               # Marks the human's cells on the board


def create():
    # Returns an empty board. The human plays first.
    board = []

    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row = row + [random.randrange(-10, 10)]
        board = board + [row]
    return [board, 0.00001, HUMAN, SIZE*SIZE]


def whoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        s[2] = COMPUTER
    else:
        s[2] = HUMAN
    return None


def value(s):
    # Returns the heuristic value of s
    return s[1]


def isFinished(s):
    # Returns True if the game ended
    return s[1] in [LOSS, VIC, TIE]


def isHumTurn(s):
    # Returns True if it the human's turn to play
    return s[2] == HUMAN


def inputMove(s):
    return None


def printState(board):
    return None


