class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # variable window
        # validity condition: window_sum > target
        # invariant: window_sum > target
        # shrink rule: window_sum > target
        # expected complexity: O(n)
        res = len(nums) + 1
        window_sum = 0
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            if window_sum >= target:
                res = min(res, r - l + 1)

            while window_sum - nums[l] >= target and r < len(nums):
                window_sum -= nums[l]
                l += 1

                res = min(res, r - l + 1)
            print(res)

        if res == len(nums) + 1:
            return 0
        else:
            return res