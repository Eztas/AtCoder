N, Q = map(int, input().split())

# 上と下を更新すればどこの山のどこに載せるかの追跡ができる
# 山の上下と、カードがどの山にあるのかの理解
# up_i = カード i のすぐ上にあるカード（なければ −1）
# down_i = カード i のすぐ下にあるカード（なければ −1）
# 互いの上下を理解していれば、枚数計算も早い？
mountain_bottom = [for n in range(N)] # 山全体の下
mountain_top = [for n in range(N)] # 山全体の上
under = [0] * N # 操作する山の下
above = [0] * N # 操作する山の上
mountains = [1] * N

# 下 = 丸々なくなるか

for _ in range(Q):
    C, P = map(int, input().split())
    c = C - 1 # index
    p = P - 1 # index
    mountain_bottom[]
    mountain_top = [for n in range(N)]
    
