H, W, N = map(int,input().split())

blocks = [[1 for _ in range(W)] for _ in range(H)]

print(blocks)

for n in range(N):
    x, y = map(int, input().split())
    blocks[x-1][y-1] = 0

Q = int(input())
for _ in range(Q):
    q, xy = map(int, input().split())
    count = 0
    if q == 1:
        for block in blocks[xy-1]:
            if block == 0:
                count += 1
        print(count)
    elif q == 2:
        for h in range(H):
            if blocks[h][xy-1] == 0:
                count += 1
        print(count)
        