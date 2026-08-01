N = int(input())
S = list(input()) # 入力例: "abcde" -> ['a', 'b', 'c', 'd', 'e']

# o=当たり、x=ハズレ
# 先頭からk個受け取り、

# k=1の時には最大何個、k=2の時には最大何個、を求める
# まず、kだけ食べる, k+1以降の数だけ食べる
# 単調増加
# oxoみたいな挟み撃ちの場合、
# oの数×2だけ増やす

# 全部× = 1ずつ増えていくだけ
# oがある = 1個増える

# 計算自体はNより長くかかる
# 行数はNだけ
# 行数優先でループか、計算優先でループか
# マックスに達したらもう終わりなんだよな

# まず
count = 0
atari = 0

o_counts_list = []
o_counts = 0

for k in range(N):
    if S[k] == 'o':
        o_counts += 1
    o_counts_list.append(o_counts)

print(o_counts_list)

for k in range(N): # ほぼ10^5の計算量
    count += 1
    idx = 0
    if count == N:
        print(N)
        continue

    if S[k] == 'o':
        atari += 1
    while atari > 0:
        count += 1
        idx += 1
        if k+idx >= N-1:
            break
        if S[k+idx] == 'o':
            atari += 1
        atari -= 1

    if k+idx == N:
        print(N)
    else:
        print(count)
