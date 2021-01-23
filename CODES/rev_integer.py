class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)

        x = x[::-1]

        if x[-1] == "-":
            x = "-" + x[:-1]

        if (int(x) >= -(2 ** 31)) and (int(x) <= 2 ** 31 - 1):

            if x[-1] == "-":
                ss = "-" + x[:-1]
                return int(ss)
            else:
                return int(x)

        else:
            return 0