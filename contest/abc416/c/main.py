N, K, X = map(int,input().split())

# N^K = 10^5
# S=10, S*N^K = 10^6
# ソート
# index配列を作る
# 挿入ソートが使えそう
# ソートしていると
# N=3, K=2, X=6なら
# 1,1, 1,2, 1,3, の順で辞書順になるため
# countを増やしてその時の番号をつけて、
# indexの文字を表示させたらいい

index_S = [0] * N
S = []
for n in range(N):
    s = input()
    S.append(s)

print(index_S)
