import sys

data = sys.stdin.read().splitlines()
flag = False

for i in range(len(data[0]) - len(data[1]) + 1):
    for idx, word in enumerate(data[1]):
        if data[0][i + idx] != word and data[0][i + idx] != '?':
            flag = False
            break

        flag = True

if flag:
    print('Yes')
else:
    print('No')
