'''
Yair Naor - 208983783
Amitai Salomon - 316336445
'''
import random
import math


# returns a random board nXn
def create(n):
    s = list(range(n * n))  # s is the board itself. a vector that represent a matrix. s=[0,1,2....n^2-1]
    m = "<>v^"  # m is "<>v^" - for every possible move (left, right, down, up)
    for i in range(n ** 3):  # makes n^3 random moves to mix the tiles
        if_legal(s, m[random.randrange(4)])
    return [s, ""]  # at the beginning "" is an empty path, later on path
    # contains the path that leads from the initial state to the state


def get_next(x):  # returns a list of the children states of x
    ns = []  # the next state list
    for i in "<>v^":
        s = x[0][:]  # [:] - copies the board in x[0]
        if_legal(s, i)  # try to move in direction i
        # checks if the move was legal and...
        if s.index(0) != x[0].index(0) and \
                (x[1] == "" or x[1][-1] != "><^v"[
                    "<>v^".index(i)]):  # check if it's the first move or it's a reverse move
            ns.append([s, x[1] + i])  # appends the new state to ns
    return ns


def path_len(x):
    return len(x[1])


def is_target(x):
    n = len(x[0])  # the size of the board
    return x[0] == list(range(n))  # list(range(n)) is the target state


#############################
def if_legal(x, m):  # gets a board and a move and makes the move if it's legal
    n = int(math.sqrt(len(x)))  # the size of the board is nXn
    z = x.index(0)  # z is the place of the empty tile (0)
    if z % n > 0 and m == "<":  # checks if the empty tile is not in the first col and the move is to the left
        x[z] = x[z - 1]  # swap x[z] and x[z-1]...
        x[z - 1] = 0  # ...and move the empty tile to the left
    elif z % n < n - 1 and m == ">":  # check if the empty tile is not in the n's col and the move is to the right
        x[z] = x[z + 1]
        x[z + 1] = 0
    elif z >= n and m == "^":  # check if the empty tile is not in the first row and the move is up
        x[z] = x[z - n]
        x[z - n] = 0
    elif z < n * n - n and m == "v":  # check if the empty tile is not in the n's row and the move is down
        x[z] = x[z + n]
        x[z + n] = 0


# This is your HW
def hdistance(s):  # the heuristic value of s

    n = math.sqrt(len(s[0]))
    sum = 0
    # we go through each number in cube to check
    for i in s[0]:
        # y gets the expected row of the current index
        y = i % n
        # x receives the row expected from the actual content of the current index
        x = s[0][i] % n

        z = 0
        w = 0
        j = 0
        # first while inserts into z the expected column of the current index
        while j < n:
            if j * n <= i < (j + 1) * n:
                z = j
            j += 1
        # second while inserts into w the expected column of the content in the current index
        j = 0
        while j < n:
            if j * n <= s[0][i] < (j + 1) * n:
                w = j
            j += 1
        # we check the max between the row and column difference and add it to sum.
        sum += max(abs(w - z), abs(y - x))
    return sum


'''
def hdistance(s):
    c = 0
    for i in range(1, len(s[0])):
        if s[0][i] != i:
            c += 1
    return c
'''

'''
2) כן, ההיוריסטיקה קבילה. כיוון שתמיד נקבל מרחק שהינו שווה או קצר ממרחק היעד של המספר.

3) 
הרצה לפי הפונקציה שנלמדה בכיתה:
[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 40175, 16920]

הרצה לפי הפונקציה שמימשנו:
[[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
[[[0, 1, 2, 3, 4, 5, 6, 7, 8], '^>v<^<^>>v<^<vv>^<^>v<^'], 6095, 2522]

ניתן לראות שיש שיפור משמעותי בין שתי הפונקציות, כאשר הפונקציה שאנו כתבתנו יותר יעילה.
דבר זה נובע מכך שהפונקציה שאנו כתבנו נותנת עדיפות בתור העדיפויות למצבים אשר מקרבים אותנו מבחינה היוריסטית אל המטרה.
כלומר, מצבים בהם המספרים קרבים אל המקום הסופי בהם הם צריכים להיות מקרבים אותנו אל המטרה הסופית שבה כל המספרים צריכים להיות מסודרים.
ריחוק של מספר ממיקומו גורם לכך שאנו מבחינה היוריסטית מתרחקים מהמטרה, ונרצה לתת לכך עדיפות קטנה יותר.
לעומת זאת ההיוריסטיקה הנתונה מההרצאה, אינה נותנת עדיפות לכיוון המטרה, אלא מסדרת את המצבים לפי כמות השוני שלהם ביחס למצב המטרה.
כלומר, אם במידה מסוימת מספר הגיע אל מקומו הסופי מצב זה יקבל עדיפות גדולה יותר.
בכך אין הבדל גדול בין המצבים, מכיוון שמצב בו הזזנו את המספרים יותר קרוב למטרה אך המספרים עדיין אינם במקומם הסופי,
יחשב באותה צורה בעדיפותו למקרה הקודם לו.

'''
