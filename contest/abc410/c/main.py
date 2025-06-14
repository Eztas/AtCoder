N, Q = map(int,input().split())

A = [n+1 for n in range(N)]

type_2_exist = False  # type 2 queryが存在するかどうか

for q in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        p = query[1] - 1
        x = query[2]
        A[p] = x

    elif query[0] == 2:
        type_2_exist = True
        p = query[1] - 1
        print(A[p])
    
    else:  # query[0] == 3
        k = query[1] % N # kがN以上の場合はNで割った余りを使う, 実質余りの数しか入れ替えが起きない(k=Nなら元に戻るから)
        if k == 0: # k=0なら移動はないのでスルー
            continue
        A = A[k:] + A[0:k] # 先頭を末尾に移動をk回繰り返す = ０からk-1番目の要素群を末尾に移動

if not type_2_exist:
    print()
