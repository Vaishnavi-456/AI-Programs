N = int(input("Enter value for N:"))

queen = "Q"
empty = "_"


b = [[empty] * N for i in range(N)]


def isSafe(i, j):
    for x in range(N):
        if b[i][x] == queen or b[x][j] == queen:
            return False
    
    for x in range(N):
        for y in range(N):
            if (x + y == i + j) or (x - y == i - j) or (x - i == y - j) or (i - x == y - j):
                if b[x][y] == queen:
                    return False
    
    return True
 

def nqueen(noq):
    if noq == 0:
        return True

    for i in range(N):
        for j in range(N):
            if b[i][j] != queen and isSafe(i,j):
                b[i][j] = queen
                if nqueen(noq-1) == True:
                    return True
                b[i][j] = empty
    
    return False

def printBoard(b):
    for i in b:
        print(i)

if nqueen(N):
    printBoard(b)
else:
    print("Can't Place")
