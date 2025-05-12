BOARD_SIZE = 8
BLACK = "□" 
WHITE = "■"  
EMPTY = "."

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]　　　#定数と方向の定義

def create_board():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mid = BOARD_SIZE // 2
    board[mid - 1][mid - 1] = WHITE
    board[mid][mid] = WHITE
    board[mid - 1][mid] = BLACK
    board[mid][mid - 1] = BLACK
    return board　　　　　　　　　　　　　　#初期盤面

def print_board(board, hint_moves=None):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        line = []
        for j, cell in enumerate(row):
            if hint_moves and (i, j) in hint_moves and cell == EMPTY:
                line.append("*")
            else:
                line.append(cell)
        print(str(i) + " " + " ".join(line))
        #盤面の表示と合法手のヒント

def is_on_board(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE      #石を探索する際に盤面の外に出ないようチェックする関数

def get_opponent(player):
    return BLACK if player == WHITE else WHITE　　　　　　#今の相手

def valid_moves(board, player):
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY and can_flip(board, row, col, player):
                moves.append((row, col))               #置けるところ
    return moves

def can_flip(board, row, col, player):
    opponent = get_opponent(player)
    for dx, dy in DIRECTIONS:
        x, y = row + dx, col + dy
        has_opponent = False
        while is_on_board(x, y) and board[x][y] == opponent:
            x += dx
            y += dy
            has_opponent = True
        if has_opponent and is_on_board(x, y) and board[x][y] == player:
            return True
    return False　　　　　　　　　　　　　　　　　　#8方向を調べどこに置けるか、また間に敵の石があるならtrue

def flip_stones(board, row, col, player):
    opponent = get_opponent(player)
    flipped = []
    for dx, dy in DIRECTIONS:
        x, y = row + dx, col + dy
        temp = []
        while is_on_board(x, y) and board[x][y] == opponent:
            temp.append((x, y))
            x += dx
            y += dy
        if temp and is_on_board(x, y) and board[x][y] == player:
            flipped.extend(temp)
    for x, y in flipped:
        board[x][y] = player
    return len(flipped) > 0　　　　　　　　　　#ひっくり返す石の記録

def place_stone(board, row, col, player):
    if board[row][col] != EMPTY:
        return False
    if not flip_stones(board, row, col, player):
        return False
    board[row][col] = player
    return True　　　　　　　　　　　　　　　　#石を置く関数で石を置けたときtrueを返す

def count_stones(board):
    black = sum(row.count(BLACK) for row in board)
    white = sum(row.count(WHITE) for row in board)
    return black, white　　　　　　　　　　　　　#カウンター
def game_loop():
    board = create_board()
    current_player = BLACK　　　　　　　　　　　
    while True:
        print_board(board)
        black_count, white_count = count_stones(board)
        print(f"\n黒（{BLACK}）: {black_count}　白（{WHITE}）: {white_count}")

        moves = valid_moves(board, current_player)
        if not moves:
            opponent_moves = valid_moves(board, get_opponent(current_player))
            if not opponent_moves:
                print("（打てる場所）ないです")
                break
            print(f"{current_player} は打てる場所がないのでスキップおつぅぅぅ‼‼‼‼‼")
            current_player = get_opponent(current_player)
            continue　　　　　　　　　　　　　　　　　　#ゲームマスター関数


        print(f"{current_player} の番")
        while True:
            try:
                row = int(input("行 (0-7): "))
                col = int(input("列 (0-7): "))
                if (row, col) in moves and place_stone(board, row, col, current_player):
                    break
                else:
                    print("（置け）ないです")
            except ValueError:
                print("数字入力あくしろよ")

        current_player = get_opponent(current_player)

    # 終了後の結果表示
    print_board(board)
    black_count, white_count = count_stones(board)
    print(f"\n最終結果：黒（{BLACK}）: {black_count}　白（{WHITE}）: {white_count}")
    if black_count > white_count:
        print("黒勝！")
    elif white_count > black_count:
        print("白勝！")
    else:
        print("引分！")

# ゲームスタート
game_loop()
