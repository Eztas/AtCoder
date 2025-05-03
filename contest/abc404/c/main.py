import sys

data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())

graph = [0 for _ in range(N)]

for i in range(1, M + 1):
    side = list(map(int, data[i].split(' ')))
    if graph[side[0] - 1] == 0 or graph[side[0] - 1] == side[1]:
        graph[side[0] - 1] = side[1]
    else:
        print("No")
        exit()
        