"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = left = 0
        for right, char in enumerate(s):
            while char in substring:
                # смещаем левый курсор на 1 вправо
                substring.remove(s[left])
                left += 1
            substring.add(char)
            max_len = max(max_len, right - left + 1)
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))
