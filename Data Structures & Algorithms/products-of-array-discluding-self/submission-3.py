class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p_list = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 1
                p = 1
                for num in nums:
                    p *= num
                p_list[i] = p
                nums[i] = 0
            
            else:
                p = 1
                for num in nums:
                    p *= num
                p_list[i] = int(p / nums[i])
            
        return p_list
