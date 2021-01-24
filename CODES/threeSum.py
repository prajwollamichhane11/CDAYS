class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        print(nums)

        lenNums = len(nums)

        fir = 1
        las = lenNums - 1

        origLis = []

        for i in range(lenNums):
            fir = i + 1
            las = lenNums - 1

            while fir < las:

                if nums[i] + nums[fir] + nums[las] == 0:
                    tempLis = [nums[i], nums[fir], nums[las]]
                    if tempLis not in origLis:
                        origLis.append(tempLis)
                    fir += 1

                elif nums[i] + nums[fir] + nums[las] < 0:
                    fir += 1

                elif nums[i] + nums[fir] + nums[las] > 0:
                    las -= 1

        print(origLis)
        return origLis