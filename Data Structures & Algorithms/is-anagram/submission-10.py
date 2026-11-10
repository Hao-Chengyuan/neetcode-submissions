class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        
        for s_char, t_char in zip(s, t):
            count[ord(s_char)-ord('a')] += 1
            count[ord(t_char)-ord('a')] -= 1
        
        return not any(count)
