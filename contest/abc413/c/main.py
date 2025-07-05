Q = int(input())

C = []
X = []

# 1 c x, xをc個追加, 下手すればO(10^9)なので正攻法はダメ
# このとき、k はその時点での A の長さ以下であることが保証される。
# kは10^9の桁半分以下、つまり、10^5以下なので、O(10^5)で計算できる。

for _ in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        c = query[1]
        x = query[2]
        C.append(c)
        X.append(x)
    elif query[0] == 2:
        k = query[1]
        sumSlice = 0
        while k > 0:
            if C[0] > k:
                sumSlice += X[0] * k
                C[0] -= k
                break
            else:
                sumSlice += X[0] * k
                k -= C[0]
                C.pop(0)
                X.pop(0)

        print(sumSlice)
