from collections import deque

# キューと4方向ごとのコストを調べるだけでbfsの計算は完成する
# 移動コストが全て同じ時にbfsは大活躍する
# 今回みたいな床もif文として加えたりするだけでよく、融通も効く
H, W = map(int,input().split())

A = []
for _ in range(H):
    s = input()
    A.append(s)

# 高橋君は、 1回の操作で今いるマスから上下左右に隣り合う、障害物マスでも閉じたドアでもないマスへ移動することができます。
# = ., o, ?, S, Gの5つを移動可能

# 幅優先×迷路のコツ
# 1. スタートとゴール座標の設定
sh, sw, gh, gw = -1, -1, -1, -1
for h in range(H):
    for w in range(W):
        if A[h][w] == "S":
            sh, sw = h, w
        if A[h][w] == "G":
            gh, gw = h, w

# 2. 無限の設定
INF = 10**9

# 3. 行(上下, H), 列(左右, W)の移動を示す配列
# 上,左はマイナスのみで表現
# 1つのループで上下左右の計算を行うために、長さ4である必要がある
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 4. 2で特殊な床に対応できるようにしつつ、(特殊な床OFF, ONの2値)
# d: 迷路の各地点までの最短経路のコスト（距離）を記録するための3次元リスト
# q: 探索すべき次の地点の候補を順番に格納する
# 3次元なのは状態があるから、なければ2次元で十分
d = [[[INF] * W for _ in range(H)] for _ in range(2)]
q = deque()
q.append((0, sh, sw))
d[0][sh][sw] = 0 # 最初のスタート、特殊な床の影響もないので0番目

while q:
    c, h, w = q.popleft() # 探索すべき地点
    # 上下左右それぞれでコスト計算
    for k in range(4):
        hh, ww = h + dh[k], w + dw[k]
        # 障害物の時はこの計算はスルー
        if (
            not (0 <= hh < H and 0 <= ww < W)
            or A[hh][ww] == "#"
            or (c == 0 and A[hh][ww] == "x")
            or (c == 1 and A[hh][ww] == "o")
        ):
            continue
        # ドア管理
        cc = c ^ (A[hh][ww] == "?")
        # d[cc][hh][ww] == INFなら訪れてない
        # = その地点のコストdを計算する必要がある
        # BFSは距離が短い順に探索するため、ある地点に最初にたどり着いたルートが、必ずその地点への最短経路
        # 上下左右1回の移動コストがすべて同じだから成り立つ
        if d[cc][hh][ww] != INF:
            continue
        q.append((cc, hh, ww))
        d[cc][hh][ww] = d[c][h][w] + 1 # 現在のセルまでにたどり着くコスト, 今のセル+1コスト
ans = min(d[0][gh][gw], d[1][gh][gw]) #ゴールに辿り着く時に状態0と1の2パターンがあるので、その最小
print(-1 if ans == INF else ans)
