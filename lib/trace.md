# 動的計画法

「数え上げ」かつ「順序が固定」されていると使える

$i$ 文字目までの部分列の総数を知りたいとき。実は「$(i-1)$ 文字目までの結果」さえ分かれば、新しい文字を「くっつける」か「くっつけない」かの2択を考えるだけで、$i$ 文字目の答えが出ます。

[応用1](./../contest/abc410/e/main.py)

[応用2](./../contest/abc415/c/main.py) (2値)

[応用3](./../contest/abc456/s/main.py) (3値)

# 貪欲法

[基礎1](./../contest/abc412/c/main.py)

# 尺取法

[基礎1](./../contest/abc430/c/main.py)

# 1 つの入力ファイルにおける N の総和は 2×10^5(その他任意の数)以下

[例1](https://atcoder.jp/contests/abc412/tasks/abc412_c)

[結果1](./../contest/abc412/c/main.py)

[例2](https://atcoder.jp/contests/abc413/tasks/abc413_d)

[結果2](./../contest/abc413/d/main.py)

# forループで素直に数えると計算量超過する時は‥

## 境目の数を数える

[例1](https://atcoder.jp/contests/abc411/tasks/abc411_c)

[結果1](./../contest/abc411/c/main.py)

## 個数を数えてから差分系

[例1](https://atcoder.jp/contests/abc449/tasks/abc449_c)

[結果1](./../contest/abc449/c/main.py)


# 幅優先×迷路

[例1](https://atcoder.jp/contests/abc420/tasks/abc420_d)

[結果1](./../contest/abc420/d/main.py)

# 毎度降順に並べながら、その値の個数とかも管理しつつ計算したい(heapq)

[例1](https://atcoder.jp/contests/abc423/tasks/abc423_d)

[結果1](./../contest/abc423/d/main.py)

[例2](https://atcoder.jp/contests/abc426/tasks/abc426_c)

[結果2](./../contest/abc426/c/main.py)

# 重複の計算に困ったらset

[例1](https://atcoder.jp/contests/abc430/tasks/abc430_b)

[結果1](./../contest/abc430/b/main.py)

# 最小値の最大化（または最大値の最小化）

単調性があれば、二分探索で判定しながら、ある値以上になるのかどうかを判定する

[例1](https://atcoder.jp/contests/abc457/tasks/abc457_d)

[結果1](./../contest/abc457/d/main.py)

`bisect_left(num, x): 「x以上の最小の値の位置」を知りたい`

`bisect_right(num, x): 「x以下の最大の値の位置」を知りたい`

# いずれ解けそう(何となくはわかるが、今はまだ言語化できない)

[abc411-D-Conflict2](https://atcoder.jp/contests/abc411/tasks/abc411_d)

[abc415-C-Mixture](https://atcoder.jp/contests/abc415/tasks/abc415_c)

[abc417-C-Distance Indicators](https://atcoder.jp/contests/abc417/tasks/abc417_c)

[abc425-C-Rotate and Sum Query](https://atcoder.jp/contests/abc425/tasks/abc425_c)

[abc455-D-Card Pile Query](https://atcoder.jp/contests/abc455/tasks/abc455_d)

[abc457-E-Crossing Table Cloth](https://atcoder.jp/contests/abc457/tasks/abc457_e)

# 個人的悔しい

[abc423-C-Lock All Doors](https://atcoder.jp/contests/abc423/tasks/abc423_c)

[abc430-B-Count Subgrid](https://atcoder.jp/contests/abc430/tasks/abc430_b)

[abc467-C-Adjacent Sums (easy)](https://atcoder.jp/contests/abc467/tasks/abc467_c)
