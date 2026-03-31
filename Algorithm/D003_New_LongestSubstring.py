"""
======================================================
Day 3: New Question
Topic: Hash Table / Sliding Window
LeetCode: Longest Substring Without Repeating Characters (Medium)
======================================================

Description:
Given a string s, find the length of the longest substring without repeating characters.

Lenovo ISG Focus: 
這類「滑動視窗 (Sliding Window)」邏輯常用於：
1. 資料串流（Packet Stream）的連續特徵分析。
2. 系統 Log 的緩衝區（Buffer）視窗解析。
3. 韌體指令序列的去重與有效區間識別。

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: 在此實作 O(n) 解法
        left = 0
        right = left+1
        ans = 0
        seen = {}
        for right in range(len(s)):
            char = s[right]
            if char in seen:
                if seen[char] >= left:
                    left = seen[char] + 1
            seen[char] = right
            print(right-left)
            ans = max(ans, right-left+1)


        return ans



if __name__ == '__main__':
    sol = Solution()
    print("Running Test Cases...")
    
    # Case 1: s = "abcabcbb" -> Output: 3 ("abc")
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    
    # Case 2: s = "bbbbb" -> Output: 1 ("b")
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    
    # Case 3: s = "pwwkew" -> Output: 3 ("wke")
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    
    print("All Test Cases Passed!")
