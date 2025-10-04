N, Q = map(int,input().split())

# N台のPC
# 最初はバージョン1~NのN種類のバージョンのPC
# Xを含むX以前のPCのバージョンをYにする
# あくまでアップグレードだから、Yが今のものよりも古ければ何もしない
# 12345
# 44345
# やはり代入が良くないが、規則性もなく代入以外の管理がない
minVer = 1

PC = [n+1 for n in range(N)]

for q in range(Q):
    X, Y = map(int,input().split())
    count = 0

    if minVer <= X:
        for i in range(X):
            if PC[i] <= X:
                PC[i] = Y
                count += 1
            else:
                break
        minVer = X + 1
        PC.sort()

    print(count)
    