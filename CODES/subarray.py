t = int(input())

while t > 0:
    sum = 0
    N,S = map(int,input().split())

    arr = list(map(int,input().split()))

    for i in range(N):
        j = i
        sum = 0
        while sum < S:
            sum += arr[i]

            if sum == S:
                print (j+1,i+1)
                pr = 0
                pass
            if sum > S:
                pr = -1
                break
            i += 1
        if pr == 0:
            break
    t -= 1
