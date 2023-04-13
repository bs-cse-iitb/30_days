class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max1 = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            if prices[i]> buy:
                max1 = max(max1,prices[i]-buy)
            else:
                buy =prices[i]

        return max1