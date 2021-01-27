class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        print(len(strs))

        if strs == [""] or strs == []:
            return ""
        if len(strs) < 2:
            return strs[0]

        for i in range(len(strs)):
            strs[i] = list(strs[i])

        strs = sorted(strs)

        count = 0
        common = ""
        loop = 0

        while loop < len(strs[0]):

            temp = strs[0][loop]
            count = 0

            for i in range(len(strs)):
                print(i, temp)
                if temp == strs[i][loop]:
                    count += 1

            if count == len(strs):
                common += temp
            else:
                break

            loop += 1

        return common