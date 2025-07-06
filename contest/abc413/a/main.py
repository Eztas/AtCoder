N, M = map(int,input().split())
A = list(map(int,input().split()))

if M >= sum(A):
    print('Yes')
else:
    print('No')
    