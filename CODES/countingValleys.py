n = int(input())
string = input()

sealevel = 0
numvalleys = 0

for i in range(n):
    if string[i] == 'U':
        sealevel += 1
    if string[i] == 'D':
        sealevel -= 1

    if sealevel == 0 and string[i] == 'U':
        numvalleys += 1


print(numvalleys)
