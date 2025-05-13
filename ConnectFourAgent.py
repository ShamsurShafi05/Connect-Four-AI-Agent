from Board import GenerateBoard
# player, actions, result, winner, terminal, utility, and minimax.

def Player(state):
    return state.player_move
    
def Actions(state):
    list1 = []
    for i in range(len(state.board)):
        for j in range(len(state.board)):
            if state.board[i][j] is None:
                list1.append((i, j))
    return list1

def Result(state, action):
    new_state = GenerateBoard(state.size)
    new_state.board = [row.copy() for row in state.board]
    new_state.player = 2 if state.player == 1 else 1  # Switch player
    new_state.player_move = "O" if state.player_move == "X" else "X"  # Switch move symbol
    i, j = action
    new_state.board[i][j] = state.player_move
    return new_state


def Winner(state):
    for i in range(state.size):
        for j in range(state.size):
            if state.board[i][j] is not None:
                # Check horizontal
                if j + 3 < state.size and all(state.board[i][j] == state.board[i][j+k] for k in range(4)):
                    return state.board[i][j]
                # Check vertical
                if i + 3 < state.size and all(state.board[i][j] == state.board[i+k][j] for k in range(4)):
                    return state.board[i][j]
                # Check diagonal (top-left to bottom-right)
                if i + 3 < state.size and j + 3 < state.size and all(state.board[i][j] == state.board[i+k][j+k] for k in range(4)):
                    return state.board[i][j]
                # Check diagonal (bottom-left to top-right)
                if i - 3 >= 0 and j + 3 < state.size and all(state.board[i][j] == state.board[i-k][j+k] for k in range(4)):
                    return state.board[i][j]
    return None

def Terminal(state):
    if Winner(state) is not None:
        return True
    for row in state.board:
        if None in row:
            return False
    return True

def Utility(state):
    winner = Winner(state)
    if winner == "X":
        return 1000
    elif winner == "O":
        return -1000
    else:
        return 0


def Evaluate(state):
    if Terminal(state):
        return Utility(state)

    size = state.size
    center_col = size // 2
    my_piece = state.player_move
    opp_piece = "O" if my_piece == "X" else "X"

    # Base weights for k-in-a-row (no mixed windows)
    BASE_WEIGHTS = {
        1: 1,      # single piece
        2: 50,     # two connected
        3: 500,    # three connected
    }
    OPEN3_BONUS = 2000       # open‐ended 3-in-row
    CENTER_MULT = 2          # factor for windows touching center

    score = { my_piece: 0, opp_piece: 0 }

    def score_window(cells, coords):
        
        cnt_my = cells.count(my_piece)
        cnt_op = cells.count(opp_piece)
        if cnt_my > 0 and cnt_op > 0:
            return  # mixed window, no score

        count = cnt_my if cnt_my else cnt_op
        owner = my_piece if cnt_my else opp_piece

        # Base value
        val = BASE_WEIGHTS.get(count, 0)
        # Open‐ended 3‐threat
        if count == 3 and cells.count(None) == 1:
            val += OPEN3_BONUS

        # Center‐column bias
        for (_, c) in coords:
            if c == center_col:
                val *= CENTER_MULT
                break

        score[owner] += val

    # Scan all 4‑length windows
    b = state.board
    N = size

    # Horizontal
    for r in range(N):
        for c in range(N - 3):
            cells = [b[r][c + i] for i in range(4)]
            coords = [(r, c + i) for i in range(4)]
            score_window(cells, coords)

    # Vertical
    for c in range(N):
        for r in range(N - 3):
            cells = [b[r + i][c] for i in range(4)]
            coords = [(r + i, c) for i in range(4)]
            score_window(cells, coords)

    # Diagonal-down-right
    for r in range(N - 3):
        for c in range(N - 3):
            cells = [b[r + i][c + i] for i in range(4)]
            coords = [(r + i, c + i) for i in range(4)]
            score_window(cells, coords)

    # Diagonal-up-right
    for r in range(3, N):
        for c in range(N - 3):
            cells = [b[r - i][c + i] for i in range(4)]
            coords = [(r - i, c + i) for i in range(4)]
            score_window(cells, coords)

    # Final heuristic
    return score[my_piece] - score[opp_piece]



def Minimax(state, depth=4, alpha=float('-inf'), beta=float('inf')):
    if Terminal(state) or depth == 0:
        return Evaluate(state), None

    if state.player == 1:           # Maximizing player (X)
        max_eval = float('-inf')
        best_move = None
        for action in Actions(state):
            eval_score, _ = Minimax(Result(state, action), depth-1, alpha, beta)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = action
            alpha = max(alpha, eval_score)
            if beta <= alpha:  # Beta cutoff
                break
        return max_eval, best_move
    
    else:                           # Minimizing player (O)
        min_eval = float('inf')
        best_move = None
        for action in Actions(state):
            eval_score, _ = Minimax(Result(state, action), depth-1, alpha, beta)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = action
            beta = min(beta, eval_score)
            if beta <= alpha:  # Alpha cutoff
                break
        return min_eval, best_move


