class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)

        lenNums = len(nums)

        closest = 999999999999

        if lenNums < 3:
            return None

        for i in range(lenNums):
            fir = i + 1
            las = lenNums - 1

            while fir < las:
                sumThree = nums[i] + nums[fir] + nums[las]

                diff = abs(sumThree - target)

                if diff <= closest:
                    closest = diff
                    output = sumThree

                if sumThree > target:
                    las -= 1

                if sumThree <= target:
                    fir += 1

        return output
