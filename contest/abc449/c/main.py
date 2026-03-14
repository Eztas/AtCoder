N, L, R = map(int,input().split())
S = input()

# 1 <= i <= j <= N
# S_i = S_j
# L <= j - i <= R
# 別にabcの文字限定ではなく、26文字の小文字アルファベットが対象
# Lの差、L+1の差、、、Rの差の分で同じものがあるかを確認

# a, b, cに対応した配列
alphas = [chr(i+97) for i in range(26)]
alphas_idx = [[] for _ in range(26)]
# 0なら更新
# 1以上なら、差分行列のみを保存

for idx, s in enumerate(S):
    alphas_idx[ord(s) - 97].append(idx)

for id in alphas_idx:
    print(id)