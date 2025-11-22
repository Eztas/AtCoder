N = int(input())
A = list(map(int,input().split()))

for n in range(N):
    if n == 0:
        print(-1)
    elif n == 1:
        if A[0] > A[1]:
            print(1)
        else:
            print(-1)
    else:
        maxheightidx = n
        for i in range(n):
            if A[i] > A[n]:
                maxheightidx = i
        if maxheightidx == n:
            print(-1)
        else:
            print(maxheightidx+1)
