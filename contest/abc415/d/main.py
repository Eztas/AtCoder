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

    # N // bottleExchange[2]だと
    # A=4, A-B=2, N=6の時
    # シール増加分は3だが
    # 厳密には(6->2->{4)->0->2}, の2シール
    # A=3, A-B=2, N=10の時
    # 10->7->8->5->6->3->4->2
    # 最後の2でも貰える前提の計算だが、実際はもらえない(Aを下回るため)
    # この対応が必要
    # 方法1: N - Aした上で残りの計算をする
    # (6->2->{4)->0->2}
    # (N - bottleExchange[0]) // bottleExchange[2] + 1
    # -4, +2, -4, +2, がされての-2
    # そのため、最初に、マイナス4をした上で、
    # +2, -4 = -2を繰り返すことができる数を調べる
    # 初手の-4と、最後の+2だけカウントできていないので、+1で帳尻合わせ
    plusSeals = (N - bottleExchange[0]) // bottleExchange[2] + 1 # 最善の行動を繰り返してシールを取る
    N = N - plusSeals * bottleExchange[2] # 実際、シールの枚数*差分だけ、Nは減る
    seals += plusSeals

print(seals)#
