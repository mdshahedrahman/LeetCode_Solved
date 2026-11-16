class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_value = 10**4 
        max_value = 0 

        n = len (prices)
        # start = prices.index(min(prices))

        # if start != n:     
        for i in range (n):
            if prices[i] < min_value: 
                min_value = prices[i]
            # print (min_value)

            diff = prices[i] - min_value
            if max_value < diff:
                max_value = diff


        return max_value