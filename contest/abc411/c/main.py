N, Q = map(int,input().split())
A = list(map(int,input().split()))

# 白を0, 黒を1とする, 左右1列
line = [0] * N

for q in range(Q):
    count = 0
    line[A[q] - 1] = 1 - line[A[q] - 1]  # A[q]の色を反転
    print(count)
    