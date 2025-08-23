N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)

for b in B:
    if b in A:
        A.remove(b)

print_horizontal_line(A, ' ')
