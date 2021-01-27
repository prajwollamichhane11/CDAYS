import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalList = sorted(nums1 + nums2)

        return np.median(finalList)