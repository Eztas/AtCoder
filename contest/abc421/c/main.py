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

print(S)

while True:
    if pos == 2*N - 1:
        break
    if S[pos] == top_s:
        pos += 1
        continue
    else: # S[i] != S[0]
        if pos == another_letter_index: # ABABAB…がつづき時の対応
            top_s = S[another_letter_index]
            another_letter_index += 1
            pos += 1
        else:
            count += pos - another_letter_index # 交換回数(移動回数)
            S = S[0:another_letter_index] + S[pos] + S[another_letter_index:pos] + S[pos+1:]
            print(S)
            top_s = S[another_letter_index]
            another_letter_index += 1
            pos = another_letter_index

print(count)
