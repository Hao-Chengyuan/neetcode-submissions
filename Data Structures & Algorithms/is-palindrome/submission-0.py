class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_combo = ""
        for c in s:
            if c.isalnum():
                str_combo += c.lower()
        return str_combo == str_combo[::-1]
            
        