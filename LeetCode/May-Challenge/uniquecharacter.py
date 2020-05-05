class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        c = Counter(s)
        for i in s:
            print (c[i])
            if c[i] == 1:
                return s.index(i)
        return -1