class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        lef, rig = 0, len(height) - 1

        while lef < rig:
            area = (rig - lef) * min(height[lef], height[rig])
            res = max(res, area)

            if height[lef] < height[rig]:
                lef += 1
            else:
                rig -= 1
        return res