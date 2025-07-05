Q = int(input())

A = []

# 1 c x, xをc個追加, 下手すればO(10^9)なので正攻法はダメ
# このとき、k はその時点での A の長さ以下であることが保証される。
# kは10^9の桁半分以下、つまり、10^5以下なので、O(10^5)で計算できる。

for _ in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        c = query[1]
        x = query[2]
        A.extend([x] * c)
    elif query[0] == 2:
        k = query[1]
        print(sum(A[:k]))
        A = A[k:]
