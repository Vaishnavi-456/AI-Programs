import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan_distance(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = divmod(value - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_moves(state):
    i, j = get_blank_position(state)
    moves = []

    if i > 0:
        moves.append(((i - 1, j), "Up"))
    if i < 2:
        moves.append(((i + 1, j), "Down"))
    if j > 0:
        moves.append(((i, j - 1), "Left"))
    if j < 2:
        moves.append(((i, j + 1), "Right"))

    return moves

def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))

def play_8_puzzle(initial_state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    start_node = PuzzleNode(initial_state, None, None, 0, manhattan_distance(initial_state))
    heap = [start_node]

    while heap:
        current_node = heapq.heappop(heap)

        if current_node.state == goal_state:
            print("Goal state reached!")
            print("Number of moves:", current_node.cost)
            path = []
            while current_node:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            for step, state in reversed(path):
                print(f"Move {step}:\n")
                print_state(state)
                print("\n")
            break

        for (i, j), action in generate_moves(current_node.state):
            new_state = [row[:] for row in current_node.state]
            blank_i, blank_j = get_blank_position(current_node.state)
            new_state[i][j], new_state[blank_i][blank_j] = new_state[blank_i][blank_j], new_state[i][j]
            new_node = PuzzleNode(new_state, current_node, action, current_node.cost + 1, manhattan_distance(new_state))
            heapq.heappush(heap, new_node)

if __name__ == "__main__":
    print("Enter the initial state of the 8-puzzle (use 0 for the blank space):")
    initial_state = [list(map(int, input().split())) for _ in range(3)]
    play_8_puzzle(initial_state)
