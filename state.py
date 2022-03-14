'''
The state is a list of 2 items: the board, the path
The target is :
012
345
678

'''
import random
import math


def get_next(x):
    ns = []
    for i in "<>v^":
        s = x[0][:]
        if_legal(s, i)
        if s.index(0) != x[0].index(0) and \
                (x[1] == "" or x[1][-1] != "><^v"["<>v^".index(i)]):
            ns.append([s, x[1] + i])
    return ns


# returns a random board nXn
def create(n):
    s = list(range(n * n))
    m = "<>v^"
    for i in range(n ** 3):
        if_legal(s, m[random.randrange(4)])
    return [s, ""]


def path_len(x):
    return len(x[1])


def is_target(x):
    n = len(x[0])
    return x[0] == list(range(n))

def hdistance(s):
    n = math.sqrt(len(s[0]))
    sum = 0
    for i in s[0]:
        y = i % n
        x = s[0][i] % n

        z = 0
        w = 0
        j = 0
        while j < n:
            if j * n <= i < (j + 1) * n:
                z = j
            j += 1

        j = 0
        while j < n:
            if j * n <= s[0][i] < (j + 1) * n:
                w = j
            j += 1

        col = abs(y - x)
        row = abs(w - z)
        sum += max(row, col)

    return sum


#############################
def if_legal(x, m):
    n = int(math.sqrt(len(x)))
    z = x.index(0)
    if z % n > 0 and m == "<":
        x[z] = x[z - 1]
        x[z - 1] = 0
    elif z % n < n - 1 and m == ">":
        x[z] = x[z + 1]
        x[z + 1] = 0
    elif z >= n and m == "^":
        x[z] = x[z - n]
        x[z - n] = 0
    elif z < n * n - n and m == "v":
        x[z] = x[z + n]
        x[z + n] = 0
