n = int(input())
string = input()

sealevel = 0
numValleys = 0

for i in range(n):
    if string[i] == 'U':
        sealevel += 1
    if string[i] == 'D':
        sealevel -= 1

    if string[i] == 'U' and sealevel == 0:
        numValleys += 1

print (numValleys)
