A = int(input())
N = int(input())

# N=10^12
# ただのforループでは超過
# シンプルにNのフィルターが必要
# ざっとNを半分以下にする必要がある
# whileループにすればいける?

# まずNが回文である前提
# Aの数は必ず、10になるからならない
# 1~9までA以外が該当
# 2桁の数字 = 11, 22などの11の倍数の加算
# 3桁の数字 = 1~1, 2~2の100の位と1の位が同じ数値
# 4桁の数字 = 上2桁の反転が下2桁だが単純化できない, 1~1は必須で、1001+110+110
# 5桁の数字 = 1~1, 1010を加算する

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

total = 0
n = 1
while True:
    n_str = str(n)
    n_a = base10int(n, A)
    if n_str == n_str[::-1] and n_a == n_a[::-1]:
        total += n
    
    n += 1
    if n > N:
        break

print(total)
