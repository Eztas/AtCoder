S = input()
stock = -1

for i, s in enumerate(S):
    if s == '#':
        if stock == -1:
            stock = i + 1
        else:
            print(str(stock)+','+str(i + 1))
            stock = -1
