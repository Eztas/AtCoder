from collections import deque

H, W = map(int,input().split())

A = []
for _ in W:
    s = input().split()
    A.append(list(s))

# 高橋君は、 1回の操作で今いるマスから上下左右に隣り合う、障害物マスでも閉じたドアでもないマスへ移動することができます。
# = ., o, ?, S, Gの5つを移動可能

# 幅優先×迷路のコツ
# 1. スタートとゴール座標の設定
for h in range(H):
    for w in range(W):
        if A[h][w] == "S":
            sx, sy = h, w
        if A[h][w] == "G":
            gx, gy = h, w

# 2. 無限の設定
INF = 10**9

# 3. 行(上下), 列(左右)の移動を示す配列
# 上,左はマイナスのみで表現
# 1つのループで上下左右の計算を行うために、長さ4である必要がある
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 4. 2で特殊な床に対応できるようにしつつ、(特殊な床OFF, ONの2値)
# d: 迷路の各地点までの最短経路のコスト（距離）を記録するための3次元リスト
# q: 探索すべき次の地点の候補を順番に格納する
d = [[[INF] * w for _ in range(h)] for _ in range(2)]
q = deque()
q.append((0, sx, sy))
d[0][sx][sy] = 0 # 最初のスタート、特殊な床の影響もないので0番目
