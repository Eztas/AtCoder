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

# 1桁数字の計算, Nが1桁の時の対応を忘れていた
for n in range(1, 10):
    if n <= N:
        n_str = str(n)
        n_a = base10int(n, A)
        if n_a == n_a[::-1]:
            total += n

# 2桁以上の計算(偶数列, 奇数列の追加)
# 999999|999999, 10^12,1000000|000000
for n in range(1, 10**6):
    n_str = str(n)
    # 間に数字を挟まずに反転したものを追加
    n_str_mirror = n_str + n_str[::-1]
    if int(n_str_mirror) <= N:
        n_a = base10int(int(n_str_mirror), A)
        if n_a == n_a[::-1]:
            total += int(n_str_mirror)
    else:
        break
            
    # 間に数字を挟んで反転したものを追加
    for i in range(0, 10):
        n_str_mirror_sand = n_str + str(i) + n_str[::-1]
        if int(n_str_mirror_sand) <= N:
            n_a = base10int(int(n_str_mirror_sand), A)
            if n_a == n_a[::-1]:
                total += int(n_str_mirror_sand)
    
print(total)
