from collections import deque
N, Q = map(int,input().split())

# N台のPC
# 最初はバージョン1~NのN種類のバージョンのPC
# Xを含むX以前のPCのバージョンをYにする
# あくまでアップグレードだから、Yが今のものよりも古ければ何もしない
# 12345
# 44345
# やはり代入が良くないが、規則性もなく代入以外の管理がない
# 6->4<-8, みたいなアップグレードごとに、中央が最小値という性質になりやすい
# countは絶対X以下になる

# PC = deque([n+1 for n in range(N)])
PC = [n+1 for n in range(N)]
# PC[X]でカウントを出せるようにする
minVer = 0
for q in range(Q):
    X, Y = map(int,input().split())

    if minVer <= X:
        print(PC[X-1] - minVer)
        minVer = X
        PC[Y-1] += PC[X-1] - minVer
    else:
        print(0)
    