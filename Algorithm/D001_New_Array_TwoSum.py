"""
======================================================
Day 1: New Question
Topic: Array / Hash Table
LeetCode: Two Sum (Easy)
======================================================

Description:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up:
Can you come up with an algorithm that is less than O(n^2) time complexity?
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 嚴禁看解答。完成後請主動回報 Time & Space Complexity。
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        ans = []
        if len(nums) < 2:
            return []
        cache = {}
        for i in range(len(nums)):
            if nums[i] not in cache:
                cache[target-nums[i]] = i
                
            else:
                return [i, cache[nums[i]]]

        return ans
                    


if __name__ == '__main__':
    sol = Solution()
    print("Running Test Cases...")
    
    # Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    ans1 = sol.twoSum(nums1, target1)
    # The output could be [0, 1] or [1, 0], we sort it for assertion
    assert ans1 is not None and sorted(ans1) == [0, 1], f"Test Case 1 Failed: Expected [0, 1], Got {ans1}"
    
    # Case 2
    nums2, target2 = [3, 2, 4], 6
    ans2 = sol.twoSum(nums2, target2)
    assert ans2 is not None and sorted(ans2) == [1, 2], f"Test Case 2 Failed: Expected [1, 2], Got {ans2}"
    
    # Case 3
    nums3, target3 = [3, 3], 6
    ans3 = sol.twoSum(nums3, target3)
    assert ans3 is not None and sorted(ans3) == [0, 1], f"Test Case 3 Failed: Expected [0, 1], Got {ans3}"
    
    print("All Test Cases Passed! 接下去請向面試官說明 Time & Space Complexity。")
