N = int(input())
D = list(map(int,input().split()))

for i in range(N-1):
    count = 0
    for j in range(i, N-1):
        count += D[j]
        if j == N-2:
            print(count)
        else:
            print(count,end=' ')
