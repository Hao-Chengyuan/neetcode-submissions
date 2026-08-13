class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_nd = set(nums)
        if len(nums) != len(nums_nd):
            return True
        else:
            return False