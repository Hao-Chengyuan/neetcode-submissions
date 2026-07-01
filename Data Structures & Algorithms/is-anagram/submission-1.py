class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert each string to a list of characters
        s_c = sorted([c for c in s])
        s_t = sorted([c for c in t])
        if s_c == s_t:
            return True
        else:
            return False