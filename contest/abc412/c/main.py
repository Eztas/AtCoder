import math
T = int(input())

# ドミノ i のすぐ右に置かれているドミノの大きさが 2S_i以下ならばそのドミノも右に向けて倒れます。
# 2倍する->探索->を繰り返す, T*N*N->10^15
# log_2(N)≒16sで済ませる方法があるはず

for t in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    count = math.log2(S[N-1]//S[0])
    domino = S[0]
    for c in range(math.ceil(count)):
        domino_flag = False
        for n in range(N):
            if domino < S[n] and S[n] <= 2 * domino:
                domino = S[n]
                domino_flag = True
                break

        if not domino_flag:
            print(-1)
            break

    if domino_flag:
        print(math.ceil(count) + 1)
    