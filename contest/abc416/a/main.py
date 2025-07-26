N, L, R = map(int,input().split())
S = input()

flag = True
for n in range(L-1, R):
    if S[n] == 'x':
        flag = False

if flag:
    print("Yes")
else:
    print("No")
    