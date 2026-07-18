class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_pro = 0

        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_pro:
                max_pro = i - min_price

        return max_pro

        