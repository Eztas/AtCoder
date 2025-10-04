N, Q = map(int,input().split())

# N台のPC
# 最初はバージョン1~NのN種類のバージョンのPC
# Xを含むX以前のPCのバージョンをYにする
# あくまでアップグレードだから、Yが今のものよりも古ければ何もしない

minVer = 1

PC = [n+1 for n in range(N)]

for q in range(Q):
    X, Y = map(int,input().split())
    count = 0

    for i in range(X):
        if PC[i] <= X:
            PC[i] = Y
            count += 1

    print(count)
    