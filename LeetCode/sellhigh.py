class Solution:
    def maxProfit(self, prices):
        if (len(prices) > 1):
            mini = min(prices)
            minipos = prices.index(mini)
            if (all(earlier >= later for earlier, later in zip(prices, prices[1:]))):
                return 0
            else:
                while(minipos == len(prices) - 1):
                    prices.remove(mini)
                    mini = min(prices)
                    minipos = prices.index(mini)
                while(len(prices) > 1):
                    maxi = max(prices)
                    maxipos = prices.index(maxi)
                    minipos = prices.index(mini)
                    if (maxipos > minipos):
                        return(maxi - mini)
                    prices.remove(maxi)
                return 0
        else:
            return 0