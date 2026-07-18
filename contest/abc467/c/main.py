import collections
import heapq
from bisect import bisect_right, bisect_left # x以下の最小値のidx, x以上の最大値のidxを返す
from collections import defaultdict # setっぽく使える
# set(L), L.count(l), heapq.heapify(L)

N, M = map(int,input().split()) # Mは2固定
A = list(map(int,input().split())) # 配列で返す
B = list(map(int,input().split())) # 配列で返す

AA = []

for i in range(N-1):
    AA.append((A[i]+A[i+1]))

count = 0
for i in range(N-1):
    if AA[i] % 2 == B[i]:
        continue
    if i == N-2:
        if AA[i] % 2 != B[i]:
            count += 1
    else:
        AA[i] += 1
        AA[i+1] += 1
        count += 1

print(count)
        
# i番目のA[i]に1を加える、を好きな回数
# 実質AA[i-1]とAA[i]を1増加
# A[i]+A[i+1]を2で割った余が、B[i]に等しい
# 基本0か1
# 必要な操作回数の最小値
# 全部でこれを満たすことが重要

# 別に足していい

# 0 0 1 2 1 1 1 1 1 AA
# 0 0 0 1 0 1 0 1 0 B

# 1 0 1 2 1 1 1 1 1 AA
# 0 0 0 1 0 1 0 1 0 B

# 0 0 1 2 1 1 1 1 1 AA
# 0 1 0 1 0 1 0 1 0 B

# 1 0 1 2 1 1 1 1 1 AA
# 0 1 0 1 0 1 0 1 0 B

# 0 0 0 1 1 0 1 0 1 0 A
# 0 0 1 2 1 1 1 1 1 AA
# 0 1 0 1 0 1 0 1 0 B
# 2つ同士のペアで揃っていないものを消せばいい
# 偶数ペア数 = /2すればいい？

# 0 0 0 1 1 0 1 0 1 0 A
# 0 0 1 2 1 1 1 1 1 AA
# 0 1 1 1 0 1 0 1 0 B
# 7つのペア

# 0 0 1 1 1 0 1 0 1 0 A
# 0 1 2 2 1 1 1 1 1 AA
# 0 1 1 1 0 1 0 1 0 B

# 0 1 3 3 1 1 1 1 1 AA
# 0 1 1 1 0 1 0 1 0 B

# 0 1 3 3 2 2 1 1 1 AA
# 0 1 1 1 0 1 0 1 0 B

# 0 1 3 3 2 2 1 1 1 AA
# 0 1 1 1 0 1 0 1 0 B