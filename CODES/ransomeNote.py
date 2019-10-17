from collections import Counter

#inputs
a,b = map(int,input().split())
magazine = input().split()
notes = input().split()

magz = Counter(magazine)
notz = Counter(notes)

result = notz - magz

if result == {}:
    print("Yes")
else:
    print("No")
