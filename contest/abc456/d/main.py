#import math
#import itertools

# Sから0文字以上取り除いた文字列
# 隣り合っていなくてもいいから、calc(len_S)以上の網羅
# 1文字-1
# 2文字-2+1=3
# 3文字-3+3 +1=7
# 4文字-4+6 +4 +1=15
# 5文字-5+10+10+3+1=29, 31だと嬉しい
# 規則性わからん
# 6+3+1
# そうか、部分列で抽出した後も隣り合っていないことが重要
# abaとかで、bを撮ったらくっつくはだめ
# 2文字を1文字に
S = input()
count = 0
sublists = []
len_S = len(S)

def calc(num):
    data = 0
    for i in range(num):
       data += (i+1)

    return data 

for idx in range(0, len_S-1):
    if S[idx+1] == S[idx]:
        sublists.append(idx)

# idxループ回して、idxスタートから見た時
# sublistsのcalcの数だけ増減した配列が生まれる
# 増減した配列での理論値を常に足していく

for sublist in sublists:
    count += (2**(len_S-sublist) - 1)
    count = count % 998244353

print(count)
