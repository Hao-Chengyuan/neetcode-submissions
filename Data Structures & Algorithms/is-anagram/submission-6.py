class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use sort function
        return sorted(s) == sorted(t)