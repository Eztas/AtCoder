N, Q = map(int,input().split())

# 移動しかしないから
# 足し算のパターンは限られている

# 実際に移動させる必要はない

# headの位置を追跡するパターンはgemini曰くダメらしい
# A = [10, 20, 30, 40, 50], N=5, head=0 の状態で 1 2 のクエリ
# [40, 50, 10, 20, 30]
# 2 3 5 のクエリ（仮想的な3番目から5番目の和)
# 求めるべき和は 10 + 20 + 30 = 60
# l=2, r=4 (0-indexed)
# head = 3
# print(sum(A[head+l:N])+sum(A[head:r-head+1]))
# sum(A[3+2:5]) → sum(A[5:5]) → これは空のスライスなので 0 です。
# sum(A[3 : 4-3+1]) → sum(A[3:2]) → これも空のスライスなので 0 です。
# head+lがそもそもNを超える場合を考えられていないので、head+lで分ける考えは間違い
# lとrでまたぐかまたがないかが本質
# r < lとなる関係性の時の対応が今できてない
# そもそもこれは結局計算量超過

A = list(map(int,input().split()))
head = 0
for q in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        c = query[1]
        head = (head - c) % N

    else: # 2の時
        l = query[1] - 1
        r = query[2] - 1

        if head <= l:
            print(sum(A[l-head:r-head+1]))
        else:
            if head <= r:
                print(sum(A[head+l:N])+sum(A[head:r-head+1]))
            else:
                print(sum(A[head+l:head+r+1]))
