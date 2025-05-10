N = int(input())
A = list(map(int,input().split()))

sumA = 0

for i in range(N):
    for j in range(i+1, N):
        sumA += A[i] * A[j]

print(sumA)
