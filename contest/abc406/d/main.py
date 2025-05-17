H, W, N = map(int,input().split())

trashs = []
for n in range(N):
    x, y = map(int, input().split())
    trashs.append([x, y])

Q = int(input())
trash_num = N

for _ in range(Q):
    if len(trashs) == 0:
        print(0)
        continue
    
    q, xy = map(int, input().split())
    count = 0
    trashs_copy = trashs.copy()

    if q == 1:
        for trash_copy in trashs_copy:
            if trash_copy[0] == xy:
                count += 1
                trashs.remove(trash_copy)

    elif q == 2:
        for trash_copy in trashs_copy:
            if trash_copy[1] == xy:
                count += 1
                trashs.remove(trash_copy)
    
    print(count)
