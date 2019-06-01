n = int(input())

for i in range(n):
    num = int(input())
    f = bin(num)[2:].zfill(32)

    lst = list(f)

    for i in range(32):
        if lst[i] == "0":
            lst[i] = "1"
        else:
            lst[i] = "0"

    lst = "".join(lst)

    print(int(lst,2))
