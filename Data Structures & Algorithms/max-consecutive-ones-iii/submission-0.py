class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # variable window
        l = 0
        res = 0
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            if window_sum + k >= r - l + 1:
                res = max(res, r - l + 1)
            else:
                window_sum -= nums[l]
                l += 1
        
        return res
