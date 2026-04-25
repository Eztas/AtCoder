import collections
import heapq
N, Q = map(int,input().split())

def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(len(data),end=endChar)
        else:
            print(len(data))

C = []
P = []
mountains = [[1]] * N
indexs = [for n in range(N)]
# N枚とN個の山, 山iにはカードiのみ, 最初は1山1枚
# 移動は全部じゃなくて、カードC_iより上、しかもP_iがどの山にいるかの管理も必要
for q in range(Q):
  c, p = map(int,input().split())
  c = c - 1
  p = p - 1
  for mountain in mountains[indexs[c]]:
    
    if mountain = c
      break
  indexs[c] = p
  
# 最後に各山の枚数
print_horizontal_line(mountains, ' ')
