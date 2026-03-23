# Day 2: Review (Blind Write 2)
# Topic: Sliding Window / Greedy
# Problem: Best Time to Buy and Sell Stock (Easy)

# 規則：不准看之前的程式碼，不准看提示。完成後要求 Bug-free。
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time complexity: O(n)
        # Space complexity: O(1)
        left = 0
        right = 1
        ans = 0
        while right < len(prices):
            price = prices[right] - prices[left]
            if price > 0:
                ans = max(ans, price)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    # Case 1
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    # Case 2
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    print("Review 2: Best Time to Buy and Sell Stock PASSED!")
