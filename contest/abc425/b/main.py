N = int(input())
A = list(map(int,input().split())) # -1 or 1<=a<=N

# P 1~N

# A_i ≠ -1なら, まず P_i = A_iにする
# その後、A_i = -1なら,余ってる数字を埋める
# 基本-1以外の数字で重複があればNo

def has_duplicates(seq):
    for s in seq:
        if s == -1:
            seq.remove(s)
    return len(seq) != len(set(seq))

def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)

if has_duplicates(A[:]):
    print("No")

else:
    P = [-1] * N
    M = []
    for n in range(N):
        M.append(n+1)


    for n in range(N):
        if A[n] != -1:
            P[n] = A[n]
            M.remove(A[n])

    for n in range(N):
        if P[n] == -1:
            P[n] = M[0]
            M.remove(M[0])

    print("Yes")

    print_horizontal_line(P, ' ')
    