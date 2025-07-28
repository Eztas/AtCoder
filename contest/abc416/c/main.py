import numpy as np
N, K, X = map(int,input().split())

# 解説曰く、計算量的にはそもそも連結させてからでも
# 計算量は余裕で大丈夫らしい
# 文字列の生成 O(N^K⋅K⋅S)=5*10^6
# 辞書順ソート (N^K⋅log(N^K)⋅(K⋅S))=5*10^6 * 16.6=8*10^7 文字列の長さ分、ソートは比較コストがかかる
# 総合計算量 10^7程度と、10^8を超えないので問題ない

# もう少しこれで模索してみる
# こういうのは簡単なテストケースを見逃していがち
# Geminiに聞いたところ, N=1だとnp.base_repr(X, N)はエラーになり、REとなる
# 実際に確認

# ver1(連結前に辞書順ソートしてから連結させる)の例
# "bab" (S[1] + S[0])
# "baba" (S[1] + S[1])
# "bb" (S[0] + S[0])
# "bba" (S[0] + S[1])
# 私のコードはこうなるが
# 実際は、"bba"よりも"bab"が辞書順で先に来る
# 連結前ソートが連結後に辞書順となるわけではない例が存在する
# 生成aiがcmp_to_keyという特殊なソートを提案したがREだし無駄そう
# やはり連結後にソートするのが無難だし楽

S = []
for n in range(N):
    s = input()
    S.append(s)

sorted_S = sorted(S)
A = [0] * K

str_X = ""
X = X - 1
if N == 1: # N==1なら、どの番目でも同じ文字をKだけ繰り返したものしかない
    for _ in range(K):
        print(sorted_S[0], end='')

else: # N >= 2
    str_X = list(str(np.base_repr(X, N)).zfill(K))
    
    for k in range(K):
        A[k] = int(str_X[k])

    for a in A:
        print(sorted_S[a], end='')

print('')
