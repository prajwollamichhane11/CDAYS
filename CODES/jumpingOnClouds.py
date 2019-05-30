n = int(input())
arr = list(map(int,input().split()))

p = 0
count = 0

for i in range(n):
    p += 2

    if p < n:
        if arr[p] == 0:
            count += 1
        else:
            p -= 1
            count += 1

    elif p == n:
        count += 1

    else:
        break

print(count)
