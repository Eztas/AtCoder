A = int(input())
N = int(input())

# 回文=そもそも半分さえ後ろを複製するだけで良い
# 奇数桁 = n/2+1さえあればいい
# 偶数桁 = n/2さえあればいい
# N=10^12で13桁, 10^7さえあればいい
# N/2の範囲で網羅できる

# Nまで計算するか、10^6(7桁)まで毎回見るかどうか

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

total = 0

# 1桁数字の計算
for n in range(1, 10):
    n_str = str(n)
    n_a = base10int(n, A)
    if n_str == n_str[::-1] and n_a == n_a[::-1]:
        total += n

# 2桁以上の計算
for n in range(1, 10**6):
    n_str = str(n)
    n_a = base10int(n, A)
    if n_str == n_str[::-1] and n_a == n_a[::-1]:
        total += n
    

print(total)
