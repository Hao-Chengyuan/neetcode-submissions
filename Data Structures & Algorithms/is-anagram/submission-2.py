class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a obvious false
        if len(s) != len(t):
            return False
        # sorted can take str input directly
        return sorted(s) == sorted(t)