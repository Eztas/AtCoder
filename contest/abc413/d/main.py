T = int(input())

# 1≤T≤10^5, もう10^3くらいの余裕しかない
# 1 つの入力ファイルにおけるN の総和は 2×10^5以下
# ->つまりrange(N)のforループ一回だけならTの計算量は無視できるのオーダーは10^5以下
# sortして、全て正の数倍なら行けるが、負の数倍だとソートしても無理
# 絶対値にすれば問題ない
# 等比数列は絶対値的に見れば、増え続けるか減り続けるかだけ
# 1, -1, 1, -1, 1, -1, ... のような等比数列は絶対値的には成立する
# 同じ数の-倍の時に、このsortだとNoになる時はある
# 90000 8100 -27000 729 -300000 -2430 1000000
# (-3/10の等比数列) = 1000000, -300000, 90000

# -16 24 54 81 -36
# -16, 24, -36, 54, 81, 絶対値的には3/2倍で成立するが、実際はマイナスであり、-81にならないからダメ

for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))

    all_same = False
    if A[0] > 0:
        plus_count = 1
        minus_count = 0
    elif A[0] < 0:
        plus_count = 0
        minus_count = 1

    for n in range(1, N):
        if abs(A[n]) != abs(A[0]):
            all_same = False
            break
        else:
            if A[n] > 0:
                plus_count += 1
            elif A[n] < 0:
                minus_count += 1
            all_same = True

    # 1, 1, 1, 1, 1 ok
    # 1, -1, 1, -1, 1 ok
    # -1, -1, -1, -1, -1 ok
    # 1, -1, 1, -1, -1 no
    # 1, -1, 1, -1, 1, -1 ok
    if all_same:
        if plus_count == N or minus_count == N:
            print("Yes")
            continue
        else:
            if plus_count == minus_count: # plus_count=minus_count=N/2
                print("Yes")
                continue
            elif (plus_count == minus_count + 1) or (minus_count == plus_count + 1):
                print("Yes")
                continue
            else:
                print("No")
                continue
    A.sort(key=abs)

    isGeometric = True
    for n in range(1, N-1):
        if A[n] * A[n] != A[n-1] * A[n+1]:
            isGeometric = False
            break

    if isGeometric:
        print("Yes")
    else: 
        print("No")
