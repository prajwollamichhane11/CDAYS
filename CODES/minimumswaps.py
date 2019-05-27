n = int(input())
arr = list(map(int,input().split()))

count = 0

for k in range(n):
    min = k
    for j in range(k+1, n):
        if arr[min] > arr[j]:
            min = j

    if arr[k] != arr[min]:
        count += 1
    arr[k], arr[min] = arr[min], arr[k]


print(count)
# count=0
#
# for x in range(0, len(arr)-1):
#     if arr[x]!=x+1:
#         b = arr.index(min(arr[x+1:len(arr)]))
#         arr[x], arr[b]= arr[b],arr[x]
#         count+=1
#
#     else:
#         continue
#
# print(count)
