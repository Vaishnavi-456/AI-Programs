m = int(input("Enter no of Max Colors: "))

g = {}

n = int(input("Enter no of edges: "))

for i in range(n):
    a,b = map(int, input().split())
    if g.get(a) == None:
        g[a] = []
    g[a].append(b)

    if g.get(b) == None:
        g[b] = []
    g[b].append(a)

print(g)

posCol = ["red", "orange", "violet", "indigo", "blue", "yellow", "green"]

def canColor(g, n, col, colList):
    for child in g[n]:
        if colList[child] == posCol[col]:
            return False
    
    return True


def graphColoring(g, m, v, n, colList):

    if n == v:
        return True

    for col in range(m):
        if canColor(g, n, col, colList):
            colList[n] = posCol[col]
            if graphColoring(g, m, v, n+1, colList) == True:
                return True
            colList[n] = -1
colList = {}

for i in g.keys():
    colList[i] = -1

if graphColoring(g, m, len(g.keys()), 0, colList):
    print(colList)
else:
    print(f"Can't color using m = {m} colors")
