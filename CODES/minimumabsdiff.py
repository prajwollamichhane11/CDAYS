n = int(input())

arr = list(map(int,input().split()))

minm = 1000000000

arr = sorted(arr)

for i in range(n-1):
    item = abs(arr[i]-arr[i+1])
    if item < minm:
        minm = item

print(minm)
