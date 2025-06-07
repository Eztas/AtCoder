N, L = map(int,input().split())
D = list(map(int,input().split()))

# 円の座標リストを作る
# 1を0(始点)とする
circle = [0] * N

for i in range(1, N):
    circle[i] = (circle[i-1] + D[i-1]) % L

# 正三角形はこの座標リストの中で、距離感が一緒のものが3つある場合である
count = 0
for i in range(N-2):
    for j in range(i + 1, N-1):
        for k in range(j + 1, N):
            # i, j, kの座標を取得
            a = circle[i]
            b = circle[j]
            c = circle[k]
            
            # 距離を計算
            d1 = min(abs(b - a), L-abs(b - a))
            d2 = min(abs(c - b), L-abs(c - b))
            d3 = min(abs(a - c), L-abs(a - c))

            # 正三角形の条件を満たすかチェック
            if d1 == d2 and d2 == d3 and d1 != 0:
                count += 1

print(count)
