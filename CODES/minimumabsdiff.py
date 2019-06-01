n = int(input())

arr = list(map(int,input().split()))
listt = []

def subtract(a,b):
    return abs(a-b)

minm = 1000000000

for i in range(n-1):
    for j in range(i+1,n):
        item = subtract(arr[i],arr[j])
        if item < minm:
            minm = item

# listt = sorted(listt)
print(item)
