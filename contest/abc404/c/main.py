import sys

data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())

graph = [[] for _ in range(N)]

for i in range(1, M + 1):
    side = list(map(int, data[i].split(' ')))
    if len(graph[side[0] - 1]) < 2 and len(graph[side[1] - 1]) < 2:
        graph[side[1] - 1].append(side[0])
        graph[side[0] - 1].append(side[1])
    else:
        print("No")
        exit()

cycleGraph = [1 for _ in range(N)]

for i in range(1, N + 1):
    cycleGraph[i] = graph[i-1]