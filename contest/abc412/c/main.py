T = int(input())

# ドミノ i のすぐ右に置かれているドミノの大きさが 2S_i以下ならばそのドミノも右に向けて倒れます。
# 2倍する->探索->を繰り返す, T*N*N->10^15

for t in range(T):
    N = int(input())
    S = list(map(int,input().split()))
