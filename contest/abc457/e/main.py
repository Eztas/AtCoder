import collections
import heapq
# set(L), L.count(l), heapq.heapify(L)

N, M = map(int,input().split()) # それぞれの変数に数値を渡す

L = []
R = []
for m in range(M):
    l, r = map(int,input().split())
    L.append(l)
    R.append(r)

# 各2枚の組み合わせが示す布パターンをやるか？
# 

Q = int(input())

for q in range(Q):
    S, T = map(int,input().split())

    # S, Tの範囲だけが覆われる, Mの中の2枚を選ぶことができるか
    # l, rを愚直に追うとN*Q通り
