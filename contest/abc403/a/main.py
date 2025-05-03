import sys

data = sys.stdin.read().splitlines()
numbers = data[1].split(' ') # pythonなら2行目の列のみでいい、数字はスペース区切り
total = 0

for idx, num in enumerate(numbers):
    if idx % 2 == 0:
        total += int(num)

print(total)