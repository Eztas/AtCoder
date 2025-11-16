A, B, C = map(int,input().split())

num = []
num.append(100*A+10*B+C)
num.append(100*A+10*C+B)
num.append(100*B+10*A+C)
num.append(100*B+10*C+A)
num.append(100*C+10*A+B)
num.append(100*C+10*B+A)

print(max(num))
