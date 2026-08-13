class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diff = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_diff:
                return [dict_diff[diff], i]
            dict_diff[num] = i
        return []
