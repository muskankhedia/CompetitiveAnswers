class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        l = len(coordinates)
        if l > 2:
            if x2-x1 == 0:
                for i in range(2, l):
                    if not x2 == coordinates[i][0]:
                        return False
                return True
            elif y2-y1 == 0:
                for i in range(2, l):
                    if not y2 == coordinates[i][1]:
                        return False
                return True
            else:
                m = (y2-y1)/(x2-x1)
                c = y2 - m*(x2)
                for i in range(2, l):
                    test = m*coordinates[i][0] + c
                    if not test == coordinates[i][1]:
                        return False
                return True
        else:
            return True