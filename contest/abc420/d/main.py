H, W = map(int,input().split())

A = []
for _ in W:
    s = input()
    A.append(list(s))

# 高橋君は、 1回の操作で今いるマスから上下左右に隣り合う、障害物マスでも閉じたドアでもないマスへ移動することができます。
# = ., o, ?, S, Gの5つを移動可能
