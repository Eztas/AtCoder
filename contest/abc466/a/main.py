N = int(input())
X = list(map(int,input().split())) # 配列で返す

isMinus = True
for x in X:
    if x >= 0:
        isMinus = False
        break

if isMinus:
    print("Yes")
else:
    print("No")
