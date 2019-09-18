class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        le = len(costs)
        totalCost = 0
        countA = 0
        countB = 0
        same = 0
        le2 = int(le/2)
        for i in range(le2):
            n = costs[i]
            if (costs[i][0] < costs[i][1]):
                countA += 1
                totalCost += costs[i][0]
            elif (costs[i][0] > costs[i][1]):
                countB += 1
                totalCost += costs[i][1]
            else:
                same += 1
                totalCost += costs[i][0]
                # if (countA < countB):
                #     countA += 1
                #     totalCost += costs[i][0]
                # elif(countA > countB):
                #     countB += 1
                #     totalCost += costs[i][1]
                # else:
                #     countA += 1
                #     totalCost += costs[i][0]
        diff = [10000]*le2
        for i in range(le2, le):
            diff.append(costs[i][0] - costs[i][1])
        if (countA < countB):
            countA += same
        else:
            countB += same
        x = le2 - countA
        y = le2 - countB
        for i in range(x):
            minipos = diff.index(min(diff))
            diff[minipos] = 10000
            totalCost += costs[minipos][0]
            countA += 1
            
        for i in range(y):
            minipos = diff.index(min(diff))
            diff[minipos] = 10000
            totalCost += costs[minipos][1]
            countB += 1
            
        return totalCost