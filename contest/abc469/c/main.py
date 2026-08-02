N = int(input())
S = list(input()) # 入力例: "abcde" -> ['a', 'b', 'c', 'd', 'e']

# oxxox
# 2, 3, 5, 5, 5
# 全部× = 1ずつ増えていくだけ
# oがある = 1個増える

# 計算自体はNより長くかかる
# 行数はNだけ
# 行数優先でループか、計算優先でループか
# マックスに達したらもう終わりなんだよな

# xの位置で考えてみたらいいらしい（回答）
# o = 加速度的に2倍以上に
# xなら制御できる
# k個目のxが出るまでと同じ
# ただどうやったら見つけられたのだろう
# あらかじめメモしておけばいい、ループ分割の考え

count = 0
cross_list = [0] * N
cross_count = 0
for n in range(N): # ほぼ10^5の計算量
    if S[n] == 'x':
        cross_count += 1
    cross_list[n] = cross_count


for k in range(N): # ほぼ10^5の計算量
    cross_count = 0
    count += 1
    if count == N:
        print(N)
        continue

    for s in S:
        count += 1
        if s == 'x':
            cross_count += 1
        if cross_count >= k or count >= N:
            break

    print(count)
