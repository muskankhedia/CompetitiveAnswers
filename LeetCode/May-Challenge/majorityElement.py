import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici = {}
        if len(nums) == 1:
            return nums[0]
        l = int(len(nums) / 2)
        for i in nums:
            if i in dici.keys():
                dici[i] += 1
                if dici[i] > l:
                    return i
            else:
                dici[i] = 1
