n = int(input())

arr = list(map(int,input().split()))
listt = []

def subtract(a,b):
    return abs(a-b)

for i in range(n-1):
    for j in range(i+1,n):
        listt.append(subtract(arr[i],arr[j]))

listt = sorted(listt)
print(listt[0])
