N, L = int(input())
D = list(map(int,input().split()))

# 円周における距離行列を作る

dist = [[0] * N for _ in range(N)]

# 1
# 1-2 = d1 = d1 % 6,  min(L-d1, d1) 1-3 = d2 = d1 + d2 % 6,  min(L-d2, d2) 
# 1-4 = d3 = d2 + d3 % 6,  min(L-d3, d3), 1-5 = d4 = d3 + d4 % 6,  min(L-d4, d4)

for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        else:
            dist[i][j] = abs(D[i] - D[j])

# 円の座標リストを作る
# 1を0(始点)とする
circle = [0] * N

for i in range(1, N):
    circle[i] = (circle[i-1] + D[i-1]) % L
    