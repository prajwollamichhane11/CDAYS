n = int(input())
arr = list(map(int,input().split()))

pos = 0
count = 0

for i in range(n):
    pos += 2

    if pos < n:
        if arr[pos] == 0:
            count += 1
        else:
            pos -= 1
            count += 1

    elif (pos == n):
        count += 1

    else:
        break



print (count)
