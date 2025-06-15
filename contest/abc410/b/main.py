n, Q = map(int,input().split())
X = list(map(int,input().split()))

# N個の箱とQ個のボール
N = [0] * n
B = [0] * Q

def min_box_index():
    min_index = 0
    min_value = N[0]
    for i in range(n):
        if N[i] < min_value:
            min_index = i
            min_value = N[i]

    return min_index  # 全ての箱が埋まっている場合

for q in range(Q):
    if X[q] >= 1:
        N[X[q] - 1] += 1
        B[q] = X[q]
    else: # X[q] == 0
        min_index = min_box_index()
        N[min_index] += 1
        B[q] = min_index + 1

for idx, b in enumerate(B):
    if idx < len(B) - 1:
        print(b,end=' ')
    else:
        print(b)
