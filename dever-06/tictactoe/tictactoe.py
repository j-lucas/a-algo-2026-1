"""
Tic Tac Toe Player
CS50 AI - Project 0
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    X always goes first. After that, players alternate.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # X goes first; if counts are equal it's X's turn, otherwise O's
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Possible moves are any cells that do not already have an X or O.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Does not modify the original board.
    """
    i, j = action

    # Validate action
    if i not in range(3) or j not in range(3):
        raise Exception(f"Invalid action: ({i}, {j}) is out of bounds.")
    if board[i][j] != EMPTY:
        raise Exception(f"Invalid action: cell ({i}, {j}) is already occupied.")

    # Deep copy so the original board is not modified
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Returns X if X won, O if O won, None otherwise.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over (someone won or board is full), False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if any cell is still empty
    for row in board:
        if EMPTY in row:
            return False

    # All cells filled, no winner → draw
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    utility() is only called on terminal boards.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action (i, j) for the current player on the board.
    Returns None if the board is terminal.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # X is the maximizing player
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
                if best_value == 1:  # Can't do better than winning
                    break
        return best_action
    else:
        # O is the minimizing player
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
                if best_value == -1:  # Can't do better than winning
                    break
        return best_action


def max_value(board):
    """
    Returns the maximum utility value achievable from this board state.
    Used internally by minimax for X (maximizing player).
    """
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == 1:  # Alpha-beta pruning: can't do better
            return v
    return v


def min_value(board):
    """
    Returns the minimum utility value achievable from this board state.
    Used internally by minimax for O (minimizing player).
    """
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == -1:  # Alpha-beta pruning: can't do better
            return v
    return v
