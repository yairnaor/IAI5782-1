import copy
import random

'''
The state of the game is represented by a list of 4 items:
0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
   the comp's cells = COMPUTER and the human's = HUMAN
1. The heuristic value of the state.
2. Who's turn is it: HUMAN or COMPUTER
3. number of empty cells
'''

SIZE = 8
COMPUTER = 1  # Marks the computer's turn. vertical choice
HUMAN = 0  # Marks the human's turn. horizontal choice
BOARD = 0
H_POINTS = 1
C_POINTS = 2
TURN = 3
LAST_MOVE = 4
ROW = 0
COLUMN = 1


def create():
    # Returns an empty board. The human plays first.
    board = []
    human_points = 0
    computer_points = 0
    last_move = [0, 0]

    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row = row + [random.randrange(-5, 16)]
        board = board + [row]

    last_move[ROW] = random.randrange(0, SIZE)
    last_move[COLUMN] = random.randrange(0, SIZE)

    board[last_move[ROW]][last_move[COLUMN]] = "X"         # the starting point on the board
    return [board, human_points, computer_points, HUMAN, last_move]


def value(state):
    # Returns the heuristic value of s
    return state[C_POINTS] - state[H_POINTS]


def printState(state):
    # If the game ended prints who won.
    if isFinished(state):
        if state[H_POINTS] > state[C_POINTS]:
            print("You are the winner... You have", format(state[H_POINTS]), "points")
            print("I scored", format(state[C_POINTS]), "points")
        elif state[H_POINTS] < state[C_POINTS]:
            print("You lost the game. Ha Ha Ha, I've got", format(state[C_POINTS]), "points")
            print("You scored", format(state[H_POINTS]), "points")
        else:
            print("We think alike")
            print("We both have", format(state[C_POINTS]), "points")
    # Prints the board.
    else:
        for i in range(1, SIZE+1):
            print("\t", i, end="\t")
        print()
        print("\t", end="")
        for i in range(SIZE):
            print("- - - - ", end="")
        print()
        for i in range(SIZE):
            print(i+1, "|", end="")
            for j in range(SIZE):
                print("\t", state[0][i][j], end="\t")
            print()
        print()
        print("Your score: ", state[1], "Computer score: ", state[2])


def isFinished(state):
    # Returns True if the game ended

    if isHumTurn(state):       # checks if the choice has to be from row
        row = state[LAST_MOVE][ROW]
        for column in state[BOARD][row]:
            if column != " " or column != "X":
                return False
    else:
        column = state[LAST_MOVE][COLUMN]
        for row in state[BOARD]:
            if row[column] != " " or row != "X":
                return False

    return True


def isHumTurn(state):
    # Returns True if it the human's turn to play
    return state[TURN] == HUMAN


def whoIsFirst(state):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you. : ")) == 1:
        state[TURN] = COMPUTER
    else:
        state[TURN] = HUMAN


def makeMove(state, move):
    # Assumes the move is legal.
    if isHumTurn(state):       # checks if the choice has to be from row
        row = state[LAST_MOVE][ROW]
        col = state[LAST_MOVE][COLUMN]
        if state[BOARD][row][move] != " " and state[BOARD][row][move] != "X":
            state[H_POINTS] += state[BOARD][row][move]
        state[BOARD][row][move] = "X"
        state[BOARD][row][col] = " "

        state[TURN] = COMPUTER
        state[LAST_MOVE][COLUMN] = move
    else:
        row = state[LAST_MOVE][ROW]
        col = state[LAST_MOVE][COLUMN]
        if state[BOARD][move][col] != " " and state[BOARD][move][col] != "X":
            state[C_POINTS] += state[BOARD][move][col]
        state[BOARD][move][col] = "X"
        state[BOARD][row][col] = " "

        state[TURN] = HUMAN
        state[LAST_MOVE][ROW] = move


def inputMove(state):
    # Reads, enforces legality and executes the user's move.
    printState(state)
    row = state[LAST_MOVE][ROW] + 1
    col = state[LAST_MOVE][COLUMN] + 1
    flag = True
    while flag:
        print("Last move was: row", row, ", column", col)
        print("Enter your next move: (choose a number 1 -", SIZE, "in row", row, ")")
        move = int(input())          # chooses between 1 to SIZE of board
        move -= 1
        row = state[LAST_MOVE][ROW]
        if move < 0 or SIZE <= move or state[BOARD][row][move] == " " or state[BOARD][row][move] == "X":
            print("Illegal move.")
        else:
            flag = False
            makeMove(state, move)


def getNext(state):
    # returns a list of the next states of s
    ns = []
    if isHumTurn(state):
        row = state[LAST_MOVE][ROW]
        for col in range(SIZE):
            if state[BOARD][row][col] != " " or state[BOARD][row][col] != "X":
                tmp = copy.deepcopy(state)
                makeMove(tmp, col)
                ns += [tmp]
    else:
        col = state[LAST_MOVE][COLUMN]
        for row in range(SIZE):
            if state[BOARD][row][col] != " " or state[BOARD][row][col] != "X":
                tmp = copy.deepcopy(state)
                makeMove(tmp, row)
                ns += [tmp]

    return ns
