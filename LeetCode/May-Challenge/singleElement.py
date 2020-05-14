class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        temp = min(c.values())
        res = [key for key in c if c[key] == temp]
        return res[0]