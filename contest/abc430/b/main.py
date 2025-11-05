N, M = map(int,input().split())
S = []
for n in range(N):
    s = input()
    S.append(s)

# 解説を見たらsetを使うらしい(重複の処理に困ったらsetを使う認識でいこう)

G = set()
for i in range(N-M+1):
    for j in range(N-M+1):
        G.add(tuple(S[ii][j:j+M] for ii in range(i, i+M)))

print(len(G))
