n = int(input())
ar = list(map(int,input().split()))
setlist = set(ar)
count = 0

for i in setlist:
    if(ar.count(i)//2 >= 1):
        count += 1
print(count)
