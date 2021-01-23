# Simple Bootstrap Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = " "
        slen = len(s)

        slist = []
        slist[:0] = s

        retList = []

        if slen == 0:
            return 0
        elif s.isspace():
            return 1

        else:
            for i in range(slen):
                newList = []
                for j in range(i, slen):
                    if slist[j] not in newList:
                        newList.append(slist[j])

                        if j == slen - 1:
                            retList.append("".join(newList))

                    else:
                        retList.append("".join(newList))
                        break

            if retList == []:
                res = res = max(newList, key=len)
            else:
                res = max(retList, key=len)
            return len(res)