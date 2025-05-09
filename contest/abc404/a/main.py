import sys

data = sys.stdin.read().splitlines()

alphabetList = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

for alphabetForDelete in data[0]:
    for alphabet in alphabetList:
        if alphabetForDelete == alphabet:
            alphabetList.remove(alphabet)
            break

print(alphabetList[0])
