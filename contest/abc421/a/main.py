N = int(input())

S = []

for n in range(N):
    s = input()
    S.append(s)

XY = list(input().split())

X = int(XY[0]) - 1
Y = XY[1]

if S[X] == Y:
    print("Yes")
else:
    print("No")
