"""
======================================================
Day 2: New Question
Topic: Array / Two Pointers / Sorting
LeetCode: 3Sum (Medium)
======================================================

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TODO: 實作。考慮到 Two Sum 的經驗與 Two Pointers。
        # 注意重複 triplet 的處理。
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                
                if nums[left] + nums[right] == target:
                    # if ([nums[i], nums[left], nums[right]]) not in ans:
                    ans.append([nums[i], nums[left], nums[right]])
                    if nums[left] == nums[left+1]:
                        left += 1
                    if nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

            
        return ans

if __name__ == '__main__':
    sol = Solution()
    print("Running Test Cases...")
    nums = [-1,0,1,2,-1,-4] 
    assert sol.threeSum(nums) == [[-1,-1,2],[-1,0,1]]
    nums = [0,1,1] 
    assert sol.threeSum(nums) == []
    nums = [0,0,0]
    assert sol.threeSum(nums) == [[0,0,0]]
    
    # 請在此補上至少 3 個 Test Cases (包含 LeetCode 範例與 Edge Cases)
    # Case 1: nums = [-1,0,1,2,-1,-4] -> Output: [[-1,-1,2],[-1,0,1]]
    # Case 2: nums = [0,1,1] -> Output: []
    # Case 3: nums = [0,0,0] -> Output: [[0,0,0]]
