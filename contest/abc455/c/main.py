import collections
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

C_A = collections.Counter(A)
total = sum(A)
k_list = [0] * K
for c_a in C_A.keys():
  for k in K:
    if c_a * C_A[c_a] >= k_list[k]:
      k_list[k] = c_a * C_A[c_a]
      break

for k in k_list:
  total -= k
  
print(total)
