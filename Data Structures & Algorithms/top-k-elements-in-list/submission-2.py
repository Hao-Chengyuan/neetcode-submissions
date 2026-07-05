class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        count_list = sorted(count.values(), reverse=True)
        return [key for key, val in count.items() if val in count_list[:k]]