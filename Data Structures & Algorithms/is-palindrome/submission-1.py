class Solution:
    def isPalindrome(self, s: str) -> bool:
        comb = ""
        for c in s:
            if c.isalnum():
                comb += c.lower()
        return comb == comb[::-1]