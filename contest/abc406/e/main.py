import sys
T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    total = 0

    for x in range(1, N+1):
        bin_x = bin(x)[2:]
        count = 0
        for bin_x_bit in bin_x:
            if bin_x_bit == 1:
                count += 1
        if count == K:
            total += x

    print(total % 998244353)
