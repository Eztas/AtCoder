import sys

data = sys.stdin.read().splitlines()

N = int(data[0])

S = []
T = []

for i in range(1, N + 1):
    S.append(data[i].split(' '))

for i in range(N + 1, 2 * N + 1):
    T.append(data[i].split(' '))