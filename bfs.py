def bfs(graph, start):
    queue = [start]
    visited = [start]

    while queue:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

# Initialize an empty graph
graph = {}

# Prompt the user to input the number of vertices in the graph
num_vertices = int(input("Enter the number of vertices in the graph: "))

# Prompt the user to input the adjacency list for each vertex
for i in range(num_vertices):
    neighbors = list(map(int, input(f"Enter the neighbors of vertex {i}: ").split()))
    graph[i] = neighbors

# Prompt the user to input the starting vertex for BFS traversal
start_vertex = int(input("Enter the starting vertex for BFS traversal: "))

# Perform BFS traversal starting from the specified vertex
bfs(graph, start_vertex)


