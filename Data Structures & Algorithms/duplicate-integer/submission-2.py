class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist_num = []
        for num in nums:
            if num in exist_num:
                return True
            else:
                exist_num.append(num)
        return False