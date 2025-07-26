N = int(input())
A = list(map(int,input().split()))
X = int(input())

flag = False
for a in A:
    if X == a:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
    