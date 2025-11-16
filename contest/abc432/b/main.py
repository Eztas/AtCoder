X = sorted(input()) # 最初からソート
for i in range(len(X)):
    if X[i] != '0':
        X[0], X[i] = X[i], X[0]
        break
print(''.join(X))