n = int(input())
arr = list(map(int,input().split()))

swaps = 0

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swaps += 1

print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element:",arr[0])
print("Last Element:",arr[n-1])
