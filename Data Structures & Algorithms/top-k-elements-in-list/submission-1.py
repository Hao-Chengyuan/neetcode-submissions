class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        sorted_nums = sorted(nums)

        non_repeat_nums = []

        for num in sorted_nums:
            if num in non_repeat_nums:
                continue
            else:
                non_repeat_nums.append(num)

        for num in sorted_nums:
            count[num] += 1
        
        count = list(count.values())

        res = []

        for i in range(k):
            idx_i = count.index(max(count))
            num_val = non_repeat_nums[idx_i]
            count[idx_i] = 0
            res.append(num_val)

        return res
        
        
        
