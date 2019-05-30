arr = []
sum = []

for i in range(6):
    arr.append([])
    arr[i] = list(map(int,input().split()))

for i in range(4):
    for j in range(4):
        sum.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

print(max(sum))
print("Github")
