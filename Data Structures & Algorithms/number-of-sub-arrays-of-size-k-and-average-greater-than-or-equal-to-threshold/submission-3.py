class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window with size k
        # shrink when number of items in a window is greater than k
        sum_window = sum(arr[0:k])

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