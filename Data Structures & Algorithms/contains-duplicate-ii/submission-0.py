class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for l in range(len(nums)):
            for r in range(l+1, len(nums)):
                if nums[l] == nums[r] and r - l <= k:
                    return True
        return False