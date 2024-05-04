import heapq

class TicTacToeNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def is_winner(board, player):
   
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    return all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))

def is_full(board):
    return all(cell is not None for row in board for cell in row)

def generate_moves(board, player):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                new_board = [row[:] for row in board]
                new_board[row][col] = player
                moves.append(((row, col), new_board))
    return moves

def heuristic(board, player, opponent):
    
    score = 0
    for i in range(3):
        if board[i].count(player) == 2 and board[i].count(None) == 1:
            score += 1
        if [board[j][i] for j in range(3)].count(player) == 2 and [board[j][i] for j in range(3)].count(None) == 1:
            score += 1
    if all(board[i][i] == player or board[i][i] is None for i in range(3)):
        score += 1
    if all(board[i][2 - i] == player or board[i][2 - i] is None for i in range(3)):
        score += 1
    return score

def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == 1 else "O" if cell == 0 else "-" for cell in row]))

def play_tic_tac_toe():
    initial_state = [[None, None, None], [None, None, None], [None, None, None]]
    player = 1

    goal_state = [[1, 1, 1], [None, None, None], [None, None, None]]  

    start_node = TicTacToeNode(initial_state, None, None, 0, heuristic(initial_state, player, 1))
    heap = [start_node]

    while heap:
        current_node = heapq.heappop(heap)

        if is_winner(current_node.state, player):
            print("Player X wins!")
            break

        for (i, j), new_board in generate_moves(current_node.state, player):
            new_node = TicTacToeNode(new_board, current_node, (i, j), current_node.cost + 1, heuristic(new_board, player, 1))
            heapq.heappush(heap, new_node)

    
    current_node = new_node
    moves = []
    while current_node:
        moves.append((current_node.action, current_node.state))
        current_node = current_node.parent
    for step, state in reversed(moves):
        print(f"Move {step}:\n")
        print_board(state)
        print("\n")

if __name__ == "__main__":
    play_tic_tac_toe()
