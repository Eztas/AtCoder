import collections
import math

N, Q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q):
    L, R, X = map(int,input().split())
    B = A[L-1:R]

    for j in range(len(B)):
        if B[j] >= X:
            B[j] = 0
    
    newB = [b for b in B if b != 0]
    newBCounts = collections.Counter(newB).values()
    combination = math.factorial(sum(newBCounts))

    for count in newBCounts:
        combination /= math.factorial(count)

    print(int(combination))
    