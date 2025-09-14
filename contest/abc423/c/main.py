# B問題に開閉捜査がついて, 計算量も増加
# 全てに鍵をかける, Rからスタートなどの違い

N, R = map(int,input().split())
L = list(map(int,input().split()))

#部屋 i−1 または部屋iにいるときに限り、ドアiの鍵に対して開閉操作を行うことができます。
# ドア iの鍵に対して開閉操作を行ったとき、その鍵が開いているときは閉まり、閉まっているときは開きます
# 開閉は必ずではない

# 右からやろうが左からやろうが変わらないとまず仮定
# この前の左からのパターンと右からのパターンの最小値を計算する余裕はあるかも
# 1 0 0 1 0 0
# 1 1 0 1 0 0

# まず一番左の0に移動する
# その0を1にする必要があるが, そこに辿り着くまでに1があれば全部まず0

# Lの操作は全く不要
# ドア i は部屋 i−1 と部屋 i を
# ドア i は部屋 i と部屋 i+1として解釈 
# 計算はできるが分岐が多すぎる

# 0  1  2. 3.   … N - 1.     N
#.  0  1. 2. 3. ….     N - 1

# head, R, tailはこれでOK
# R, head, tailなら

count = 0

head = 0
tail = 0
for n in range(N):
    if L[n] == 0:
        head = n
        break

for n in range(N):
    if L[N - n - 1] == 0:
        tail = N - n - 1
        break

if head > R:
    for j in range(R, tail+1):
        if L[j] == 0:
            count += 1
        else: # 1ならまず開けてから閉めないといけない
            count += 2

    print(count)

elif tail < R:
    for j in range(head, R):
        if L[j] == 0:
            count += 1
        else: # 1ならまず開けてから閉めないといけない
            count += 2

    print(count)

else:
    for j in range(head, tail+1):
        if L[j] == 0:
            count += 1
        else: # 1ならまず開けてから閉めないといけない
            count += 2

    print(count)
