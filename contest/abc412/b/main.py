S = input()
T = input()

result = 'Yes'

for n in range(1, len(S)):
    if S[n].isupper() == True:
        if T.find(S[n-1]) != -1:
            result = 'Yes'
        else:
            result = 'No'
            break
    
print(result)
