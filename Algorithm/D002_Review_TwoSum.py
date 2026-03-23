# Day 2: Review (Blind Write 1)
# Topic: Hash Table
# Problem: Two Sum (Easy)

# 規則：不准看之前的程式碼，不准看提示。完成後要求 Bug-free。
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity : O(n)
        # Space Complexity: O(n)
        seen = {}
        
        for i in range(len(nums)):         
            if target - nums[i] not in seen:
                seen[nums[i]] = i
            else:
                return [i, seen[target-nums[i]]]

        return None

if __name__ == '__main__':
    sol = Solution()
    # Case 1
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    # Case 2
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    # Case 3
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]
    print("Review 1: Two Sum PASSED!")
