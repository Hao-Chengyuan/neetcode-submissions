class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # fixed window, size = k
        # shrink window when num of items > k
        window = []

        for r in range(len(arr)):
            window.append(arr[r])

            while len(window) > k:
                
                if abs(window[0] - x) < abs(window[-1] - x) or (abs(window[0] - x) == abs(window[-1] - x) and window[0] < window[-1]):

                    del window[-1]
                    return window
                
                else:

                    del window[0]
                    
        return window