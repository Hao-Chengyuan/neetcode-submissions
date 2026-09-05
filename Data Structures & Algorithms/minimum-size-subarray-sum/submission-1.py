class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        length = len(nums) + 1
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                length = min(length, r - l + 1)
                window_sum -= nums[l]
                l += 1
                
        if length == len(nums) + 1:
            return 0
        else:
            return length