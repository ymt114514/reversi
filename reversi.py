# reversi first board settings
BOARD_SIZE = 8

def create_board():
    board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mid = BOARD_SIZE // 2
    board[mid - 1][mid - 1] = "W"
    board[mid][mid] = "W"
    board[mid - 1][mid] = "B"
    board[mid][mid - 1] = "B"
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

board = create_board()
print_board(board)
