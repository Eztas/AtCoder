N = int(input())
A = list(map(int,input().split()))
A_sorted = sorted(list(set(A)))

for idx, a in enumerate(A_sorted):
    print(a,end='')
    if idx < len(A_sorted) - 1:
        print(' ',end='')
