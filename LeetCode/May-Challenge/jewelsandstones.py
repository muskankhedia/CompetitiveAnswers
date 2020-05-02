#DAY 2

class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in J:
            if i in S:
                for j in S:
                    if i == j:
                        count += 1
        return count