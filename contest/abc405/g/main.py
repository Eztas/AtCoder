import collections
import math

N, Q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q):
    L, R, X = map(int,input().split())
    B = A[L-1:R]
    
    newB = [b for b in B if b < X]
    newBCounts = collections.Counter(newB).values()
    combination = math.factorial(sum(newBCounts))

    for count in newBCounts:
        combination //= math.factorial(count)

    print(int(combination % 998244353))
    