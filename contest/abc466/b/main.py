def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)

N, M = map(int,input().split()) # それぞれの変数に数値を渡す

C = []
S = []
K = [-1] * M
for n in range(N):
    c, s = map(int,input().split()) # それぞれの変数に数値を渡す
    if K[c-1] < s:
        K[c-1] = s

print_horizontal_line(K, ' ')
