def intersection(set1,set2):
    return set(set1).intersection(set2)

n = int(input())

for i in range(n):
    s1 = input()
    s2 = input()

    s1 = list(s1)
    s2 = list(s2)

    res = intersection(s1, s2)

    if(len(res) > 0):
        print("YES")
    else:
        print("NO")
