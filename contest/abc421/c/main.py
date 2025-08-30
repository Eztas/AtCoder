N = int(input())
S = input()

# 実際に移動させる必要はない

# 方法1
# A始動ならBの移動回数を記せば良い
# S="AAABABBB", ならS[3] = Bの時、S[1]まで移動させる回数だけ書く
# 結局2N回検索が必要, 別にN^2じゃないから大丈夫だ
# 方法2, リスト半分(奇数番目, 偶数番目)
# 奇数番目は全部同じにしたい, 偶数ばんめも同じ

# AAABABABBBABABBABABABABBAAABABABBA
# ABAAABABBBABABBABABABABBAAABABABBA

another_letter_index = 1
count = 0
pos = 0
top_s = S[0]
odd_S = S[0::2]
even_S = S[1::2]

index1_list = []
# 今のBの位置のリスト
# これらを全部1, 3, 5の変化できればいい
for n in range(2*N):
    if top_s == S[n]:
        index1_list.append(n)

idx = 0
for n in range(1, 2*N, 2):
    count += abs(index1_list[idx] - n)
    idx += 1

print(count)
