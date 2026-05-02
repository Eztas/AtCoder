#import math
#import itertools
S = input()

def calc(num):
    data = 0
    for i in range(num):
       data += (i+1)

    return data 
        
# 1文字目から数えて、重複が生まれるまでの個数
# 3×10^5×3×10^5の計算
# 重複インデックスの計算か？
# 隣り合う文字が重複している時のインデックス(1,2 で隣り合う時の1)
# イメージとしては重複があると
# abbcを ab, bcで区切って、それぞれを階乗させるイメージ
# 長さ配列を作ればいいのか
count = 0
sublists = []
len_S = len(S)
# そのインデックス,abcc
# a, b, c, ab, bc, abc
# abca
# a, b, c, a
# abccbaa
# 0, 2, 5
head = 0
for idx in range(0, len_S-1):
    if S[idx+1] == S[idx]:
        sublists.append(idx-head+1)
        head = idx+1

if head != len_S-1:
    sublists.append(len_S-1-head+1)
else:
    sublists.append(1) ## 同じということは、bbのbまでみたが、末尾のbの対応だけない

for sublist in sublists:
    count += calc(sublist)

print(count%998244353)
