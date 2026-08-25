class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        cmap = {}
        for r in range(len(s)):
            if s[r] in cmap:
                l = max(cmap[s[r]] + 1, l)
            cmap[s[r]] = r
            res = max(res, r - l + 1)
        return res