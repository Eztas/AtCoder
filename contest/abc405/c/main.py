N = int(input())
A = list(map(int,input().split()))

sumA = 0

copyA = A.copy()

for i in range(N):
    copyA.pop(0)
    sumA += A[i] * sum(copyA)

print(sumA)
