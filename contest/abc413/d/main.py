T = int(input())

# 1≤T≤10^5, もう10^3くらいの余裕しかない
# 1 つの入力ファイルにおけるN の総和は 2×10^5以下
# ->つまりrange(N)のforループ一回だけならTの計算量は無視できるのオーダーは10^5以下
# sortして、全て正の数倍なら行けるが、負の数倍だとソートしても無理
# 絶対値にすれば問題ない

# 90000 8100 -27000 729 -300000 -2430 1000000
# (-10/3の等比数列) = 1000000, -300000, 90000

# -16 24 54 81 -36
# -16, 24, -36, 54, 81, 絶対値的には3/2倍で成立するが、実際はマイナスであり、-81にならないからダメ

for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))

    for n in range(N):
        A[n] = abs(A[n])

    A.sort()

    isGeometric = True
    for n in range(1, N-1):
        if A[n] * A[n] != A[n-1] * A[n+1]:
            isGeometric = False
            break

    if isGeometric:
        print("Yes")
    else: 
        print("No")
