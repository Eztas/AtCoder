# 手法1 ライブラリを使う
# 1進数などは変換できないので、そこに注意
# 2~36までしか使えないので注意

import numpy as np

n = 10
A = 2

np.base_repr(n, A) # nをA進数にする
