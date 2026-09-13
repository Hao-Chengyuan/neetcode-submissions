class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # variable window
        # in each window, it should follow the number of the same char + k should be greater than or equal to window length
        window = {}
        res = 0
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxfreq = max(maxfreq, window[s[r]])
            
            while maxfreq + k < r - l + 1:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res