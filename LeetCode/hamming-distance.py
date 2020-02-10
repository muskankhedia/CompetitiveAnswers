class Solution:
            
    def hammingDistance(self, x: int, y: int) -> int:
        xx = bin(x).replace("0b", "")
        yy = bin(y).replace("0b", "")
        print(xx + "  " + yy)
        print(len(xx))
        diff = len(xx) - len(yy)
        if diff > 0:
            yy = ('0' * diff) + yy
        else:
            xx = ('0' * abs(diff)) + xx
        count = 0
        for i in range(0, len(xx)):
            if not xx[i] == yy[i]:
                count += 1
        return count
        
        