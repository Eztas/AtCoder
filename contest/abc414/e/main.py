N = int(input())
#整数の組 (a,b,c) であって以下の条件を満たすものの個数を 998244353 で割ったあまりを求めてください。

#1≤a,b,c≤N
#a,b,c は相異なる。
#a を b で割ったあまりは c に等しい。
# a=bはない
# a<bの時、あまりはa, つまりa=cになり、条件を満たさない
# 必ず、a>bの時のみを求めれば良い
# N=10^12
# a=10^12, b=10^12, c=10^12
# a>bなので、1/2*10^24*10^12?

count = 0
for c in range(1, N + 1):
    for b in range(1, N + 1):
        for a in range(b + 1, N + 1):
            if c == a % b:
                count += 1

print(count)