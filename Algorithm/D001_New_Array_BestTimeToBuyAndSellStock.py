"""
======================================================
Day 1: Extra Bonus Question 2
Topic: Array / Greedy / Sliding Window
LeetCode: Best Time to Buy and Sell Stock (Easy)
======================================================

Description:
You are given an array `prices` where `prices[i]` is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a SINGLE day to buy one stock and choosing
a DIFFERENT day in the FUTURE to sell that stock.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Examples:
  Case 1: prices = [7, 1, 5, 3, 6, 4]  ->  Output: 5
          (Buy day 2 at price 1, sell day 5 at price 6, profit = 5)
  Case 2: prices = [7, 6, 4, 3, 1]     ->  Output: 0
          (Prices only go down, no profitable transaction possible)
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if len(prices) < 2: return 0
        left = 0
        right = 1
        ans = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1
                continue
            price = prices[right] - prices[left]    
            ans = max(ans, price)
            right += 1
        return ans



if __name__ == '__main__':
    sol = Solution()
    print("Running Test Cases...")
    prices = [7, 1, 5, 3, 6, 4]
    ans1 = sol.maxProfit(prices)
    assert ans1 == 5, f"Test Case 1 Failed: Expected 5, Got {ans1}"
    prices = [7, 6, 4, 3, 1]
    ans2 = sol.maxProfit(prices)
    assert ans2 == 0, f"Test Case 1 Failed: Expected 5, Got {ans2}"
    prices = [7, 1, 5, 3, 3, 3]
    ans3 = sol.maxProfit(prices)
    assert ans3 == 4, f"Test Case 1 Failed: Expected 5, Got {ans3}"
    prices = [1]
    ans4 = sol.maxProfit(prices)
    assert ans4 == 0, f"Test Case 1 Failed: Expected 5, Got {ans4}"
    # 請在這裡自己撰寫 Test Cases (至少 2 個 LeetCode 範例 + 2 個你自己想的 Edge Cases)
    # 格式範例:
    # assert sol.maxProfit([...]) == X, "Test Case N: ..."

    print("All Test Cases Passed!")
