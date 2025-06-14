N, Q = map(int,input().split())

A = [n+1 for n in range(N)]

for q in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        p = query[1] - 1
        x  = query[2]
        A[p] = x

    elif query[0] == 2:
        p = query[1] - 1
        print(A[p])
    
    else:  # query[0] == 3
        k = query[1]
        A = A[k:] + A[0:k] # 先頭を末尾に移動をk回繰り返す = ０からk-1番目の要素群を末尾に移動
