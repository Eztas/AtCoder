import numpy as np
N, K, X = map(int,input().split())

S = []
for n in range(N):
    s = input()
    S.append(s)

sorted_S = sorted(S)
# f(0, 0), X=1, f(0, 1), X=2, f(0, 2), X=3
# f(1, 0), X=4, f(1, 1), X=5
# でも、0, 2よりも1, 0, 1,1 が優先されることがある
# 2進数みたいにすればいける

A = [0] * K
X = X - 1

str_X = list(str(np.base_repr(X, N)).zfill(K))
for k in range(K):
    A[k] = int(str_X[k])

for a in A:
    print(sorted_S[a], end='')

print('')
