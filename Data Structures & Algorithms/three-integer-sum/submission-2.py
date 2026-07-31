class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] == target and [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                else:
                    k -= 1
                    j += 1

        return res
