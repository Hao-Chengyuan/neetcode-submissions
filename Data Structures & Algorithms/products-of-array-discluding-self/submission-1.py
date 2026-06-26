class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []

        for i in range(len(nums)):
            array_wo = nums[:i] + nums[i+1:]
            product = 1

            for item in array_wo:
                product *= item
            
            output.append(product)
        
        return output