N, Q = map(int,input().split())

# 移動しかしないから
# 足し算のパターンは限られている

# 実際に移動させる必要はない
A = list(map(int,input().split()))
head = 0
for q in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        c = query[1]
        head = (head - c) % N

    else: # 2の時
        l = query[1] - 1
        r = query[2] - 1

        if head <= l:
            print(sum(A[l-head:r-head+1]))
        else:
            if head <= r:
                print(sum(A[head+l:r-head+1]))
            else:
                print(sum(A[head+l:head+r+1]))
