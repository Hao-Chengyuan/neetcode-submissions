class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window with size k
        # maintain a fixed window containing exactly k items
        sum_window = sum(arr[i] for i in range(k))

        if sum_window >= threshold * k:
            res = 1
        else:
            res = 0

        l = 0
        r = k - 1

        while r < len(arr) - 1:

            r += 1

            sum_window += (arr[r] - arr[l])

            l += 1

            if sum_window >= threshold * k:
                res += 1
        
        return res