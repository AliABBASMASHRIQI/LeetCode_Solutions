prices = [2,4,1]
# class Solution:
#     def maxProfit(self, prices) -> int:
#         min_price_stock = prices[0]
#         min_index = 0
#         max_price_stock = 0
#         max_index = 0
#         for i, price in enumerate(prices):
#             if price <= min_price_stock:
#                 min_price_stock = price
#                 min_index = i
#         print(min_index,":min_index")
#         for index in range(min_index,len(prices)):
#             print(index,":",prices[index])
#             if prices[index] >= max_price_stock:
#                 max_price_stock = prices[index]
#                 max_index = index
#         print(max_price_stock,"asas")
#         print(max_index,":max_index")
#         if min_index+1 == len(prices):
#             print(0)
#             return 0 
#         print(abs(max_price_stock-min_price_stock),":Answer")
#         return abs(max_price_stock-min_price_stock)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

            

sol = Solution()
sol.maxProfit(prices)