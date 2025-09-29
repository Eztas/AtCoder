import heapq
from collections import deque
N = int(input())
K = int(input())

k = 0
# 最大0~Aまでの長さのリストがそれぞれ人数を格納していれば良い
# 格納する時にN*latestTimeの時間量になる

# 解説曰く, heapqという優先付きキューが利用できる
# https://qiita.com/uniTM/items/9630ed9d51f62b3e35ab

# gemini曰く イベント駆動シミュレーション (Event-Driven Simulation) 
# ↑ 状態が変化するイベントの総数が、時間の最大値に比べて十分に小さいため
# 時間が連続的に流れると考えるのではなく、
# 「何かが起こる瞬間」（イベント）にだけ注目して、
# -> 俺の最初の考えとは大違い

# 流れ
# 入店でt, cを変更 -> AとCを用いる
# 割り込み的にBが来たら減らす作業が必要
# ただBのリストを参照して毎回計算みたいなことをすると、計算量がオーバー
# -> 優先度付きキューを用いる, 順序関係なく最小値をpopできる
# 最小値だから退店時間が早いものを取り出せる

A = []
B = []
C = []
currentTime = 0
currentCustomers = 0
for n in range(N):
    a, b, c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for n in range(N):

