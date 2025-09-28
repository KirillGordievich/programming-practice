"""
Мы можем перечислить середину палиндрома, распространить ее в обе стороны и найти самый длинный палиндром.

Сложность O(n^2), память O(1)

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper_fun(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left, right = left - 1, right + 1
            return right - left - 1

        n = len(s)
        start, mx = 0, 1
        for i in range(n):
            a = helper_fun(i, i)
            b = helper_fun(i, i + 1)
            t = max(a, b)
            if mx < t:
                mx = t
                start = i - ((t - 1) // 2)
        return s[start:start + mx]


sol = Solution()
print(sol.longestPalindrome("abadab"))
