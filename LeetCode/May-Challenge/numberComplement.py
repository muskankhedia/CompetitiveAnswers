class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num).replace("0b", "") 
        new = ''
        for i in binary:
            if i == '0':
                new += '1'
            else:
                new += '0'
        return int(new,2) 