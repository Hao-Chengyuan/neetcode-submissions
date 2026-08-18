class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kl, kr = 1, max(piles)
        res = kr
        while kl <= kr:
            km = (kl + kr) // 2
            hk = 0
            for pile in piles:
                hk += math.ceil(float(pile) / km)
            if hk <= h:
                res = km
                kr = km - 1
            else:
                kl = km + 1
        return res