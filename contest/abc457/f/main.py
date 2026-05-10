import collections
import heapq
# set(L), L.count(l), heapq.heapify(L)

s = input()
s_list = list(input()) # 入力例: "abcde" -> ['a', 'b', 'c', 'd', 'e']
S = input().split() # 入力例: ". # ." -> ['.', '#', '.']
T = [list(input()) for _ in range(H)]

M = int(input())
A = list(map(int,input().split())) # 配列で返す
N, Q = map(int,input().split()) # それぞれの変数に数値を渡す
