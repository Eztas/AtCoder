import itertools

# 配列の総当たりを担う
# Kの数だけSの要素を連結させたものの全パターンの用意が可能

S = [2, 3, 4]
K = 2

S_K_products = itertools.product(S, repeat=K)
