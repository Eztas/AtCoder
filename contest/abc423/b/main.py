N = int(input())
L = list(map(int,input().split()))

# N+1個の部屋にN個のドア
# Li=0が開いてて、1なら閉まっている
# 0-> <-N

# 先頭から始めて最初の1と最後からの1で計算

head = 0
tail = 0

for n in range(N):
    if L[n] == 1:
        head = n
        break

for n in range(N):
    if L[N - n - 1] == 1:
        tail = N - n - 1
        break

if tail >= head:
    print(tail - head) # tail > headの時
else:
    print(0) # 全部たどり着けてる時,サンプルにない
    