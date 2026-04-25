import collections
import heapq
N, K = map(int,input().split())
A = list(map(int,input().split()))

# 最大値を上から消して行くだけ
# あるいは最小値を足すだけ
# 違うか、同じ整数でまとめて、その和が小さい順に引く感じ
# set
# print(c.keys())
# dict_keys(['a', 'b', 'c'])
# print(c.values())
# dict_values([4, 1, 2])
# print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])

set_a = set(A)
total_A = sum(A)
min_count = len(set_a) - K
max_data = 0
k_list = [0]*K
heapq.heapify(k_list) # 返り値を返す関数ではない

if min_count <= 0:
  print(0)

else:
  for solo_a in set_a:
    pop_k = heapq.heappop(k_list)
    if pop_k < solo_a * A.count(solo_a):
      heapq.heappush(k_list, solo_a * A.count(solo_a))
    else:
      heapq.heappush(k_list, pop_k)
      
  print(total_A - sum(k_list))
