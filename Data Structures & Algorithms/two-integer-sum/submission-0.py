class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_i, i in enumerate(nums):
            for j in range(idx_i+1, len(nums)):
                if i + nums[j] == target:
                    return [idx_i, j]
        return []
                    

        