N, M = map(int,input().split())

# 最前の行動ばかり取るようにすることを意識してまず力技
# A/Bじゃなくても、A-Bの少ないものをやるので良さそう
# この考え方なだけで貪欲法に該当するらしい

# 計算量は初手のソートが一番時間かかる(O(MlogM))
# だけどTLE, 瓶の受け渡しの計算時間を減らせるか？
# -> そもそも飲み瓶、空き瓶で分けず
# Aではなく差分のみで空き瓶を減らす方向性で続けて、無理なら次へにする

bottleExchanges = [] # 渡す瓶, 貰う瓶、実質減る瓶
seals = 0

for _ in range(M):
    a, b = map(int,input().split())
    diff = a - b
    bottleExchanges.append([a, b, diff])

# diffの小さいものから
sortedBottleExchanges = sorted(bottleExchanges, key=lambda x: x[2])

for bottleExchange in sortedBottleExchanges:
    if N <= 0: # N=空き瓶がないなら別にいい
        break
    if N < bottleExchange[0]: # そもそも交換できない
        continue

    plusSeals = N // bottleExchange[2] # 最善の行動を繰り返してシールを取る
    N = N % bottleExchange[2]
    seals += plusSeals

print(seals)
