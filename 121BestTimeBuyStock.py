from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        if len(prices) == 1:
            return 0

        # BRUTE FORCE
        # for x in range(0, len(prices)):
        #     for y in range(x, len(prices)):
        #         if prices[y] - prices[x] > maxP:
        #             maxP = prices[y] - prices[x]
        # return maxP

        for x in range(0, len(prices)):
            if max(prices) - prices[x] > maxP:
                maxP = max(prices) - prices[x]
                prices[x] = 0
            else:
                prices[x] = 0
        return maxP


print(Solution.maxProfit(Solution, [7, 1, 5, 3, 6, 4]))
print(Solution.maxProfit(Solution, [7, 6, 4, 3, 1]))
print(Solution.maxProfit(Solution, [7, 11, 1, 2, 4]))
