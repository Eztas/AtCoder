N = int(input())
S = input()

# 実際に移動させる必要はない

# 方法1
# A始動ならBの移動回数を記せば良い
# S="AAABABBB", ならS[3] = Bの時、S[1]まで移動させる回数だけ書く
# 結局2N回検索が必要, 別にN^2じゃないから大丈夫だ
# 方法2, リスト半分(奇数番目, 偶数番目)
# 奇数番目は全部同じにしたい, 偶数ばんめも同じ

another_letter_index = 1
count = 0
top_s = S[0]
odd_S = S[0::2]
even_S = S[1::2]

for i in range(1, 2*N):
    if S[i] == S[0]:
        continue
    else: # S[i] != S[0]
