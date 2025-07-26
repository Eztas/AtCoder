S = input()
#T = S
T = []
for s in S:
    T.append(s)

def print_horizontal_line(dataList, endChar):
    for idx, data in enumerate(dataList):
        if idx < len(dataList) - 1:
            print(data,end=endChar)
        else:
            print(data)

dot_pos = -1
sharp_flag = False
for i in range(len(S)):
    if S[i] == '.' and dot_pos == -1:
        dot_pos = i
        T[i] = 'o'

    elif S[i] == '#' and dot_pos != -1 and sharp_flag == False:
        sharp_flag = True

    elif S[i] == '.' and dot_pos != -1 and sharp_flag == True:
        T[dot_pos] = 'o'
        T[i] = 'o'
        dot_pos = i
        sharp_flag = False

print_horizontal_line(T, '')
        