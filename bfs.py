# g = {
#     0:[1,2],
#     1:[0,3,4],
#     2:[0,3],
#     3:[1,2,4],
#     4:[1,3]
# }


# def bfs(g, s):
#     q = [s]
#     visited = [s]

#     while q:
#         curr = q.pop(0)
#         print(curr)
#         for c in g[curr]:
#             if c not in visited:
#                 q.append(c)
#                 visited.append(c)

# bfs(g, 0)




g = {
    0:[1,2],
    1:[0,3,4],
    2:[0,3],
    3:[1,2,4],
    4:[1,3]
}


def bfs(g, s):
    q = [s]
    visited = [s]

    while q:
        curr = q.pop(0)
        print(curr)
        for c in g[curr]:
            if c not in visited:
                q.append(c)
                visited.append(c)

bfs(g, 0)