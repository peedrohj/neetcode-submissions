"""

Create an algorithm that can return the max diff between two numbers
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6


Requirements:
- You may choose to not make any transactions
- No profitable transactions can be made, thus the max profit is 0.

Solution:
- Have a pointer called buy and sell
- For each buy, get the max diff compared to sell.

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for begin in range(len(prices)):
            end = begin + 1

            while end < len(prices):
                print(f"{begin} - {end}")
                result = max(prices[end]-prices[begin], result)
                end += 1

        
        return result
        