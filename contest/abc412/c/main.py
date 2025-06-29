import math
T = int(input())

# ドミノ i のすぐ右に置かれているドミノの大きさが 2S_i以下ならばそのドミノも右に向けて倒れます。
# T*Nではなく、Tの全てをすると最大で2*10^5と示されている
# N^2にさえならなければ良い
# log_2(N)≒16sで済ませる方法があるはず
# 最初に見つかったものを選ぶ貪欲法でなく、最大のものを選ぶ貪欲法にする工夫がいる

for t in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    count = 1
    right = 0 # 現時点での一番右
    effected = [False] * N  # 倒れたドミノを管理するためのリスト, 貪欲法では一度通ったものは使わない　

    while True:
        if S[right] * 2 >= S[N-1]:
            count += 1
            break

        nxt = -1 # 次に倒すドミノ、なければ-1, またN-1を示す
        for n in range(1, N):
            if effected[n]:
                continue
            if S[right] * 2 >= S[n]: # 右に倒せる場合
                if nxt == -1 or S[n] > S[nxt]: # まだ倒していない or 今保持している次のドミノより大きいかつ範囲内なら
                    nxt = n # 今のドミノを次倒すドミノにする

        if nxt == -1:  # 次に倒すドミノがない場合
            count = -1
            break
        else:          # 次に倒すドミノがある場合
            effected[nxt] = True  # 倒れたドミノを管理する
            right = nxt  # 右に倒したドミノを更新
            count += 1  # 倒したドミノの数を更新

    print(count)
    