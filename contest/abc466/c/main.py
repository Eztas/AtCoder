N = int(input())
# https://qiita.com/y-tsutsu/items/aa7e8e809d6ac167d6a1
# print("出力内容", flush=True)
# 点の総当たり, 3なら3, 4なら4*3/2=6
# N*(N-1)/2 < 2N
# N^2-N < 4N, N^2<5N
# 2Nで済ませる方法なくない
# 1, 2, 3は聞けない
# 差分だけ聞いて当てないといけない
# 点1, 2, …, N が この順に 左から右に並んでるらしい
# 点1, 2と点2, 3が共にYesの場合、1と3がYesかは確定しない、少数もあるから
# 1, 2 , 3, 4OK, 1-5でダメになる
# 1から4まで全てOKするのが確定, 次の2とかは2, 5のパターンを調べればいい
countIJ = 0
ikeru_kazu = 1
hasNo = False
for i in range(1, N):
    for j in range(ikeru_kazu+1, N+1):
        print("? "+str(i)+" "+str(j), flush=True) # キャストしてもRE

        S = input()
        if S == "Yes":
            ikeru_kazu += 1
        else:
            break # これ以上はNo, continueやと結局計算してるわ、2N超過でREかな？
    countIJ += ikeru_kazu - i

print("! "+str(countIJ), flush=True)
