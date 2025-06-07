N = int(input())
A = list(map(int,input().split()))
A_sorted = sorted(list(set(A)))

print(len(A_sorted)) 
for idx, a in enumerate(A_sorted):
    if idx < len(A_sorted) - 1:
        print(a,end=' ')
    else:
        print(a)
