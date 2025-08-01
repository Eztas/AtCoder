# 手法1 ライブラリを使う
# 1進数などは変換できないので、そこに注意
# 2~36までしか使えないので注意

import numpy as np

n = 10
A = 2

np.base_repr(n, A) # nをA進数にする

# 手法2 自作関数
# 配列で返すので、strでキャストなどの工夫は必要
# 後おそらく計算も遅くなる

def base10int(value, base):

    # baseが1の場合は、計算せずに固定の結果を返す
    if base == 1:
        return [0] * (value + 1)
    
    digits = []
    temp_num = value
    while temp_num > 0:
        digits.append(temp_num % base)
        temp_num //= base

    digits.reverse()
    return digits

print(base10int(8, 1))
