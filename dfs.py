def dfs(graph, start, visited):
    visited[start] = True
    print(start)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Initialize an empty graph
graph = {}

# Prompt the user to input the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

# Prompt the user to input the adjacency list for each vertex
for i in range(num_vertices):
    neighbors = list(map(int, input(f"Enter the neighbors of vertex {i}: ").split()))
    graph[i] = neighbors

# Initialize a list to track visited vertices
visited = [False] * num_vertices

# Prompt the user to input the starting vertex for DFS traversal
start_vertex = int(input("Enter the starting vertex for DFS traversal: "))

# Perform DFS traversal starting from the specified vertex
dfs(graph, start_vertex, visited)
