N = int(input())
A = list(map(int,input().split()))

x = 0

while True:
    flag = True
    count = 0
    for n in range(N):
        if A[n] >= x:
            count += 1
    if count < x:
        flag = False
    
    if not flag:
        if x != 0:
          x -= 1
        break
    x += 1

print(x)
