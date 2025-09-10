from collections import deque

H, W = map(int,input().split())

A = []
for _ in range(H):
    s = input()
    A.append(s)

# 1. スタートとゴール座標の設定
sh, sw, gh, gw = -1, -1, -1, -1
for h in range(H):
    for w in range(W):
        if A[h][w] == "S":
            sh, sw = h, w
        if A[h][w] == "G":
            gh, gw = h, w

# 2. 無限大(訪れていないことを示す)の設定
INF = 10**9

# 3. 上下左右の移動を示す配列
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 4. 迷路の各地点までの最短経路のコストを記録する2次元リスト
d = [[INF] * W for _ in range(H)] #初期値は無限大, 訪れていないから
q = deque()
q.append((sh, sw)) # スタートから考える
d[sh][sw] = 0

while q:
    h, w = q.popleft() # 探索すべき地点
    # 上下左右方向を調べる
    for k in range(4):
        hh, ww = h + dh[k], w + dw[k]

        # 迷路の外に出るか、障害物(#)ならスキップ
        # 障害物からのルートは計算させない
        if not (0 <= hh < H and 0 <= ww < W) or A[hh][ww] == "#":
            continue

        # 既に訪れた場所はスキップ
        if d[hh][ww] != INF:
            continue

        q.append((hh, ww))
        d[hh][ww] = d[h][w] + 1

ans = d[gh][gw]
print(-1 if ans == INF else ans)