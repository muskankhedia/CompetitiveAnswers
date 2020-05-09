class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = math.sqrt(num)
        if x == int(x):
            return True
        else:
            return False