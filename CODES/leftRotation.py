n,d = map(int,input().split())
arr = list(map(int,input().split()))

newarr = list()

for i in range(n):
    newarr.append(0)

for i in range(n):
    newarr[i-d] = arr[i]

for i in range(n):
    print(newarr[i], end =" ")
