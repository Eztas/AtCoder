N = int(input())
S = input().split() # 入力例: ". # ." -> ['.', '#', '.']

# o=人がいる, x=人いない
# 椅子がない = 左端
S_edge = ['x'] + S + ['x']
print(S_edge)
count = 0

for n in range(N+2):
    if n == 0 or n == N+1:
        continue
    else:
        print('n='+str(n))
        if S_edge[n-1] == 'x' and S_edge[n] == 'x' and S_edge[n+1] == 'x':
            count += 1

print(count)
