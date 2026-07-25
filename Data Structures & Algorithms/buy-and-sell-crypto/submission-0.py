class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        n = len(prices)
        maxProfit = 0
        profit = 0
        while j<n:
            
            if prices[j] > prices[i]:
                profit= prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
                j+=1

            
            else:
                profit= 0
                i = j
                j +=1

        return maxProfit
