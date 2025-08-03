N, A, B = map(int,input().split())
S = input()

if B == 0:
    print(S[A:])
else:
    print(S[A:-B])
