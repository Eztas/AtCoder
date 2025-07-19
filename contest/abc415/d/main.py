N, M = map(int,input().split())

# 初期値=N本の空いていないコーラ
# i回飲む -> N-iの空いていない, iの空いている

# 行動選択
# 最大値=動的計画法

# seal 最大, seal = d[x][y]
# iが同じ動作はできる, 動的計画法しづらい

notEmpty = N
empty = 0

A = [] # 渡す瓶
B = [] # 貰う瓶(シールは毎回1枚)

# 優先行動, A/Bが一番いい行動をとるようにする
# A/Bが悪い、かつ消費が多いものは排他
# 

for m in M:
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)

while True:
