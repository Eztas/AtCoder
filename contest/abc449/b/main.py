H, W, Q = map(int,input().split())

# H行、W列
# 行丸ごと消える感じ

for q in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        R = query[1]
        H = H - R
        print(R * W)
    if query[0] == 2:
        C = query[1]
        W = W - C
        print(H * C)