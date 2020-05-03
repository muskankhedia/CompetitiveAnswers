class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        i = 0
        ransomNote = ''.join(sorted(ransomNote)) 
        magazine = ''.join(sorted(magazine)) 
        for j in magazine:
            if i < len(ransomNote):
                if j == ransomNote[i]:
                    i += 1
        if i == len(ransomNote):
            return True
        else:
            return False