import sys
n = int(input())
n,m = map(int,input().split())

a = list(map(int,input().split()))
li = [list(map(int, input().split())) for _ in range(n)]
data = sys.stdin.read().splitlines()