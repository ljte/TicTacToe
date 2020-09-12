import sys

from main import check_winner


scores = {
    'X': 1,
    'O': -1,
    'Tie': 0
}

ai_player = 'O'
human_player = 'X'


def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result:
        return scores[result]

    if is_maximizing:
        best_score = -sys.maxsize

        for i in range(3):
            for j in range(3):
                if board[i][j].is_empty:
                    board[i][j].value = human_player
                    score = minimax(board, depth + 1, False)
                    board[i][j].value = None
                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = sys.maxsize

        for i in range(3):
            for j in range(3):
                if board[i][j].is_empty:
                    board[i][j].value = ai_player
                    score = minimax(board, depth + 1, True)
                    board[i][j].value = None
                    best_score = min(score, best_score)

        return best_score


def make_best_move(board):
    best_score = sys.maxsize
    best_move = ()

    for i in range(3):
        for j in range(3):
            if board[i][j].is_empty:
                board[i][j].value = ai_player
                score = minimax(board, 0, True)
                if score < best_score:
                    best_score = score
                    best_move = (i, j)
                board[i][j].value = None

    board[best_move[0]][best_move[1]].value = ai_player


def make_simple_turn(grid):
    empty_cell = grid.get_empty_cell()
    if empty_cell:
        empty_cell.value = ai_player
