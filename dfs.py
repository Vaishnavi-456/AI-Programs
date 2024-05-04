# g = {
#     0:[1,2],
#     1:[0,3,4],
#     2:[0,3],
#     3:[1,2,4],
#     4:[1,3]
# }

# def dfs(g,s):
#     visited[s]=1
#     print(s)
    
#     for c in g[s]:
#         if not visited [c]:
#             dfs(g,c)


# visited = [0]*5

# dfs(g,0)










g = {
    0:[1,2],
    1:[0,3,4],
    2:[0,3],
    3:[1,2,4],
    4:[1,3]
}

def dfs(g, s):
    visited[s] = 1
    print(s)

    for c in g[s]:
        if not visited[c]:
            dfs(g, c)

visited = [0]*5

dfs(g, 0)

