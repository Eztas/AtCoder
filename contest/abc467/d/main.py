T = int(input())

for t in range(T):
    PX, PY, QX, QY, RX, RY, SX, SY = map(int,input().split()) # それぞれの変数に数値を渡す
    # C1, C2の中心は同じだが、どこでもいい
    # RとSの直交の直線とPとQの直交直線の式では
    # 
    anti_C_1_slope = (QY - PY) / (QX - PX)
    anti_C_2_slope = (SY - RY) / (SX - RX)
    C_1_slope = (-1) / anti_C_1_slope
    C_2_slope = (-1) / anti_C_2_slope

    # y = cs*X + a
    C_1_seppen = (QY - PY) / 2 + (C_1_slope*((QX - PX) / 2))
    C_2_seppen = (SY - RY) / 2 + (C_2_slope*((SX - RX) / 2))

    if C_1_slope == C_2_slope:
        print("No")
    else:
        print("Yes")
