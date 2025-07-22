N, M = map(int,input().split())

# 最前の行動ばかり取るようにすることを意識してまず力技

notEmpty = N
empty = 0

bottleExchanges = [] # 渡す瓶, 貰う瓶、実質減る瓶
seals = 0

for _ in range(M):
    a, b = map(int,input().split())
    diff = a - b
    bottleExchanges.append([a, b, diff])

# diffの小さいものから
sortedBottleExchanges = sorted(bottleExchanges, key=lambda x: x[2])

while True:
    if notEmpty <= 0:
        break
    empty += notEmpty # 飲む
    notEmpty = 0

    for bottleExchange in sortedBottleExchanges:
        if empty >= bottleExchange[0]:
            plusSeals = empty // bottleExchange[0] # 最善の行動を繰り返してシールを取る
            empty = empty % bottleExchange[0]
            notEmpty += plusSeals * bottleExchange[1]
            seals += plusSeals
            break

print(seals)
