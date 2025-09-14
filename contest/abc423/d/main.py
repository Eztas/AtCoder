S = input()
N = int(input())
K = int(input())

k = 0
# 最大0~Aまでの長さのリストがそれぞれ人数を格納していれば良い
# 格納する時にN*latestTimeの時間量になる
A = []
B = []
C = []
latestTime = 0
for n in range(N):
    a, b, c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

    if a+b > latestTime:
        latestTime = a+b

L = [0] * (latestTime) # 最悪 A+max(B)

for n in range(N):

