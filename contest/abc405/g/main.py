N, Q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q):
    L, R, X = map(int,input().split())
    B = A[L-1:R]

    for j in range(len(B)):
        if B[j] >= X:
            B.remove(B[j])
            