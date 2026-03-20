"""
======================================================
Day 1: Extra Bonus Question
Topic: Array / Two Pointers / Greedy
LeetCode: Container With Most Water (Medium)
======================================================

Description:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # TODO: 在這裡實作你的解答
        # Time Complexity: O(n)
        # Space Complexity:: O(1)
        if len(height) < 2:
            return 0
        elif len(height) == 2:
            return min(height[0] , height[1]) 
        right = len(height) - 1
        left = 0
        ans = 0
        while left < right:
            area = min(height[left] , height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
        
            

if __name__ == '__main__':
    sol = Solution()
    print("Running Test Cases...")
    
    # Case 1
    h1 = [1,8,6,2,5,4,8,3,7]
    ans1 = sol.maxArea(h1)
    assert ans1 == 49, f"Test Case 1 Failed: Expected 49, Got {ans1}"
    
    # Case 2
    h2 = [1,1]
    ans2 = sol.maxArea(h2)
    assert ans2 == 1, f"Test Case 2 Failed: Expected 1, Got {ans2}"

    print("All Test Cases Passed! 接下去請向面試官說明 Time & Space Complexity。")
