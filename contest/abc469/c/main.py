N = int(input())
S = list(input()) # 入力例: "abcde" -> ['a', 'b', 'c', 'd', 'e']

# o=当たり、x=ハズレ
# 先頭からk個受け取り、

# k=1の時には最大何個、k=2の時には最大何個、を求める
# まず、kだけ食べる, k+1以降の数だけ食べる
# 単調増加
# oxoみたいな挟み撃ちの場合、
# xo

# 全部× = 1ずつ増えていくだけ
# oがある = 1個増える

# 計算自体はNより長くかかる
# 行数はNだけ
# 行数優先でループか、計算優先でループか
# マックスに達したらもう終わりなんだよな
count = 0
atari = 0
idx = 0
for k in range(N): # ほぼ10^5の計算量
    if count == N:
        print(N)
        continue

    if S[k] == 'o':
        atari += 1
    while atari > 0:
        count += 1
        if S[k+count] == 'o':
            atari += 1
        atari -= 1

    print(count)
    