import heapq
N, Q = map(int,input().split())

# N台のPC
# 最初はバージョン1~NのN種類のバージョンのPC
# Xを含むX以前のPCのバージョンをYにする
# あくまでアップグレードだから、Yが今のものよりも古ければ何もしない
# 12345
# 44345
# やはり代入が良くないが、規則性もなく代入以外の管理がない

# 最小の要素を取る、heapqが使えるらしい
# ちょっとは過ったが、無意味だと思ってた

# O(NQ)がO((N+Q)logN)で済む

PC = []
for n in range(N):
    heapq.heappush(PC, (n+1, 1)) # 単にPCのバージョンだけでなく、個数も記録

for q in range(Q):
    X, Y = map(int,input().split())
    count = 0

    while(PC):
        if PC[0][0] > X:
            break
        count += PC[0][1] #  最小値の確認は O(1)
        heapq.heappop(PC) # # 取り出しは 最大でO(logN)
    if count > 0:
        heapq.heappush(PC, (Y, count)) # 優先付きだから勝手にソートしてくれる(ちゃんと順番通りにしてくれる)

    print(count)
    