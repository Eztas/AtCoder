import heapq
from collections import deque
N, K = map(int,input().split())

# 最大0~Aまでの長さのリストがそれぞれ人数を格納していれば良い
# 格納する時にN*latestTimeの時間量になる

# 解説曰く, heapqという優先付きキューが利用できる
# https://qiita.com/uniTM/items/9630ed9d51f62b3e35ab

# gemini曰く イベント駆動シミュレーション (Event-Driven Simulation) 
# ↑ 状態が変化するイベントの総数が、時間の最大値に比べて十分に小さいため
# 時間が連続的に流れると考えるのではなく、
# 「何かが起こる瞬間」（イベント）にだけ注目して、
# -> 俺の最初の考えとは大違い

# 流れ
# 入店でt, cを変更 -> AとCを用いる
# 割り込み的にBが来たら減らす作業が必要
# ただBのリストを参照して毎回計算みたいなことをすると、計算量がオーバー
# -> 優先度付きキューを用いる, 順序関係なく最小値をpopできる
# 最小値だから退店時間が早いものを取り出せる

# 入店時間さえ取得できればいい
# n番目に擬似的にデータの挿入とかしてしまって検証するものあり(?)
# こういうややこしいやつはまずイベントとデータ構造で考える
# イベントは2種類
# 到着(到着時に、入店タイムの計算を行うからイベント自体は到着のみ) 
# 退店(客数が減る)
# 扱いたいデータ構造1 種類
# 店内の客(店内)
# forループでは各客の入店時間を格納することを軸に行う
# forループ一回ごとに入店が済んでいるわけではないので注意

canEnterTime = 0
currentCustomers = 0
goOutCustomers = []

for n in range(N):
    a, b, c = map(int,input().split())
    # まだ暫定
    # 前の客の入店時刻(last_enter_time)と自分の到着時刻(a)のうち、遅い方からスタート
    # 待ち行列というルールをこれで守らせる
    canEnterTime = max(canEnterTime, a) 

    # 今の人数とこれから入る人数がK以上の時だけpopする作業をする
    # 普通に入れるなら何もせずに入る
    # 同じ時間に重複してても、1回だしてKに収まるなら次に外せばいい
    # 同じ退店時間の人が複数いるときは一度に取り出して、なんてことはいらない
    while (currentCustomers + c > K):
        goOutCustomer = heapq.heappop(goOutCustomers)
        # 待ち行列に着く時間の方が遅いなら、そっちになるようにしないと
        # 待ち時間よりも早く入店することになる
        canEnterTime = max(canEnterTime, goOutCustomer[0]) 
        currentCustomers -= goOutCustomer[1]
    
    print(canEnterTime)
    heapq.heappush(goOutCustomers, (canEnterTime+b, c)) # B時間後に出るからcanEnterTimeと足す
    currentCustomers += c # 今店にいる人数
