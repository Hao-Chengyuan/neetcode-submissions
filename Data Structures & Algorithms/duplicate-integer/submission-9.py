class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use the python built-in function `set`
        return len(set(nums)) != len(nums)