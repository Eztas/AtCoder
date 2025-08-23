N = int(input())
A = list(map(int,input().split()))

# j - i = A_i + A_j

count = 0

for j in range(1, N):
    for i in range(j):
        if j - i == A[i] + A[j]:
            count += 1

print(count)
