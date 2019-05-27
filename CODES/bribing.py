t = int(input())

count = 0
run = 1

for c in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n):
        if abs((i+1)-arr[i]) > 2:
            run = 0
            print("Too chaotic")
            break

    if (run == 1):
        for k in range(len(arr)):
            min_idx = k
            for j in range(k+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    count += 1
                    min_idx = j

            arr[k], arr[min_idx] = arr[min_idx], arr[i]


        print(count)
