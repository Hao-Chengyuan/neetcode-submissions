class Solution:
    def findMin(self, nums: List[int]) -> int:
        # cheating
        nums.sort()
        return nums[0]
