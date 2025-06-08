N, L = map(int,input().split())
D = list(map(int,input().split()))

# 円の座標リストを作る
# 1を0(始点)とする
circle = [0] * N
freq = [0] * L

for i in range(0, N):
    if i == 0:
        circle[i] = 0
        freq[0] += 1
    else:
        circle[i] = (circle[i-1] + D[i-1]) % L
        freq[circle[i]] += 1

# 正三角形はこの座標リストの中で、距離感が一緒のものが3つある場合である
# 3 点 a,b,c が正三角形をなすということは，この 3 点が円周上に等間隔に並んでいるということ
# 距離感はL/3になり, L/3になる関係同志の点で計算すればいい
# 0, 4, 8や1, 5, 9, 0, 3, 6など
# つまり三角形になる関係性の組が決まっている
# 各点の座標発生頻度を比較すれば、実質的に計算できる
count = 0

for i in range(L // 3):
    count += freq[i] * freq[i + L // 3] * freq[i + 2 * L // 3]

print(count)
