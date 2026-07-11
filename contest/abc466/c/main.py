N = int(input())

# print("出力内容", flush=True)
# 点の総当たり, 3なら3, 4なら4*3/2=6
# N*(N-1)/2 < 2N
# N^2-N < 4N, N^2<5N
# 2Nで済ませる方法なくない
# 1, 2, 3は聞けない
# 差分だけ聞いて当てないといけない
# 点1, 2, …, N が この順に 左から右に並んでるらしい
# 点1, 2と点2, 3が共にYesの場合、1と3がYesかは確定しない、少数もあるから
countIJ = 0
for j in range(N):
    print("? "+j+" "+(j+1), flush=True)

    S = input().split()
    if S == "Yes":
        countIJ += 1

print("! "+countIJ)

