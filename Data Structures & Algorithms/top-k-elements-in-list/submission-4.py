class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for i in range(len(nums)):
            key = str(nums[i])
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
        return [int(val) for _, val in sorted(zip(list(count.values()), list(count.keys())), reverse=True)][:k]
