X = int(input())
str_X = str(X)

sorted_X = sorted(str_X, reverse=False)
zero_flag = False
for idx, x in enumerate(sorted_X):
    if zero_flag == False and x != '0':
        print(''.join(sorted_X))
        break
    if zero_flag == True and x != '0':
        sorted_X[0] = x
        sorted_X[idx] = '0'
        print(''.join(sorted_X))
        break
    if x == '0':
        zero_flag = True
        