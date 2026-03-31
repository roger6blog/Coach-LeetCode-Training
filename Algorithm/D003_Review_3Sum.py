# Day 3: Review (Blind Write 1)
# Topic: Two Pointers / Sorting
# Problem: 3Sum (Medium)
# Lenovo Context: Sorting and multi-pointer logic is fundamental for hardware resource allocation and scheduling.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TODO: 盲寫最佳解 (O(n^2) Time, O(1) Space excluding output)
        # 規則：不准看昨天的紀錄，不准用 `if x in list` 做重複檢查。
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        print(ans)
        return ans





if __name__ == '__main__':
    sol = Solution()
    print("Running 3Sum Review...")
    # Case 1
    assert sorted([sorted(x) for x in sol.threeSum([-1,0,1,2,-1,-4])]) == sorted([sorted(x) for x in [[-1,-1,2],[-1,0,1]]])
    # Case 2
    assert sol.threeSum([0,1,1]) == []
    # Case 3
    assert sol.threeSum([0,0,0]) == [[0,0,0]]
    print("3Sum Review: PASSED!")
