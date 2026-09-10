class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window with size k
        # shrink when number of items in a window is greater than k
        res = 0
        sum_window = 0
        l = 0
        r = k

        while r <= len(arr):
            
            sum_window = sum(arr[l:r])

            if sum_window / k >= threshold:
                print(sum_window / k)
                res += 1
            
            r += 1
            l += 1
        
        return res