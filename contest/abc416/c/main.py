import numpy as np
N, K, X = map(int,input().split())

# 解説曰く、計算量的にはそもそも連結させてからでも
# 計算量は余裕で大丈夫らしい
# もう少しこれで模索してみる
# こういうのは簡単なテストケースを見逃していがち
# Geminiに聞いたところ, N=1だとnp.base_repr(X, N)はエラーになり、REとなる
# 実際に確認

S = []
for n in range(N):
    s = input()
    S.append(s)

sorted_S = sorted(S)
A = [0] * K
X = X - 1

str_X = list(str(np.base_repr(X, N)).zfill(K))
for k in range(K):
    A[k] = int(str_X[k])

for a in A:
    print(sorted_S[a], end='')

print('')
