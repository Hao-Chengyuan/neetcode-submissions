class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        map1 = {}
        window = {}
        for i in range(n):
            map1[s1[i]] = map1.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1
        if window == map1:
            return True
        for r in range(n, len(s2)):
            window[s2[r-n]] -= 1
            window[s2[r]] = window.get(s2[r], 0) + 1
            if window[s2[r-n]] == 0:
                del window[s2[r-n]]
            if window == map1:
                return True
        return False