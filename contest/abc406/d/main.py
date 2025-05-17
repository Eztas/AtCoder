H, W, N = map(int,input().split())

blocks = [[1 for _ in range(W)] for _ in range(H)]

for n in range(N):
    x, y = map(int, input().split())
    blocks[x-1][y-1] = 0

Q = int(input())
trash_num = N
for _ in range(Q):
    q, xy = map(int, input().split())
    count = 0

    if trash_num == 0:
        print(0)
        continue

    if q == 1:
        for w in range(W):
            if blocks[xy-1][w] == 0:
                count += 1
                blocks[xy-1][w] = 1

    elif q == 2:
        for h in range(H):
            if blocks[h][xy-1] == 0:
                count += 1
                blocks[h][xy-1] = 1
    
    trash_num -= count
    print(count)
