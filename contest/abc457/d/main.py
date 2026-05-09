import collections
import heapq
# set(L), L.count(l), heapq.heapify(L)

N, K = map(int,input().split())
A = list(map(int,input().split()))

# 0回以上K回以下
# 最小値の中の最大値, 下界
# 一応理論上、i=1の時にやる方が、A_1+1を繰り返せて、上昇幅が少なめ
# ちょっと違うかも

#4 5
#10 1 10 1
# A_i=10のため、足しても、他より超える
# A_2 = 2を5回, A_2はいいがA_4が1のまま
# A_2を4回, 9と5
# A_2を3回, 7と9
# これ以降は、極端な最小値を生むだけ
# 7が取りうる最小値の中で最大
# dpっぽい
