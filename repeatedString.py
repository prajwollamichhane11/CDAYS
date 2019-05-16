s = input()
n = int(input())
os = s
count = 0
cnta = 0
length = len(s)
len = length

for i in range (len):
    if s[i] == 'a':
        cnta += 1

count_string = n//len
count = count_string * cnta

x = count_string*len

i = 0
while x < n:
    if s[i] == 'a':
        count += 1
        x += 1
    else:
        x += 1
    i += 1

print (count)
