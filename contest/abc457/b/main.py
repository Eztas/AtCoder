N = int(input())
A = []
for n in range(N):
    a = list(map(int,input().split()))
    A.append(a[1:])

X, Y = map(int,input().split())

print(A[X-1][Y-1])
