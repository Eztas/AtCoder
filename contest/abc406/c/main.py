N = int(input())
P = list(map(int,input().split()))

count = 0

for n in range(4, N):
    for i in range(N-n+1):
        flag = True
        # A_1 < A_2である 
        if P[i] >= P[i+1]:
            flag = False
            break
