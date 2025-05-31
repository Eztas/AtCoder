N = int(input())
A = list(map(int,input().split()))
A_sorted = sorted(list(set(A)))

for a in A_sorted:
    print(a,end='')
