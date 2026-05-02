import math
S = input()

# 1文字目から数えて、重複が生まれるまでの個数
# 3×10^5×3×10^5の計算
# 重複インデックスの計算か？
# 隣り合う文字が重複している時のインデックス(1,2 で隣り合う時の1)
count = 0
neighbor_index = [0]
len_S = len(S)
prevS = S[0]
# そのインデックス,abcc
# a, b, c, ab, bc, abc
# abccbaa
# 0, 2, 5
for idx, s in enumerate(S):
    neighbor_index.append(idx)

for idx in range(1, len(neighbor_index)):
    count += math.factorial(neighbor_index[idx]-neighbor_index[idx-1])

print(count%998244353)
