N, K, X = map(int,input().split())

# N^K = 10^5
# S=10, S*N^K = 10^6
# ソート
# index配列を作る
# 挿入ソートが使えそう
# ソートしていると
# N=3, K=2, X=6なら
# 1,1, 1,2, 1,3, の順で辞書順になるため
# countを増やしてその時の番号をつけて、
# indexの文字を表示させたらいい

S = []
for n in range(N):
    s = input()
    S.append(s)

sorted_S = sorted(S)
# f(0, 0), X=1, f(0, 1), X=2, f(0, 2), X=3
# f(1, 0), X=4, f(1, 1), X=5
# でも、0, 2よりも1, 0, 1,1 が優先されることがある

A = [0] * K

N = N - 1

for k in range(K):
    if X == 0:
        break
    if X <= N:
        A[K-1-k] = X
        X = 0
    else:
        A[K-1-k] = N
        X = X - N

print(sorted_S)
print(A)

for a in A:
    print(sorted_S[a], end='')
print('')
for s1 in sorted_S:
    for s2 in sorted_S:
        print(s1+s2)

print('')
