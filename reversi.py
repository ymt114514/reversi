#初期盤面
BOARD_SIZE = 8
BLACK = "□"
WHITE = "■"
EMPTY = "."
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

def create_board():
    board = [["." for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mid = BOARD_SIZE // 2
    board[mid - 1][mid - 1] = "■"  
    board[mid][mid] = "■"
    board[mid - 1][mid] = "□"      
    board[mid][mid - 1] = "□"
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))
#石を置く処理
def print_board(board):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))  # 列番号
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))  # 行番号つき
def is_on_board(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def get_opponent(player):
    return BLACK if player == WHITE else WHITE
def flip_stones(board, row, col, player):
    opponent = get_opponent(player)
    to_flip = []

    for dx, dy in DIRECTIONS:
        x, y = row + dx, col + dy
        stones = []

        while is_on_board(x, y) and board[x][y] == opponent:
            stones.append((x, y))
            x += dx
            y += dy

        if is_on_board(x, y) and board[x][y] == player:
            to_flip.extend(stones)

    for x, y in to_flip:
        board[x][y] = player

    return len(to_flip) > 0  # ひっくり返せたかどうか



def place_stone(board, row, col, player):
    if board[row][col] != ".":
        print("（そこには置け）ないです")
        return False
    board[row][col] = player
    return True
    
board = create_board()
print_board(board)

# 黒のターン（□）
row = int(input("行を入力シロォ（0〜7）: "))
col = int(input("列も入力スルンダヨォ（0〜7）: "))
success = place_stone(board, row, col, "□")

if success:
    print_board(board)
