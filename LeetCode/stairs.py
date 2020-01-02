def minCostClimbingStairs(cost):
    
    def climbingDown(total, costList):
        if (len(costList) > 1):
            l = len(costList)
            cost1 = total + costList[l-1]
            cost2 = total + costList[l-2]
            if (cost1 < cost2):
                costList.pop()
                finalcost = cost1
            else:
                del costList[l-2:l]
                finalcost = cost2
            return(climbingDown(finalcost, costList))
        else:
            return total
    
    def climbingUp(total, costList2):
        if (len(costList2) > 1):
            l = len(costList2)
            cost1 = total + costList2[0]
            cost2 = total + costList2[1]
            if (cost1 < cost2):
                costList2.pop(0)
                finalcost = cost1
            else:
                costList2.pop(0)
                costList2.pop(0)
                finalcost = cost2
            return(climbingUp(finalcost, costList2))
        else:
            return total
    costLists = cost[:]
    return min(climbingUp(0, cost), climbingDown(0, costLists))

print(minCostClimbingStairs([0,2,2,1]))