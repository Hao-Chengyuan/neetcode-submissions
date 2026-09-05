class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # window type: variable
        # validity condition: sum > target
        # invariant: target
        # shrink rule: while sum > target
        window = []
        res = len(nums)
        l = 0
        
        if sum(nums) < target:
            return 0
        
        for r in range(len(nums)):
            window.append(nums[r])

            while sum(window) >= target:
                res = min(res, r - l + 1)
                window.pop(0)
                l += 1

        return res