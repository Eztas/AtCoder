N = int(input())
A = list(map(int,input().split()))

sumA = sum(A)

sumAA = 0

for i in range(N):
    sumA -= A[i]  
    sumAA += sumA * A[i]

print(sumAA)
