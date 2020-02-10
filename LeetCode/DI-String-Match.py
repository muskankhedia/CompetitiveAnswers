class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        arr = []
        ptr1, ptr2 = 0, len(S)
        for i in S:
            if i == 'I':
                arr.append(ptr1)
                ptr1 += 1
            else:
                arr.append(ptr2)
                ptr2 -= 1
        return (arr + [ptr1])