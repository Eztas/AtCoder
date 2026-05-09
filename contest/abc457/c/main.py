import collections
import heapq
# set(L), L.count(l), heapq.heapify(L)

N, K = map(int,input().split())
A = []
for n in range(N):
    a = list(map(int,input().split()))
    A.append(a[1:]) # 初項のLを除く

C = list(map(int,input().split()))

B = 0

# A[n]をC[n]回列に加える
# KがC[n]のうちどれなのかを知る必要がある

# idxとoffsetさえ求めたらOK
# ちょい複雑
# c * len(A[i]) >= k
# 2 * 3, 4
k = K
idx = 0
offset = 0
for i, c in enumerate(C):
    if k > c * len(A[i]):
        k = k - c
    else:
        idx = i
        offset = k % len(A[i])
        if k == 0:
            print(A[i][len(A[i])-1])
        else:
            print(A[i][k-1])
        break
