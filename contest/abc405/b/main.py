N, M = map(int,input().split())
A = list(map(int,input().split()))

for n in range(N):
    flags = [False] * M
    for a in A:
        if a >= 1 and a <= M:
            flags[a-1] = True
        else:
            print(n)
            exit()
    
    for flag in flags:
        if not flag:
            print(n)
            exit()
    A.pop(len(A)-1)

print(N)
