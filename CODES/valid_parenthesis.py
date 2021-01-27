def isValid():

    s = input()

    a = set(["(", ")"])
    b = set(["{", "}"])
    c = set(["[", "]"])

    d = set(["(", ")", "[", "]"])
    e = set(["(", ")", "{", "}"])
    f = set(["{", "}", "[", "]"])

    g = set(["(", ")", "{", "}", "[", "]"])

    if (
        set(s) == a
        or set(s) == b
        or set(s) == c
        or set(s) == d
        or set(s) == e
        or set(s) == f
        or set(s) == g
    ):
        return "true"
    else:
        return "false"


print(isValid())