N, X, Y = map(int,input().split())
A = list(map(int,input().split()))

minA = min(A)
# min(A)で使える最大のYの個数が、A_iにおける最大個数
total = minA * Y
count = 0
flag = False

# X*(a-b) + Y*b = total = X*a + (Y-X)*b
# 
for a in A:
    i = (total - (X * a) // (Y-X))
    if isinstance(i, int):
        count += i
    else:
        flag = True
        break

if flag:
    print(-1)
else:
    print(count)

# Xグラム, Yグラム
# X*m + Y*n = Lになるようにする, m+n=A_i
# 最大max(A)*Yグラムを配る
# 動的計画法?
# 2≤N≤2×10*5
# 個数最小のやつは、Y*n=Lになる(ここからは個数が増える分、Xの方を使うことになる)
# 条件を満たす配り方が存在する場合、そのような配り方における、大きな飴を配る個数としてあり得る最大値を出力せよ。
# nが最大化できる計算が必要
