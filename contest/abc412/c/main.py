import math
T = int(input())

# ドミノ i のすぐ右に置かれているドミノの大きさが 2S_i以下ならばそのドミノも右に向けて倒れます。
# 2倍する->探索->を繰り返す, T*N*N->10^15
# log_2(N)≒16sで済ませる方法があるはず

for t in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    count = math.log2(S[N-1]//S[0])
    print(math.ceil(count) + 1)  # 0-indexedなので+1
