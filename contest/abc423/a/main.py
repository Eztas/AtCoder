import math
X, C = map(int,input().split())

# X = Y + Y * C/1000
# 1000X = 1000Y + CY
# Y = 1000X / (1000 + C)
# Yは1000円単位

real_money = math.floor(1000 * X / (1000 + C) / 1000) * 1000

print(real_money)
