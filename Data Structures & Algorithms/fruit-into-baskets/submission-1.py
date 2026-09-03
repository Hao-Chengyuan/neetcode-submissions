class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        maxf = 0
        l = 0

        for r in range(len(fruits)):
            window[fruits[r]] = window.get(fruits[r], 0) + 1

            # fixed basket size = 2
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1

            maxf = max(maxf, r - l + 1)
        
        return maxf