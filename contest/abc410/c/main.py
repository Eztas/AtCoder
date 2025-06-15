# 実際に配列を変えるのではなく、offsetを用意し、それで先頭を指示することで
# 配列の操作に関する計算をしなくてもよい
N, Q = map(int,input().split())

A = [n+1 for n in range(N)]

type_2_exist = False  # type 2 queryが存在するかどうか
offset = 0
for q in range(Q):
    query = list(map(int,input().split()))

    if query[0] == 1:
        A[(query[1] - 1 + offset) % N] = query[2]

    elif query[0] == 2:
        type_2_exist = True
        print(A[(query[1] - 1 + offset) % N])
    
    else:  # query[0] == 3
        offset += query[1] # kがN以上の場合はNで割った余りを使う, 実質余りの数しか入れ替えが起きない(k=Nなら元に戻るから)

if not type_2_exist:
    print()
