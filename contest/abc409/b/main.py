N = int(input())
A = map(int,input().split())

x = 0

while True:
    flag = True
    count = 0
    for a in A:
        print('a-', a, 'x=',x)
        if a >= x:
            count += 1
    print(count, x)
    if count < x:
        flag = False
    
    if not flag:
        if x != 0:
          x -= 1
        break
    x += 1

print(x)
