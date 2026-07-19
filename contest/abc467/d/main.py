T = int(input())

# 方程式を使うと遅いかつ外部ライブラリが必須だから、ベクトルがいいらしい
# 空間ベクトル a, b の外積（Cross Product）に関する仕様
# - 大きさ: |a||b|sinθ （a と b が成す平行四辺形の面積に等しい）
# - 向き: ベクトル a, b の両方に垂直な方向
# これさえ求めれば。PQとRSに直交する箇所の交点がわかる
for t in range(T):
    PX, PY, QX, QY, RX, RY, SX, SY = map(int,input().split()) # それぞれの変数に数値を渡す
    # C1, C2の中心は同じだが、どこでもいい
    # RとSの直交の直線とPとQの直交直線の式では

    vecPQ = [QX - PX, QY - PY]
    vecRS = [SX - RX, SY - RY]
    # Y1/X1 = Y2/X2の考えを応用

    # 並行
    if vecPQ[1] * vecRS[0] - vecPQ[0] * vecRS[1] == 0:
        print("No")
    else: # 並行でない = 交わる = 中心は存在
        print("Yes")
    