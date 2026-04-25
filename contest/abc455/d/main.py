import sys

# 大量入力なので高速化
input = sys.stdin.readline

N, Q = map(int, input().split())

# 各カードの下、上を管理 (1-indexed)
under = [0] * N
above = [0] * N
# 各山の「一番下」と「一番上」のカード
mountain_bottom = [0] * N
mountain_top = [0] * N
# カードが今どの山にあるか (一番下のカードを辿ればわかるようにする)
# または「どのカードがどの山の底か」を管理

# 操作...
for _ in range(Q):
    C, P = map(int, input().split())
    
    # 1. Cの下にあるカードとの接続を切る
    X = under[C-1]
    if X != 0:
        # Cの下にカードがあれば、そのカードが新しい「山の頂上」になる
        above[X] = 0
        # ※ Xがどの山の頂上になったか管理が必要
    else:
        # Cが底だった場合、その山は空になる処理
        pass

    # 2. 山Pの頂上にCを繋ぐ
    Y = mountain_top[P-1]
    under[C] = Y
    above[Y] = C
    
    # 3. 山の頂上情報を更新
    # Cのさらに上に乗っている「塊の主」を山Pの新しい頂上にする
    # ...
  
# 最後に各山の枚数
print_horizontal_line(mountains, ' ')
