class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # using the strict-valid while approach
        res = 0
        window_sum = 0
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]
            
            if window_sum + k >= r - l + 1:
                res = max(res, r - l + 1)

            while window_sum + k < r - l + 1 and l < r:
                window_sum -= nums[l]
                l += 1
            print(res)
            
        return res
