H, W, N = map(int,input().split())

blocks = [[1 for _ in range(W)] for _ in range(H)]

print(blocks)

for n in range(N):
    x, y = map(int, input().split())
    blocks[x-1][y-1] = 0
