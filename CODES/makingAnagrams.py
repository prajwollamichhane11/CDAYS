def intersection(set1, set2, la, lb):

    st1 = {}
    st2 = {}

    for i in range(la):
        st1[i] = set1[i]
    for i in range(lb):
        st2[i] = set2[i]

    return (st1 & st2)

if __name__ == '__main__':

    a = input()
    b = input()

    la = len(a)
    lb = len(b)

    L = intersection(list(a), list(b), la, lb)

    cnt_int = len(L)

    cnt_a = len(a)
    cnt_b = len(b)

    print(cnt_a+cnt_b-2*cnt_int)
