class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window = []
        left = 0

        for right in range(len(arr)):
            window.append(arr[right])

            while len(window) > k:
                if (abs(window[-1] - x) < abs(window[0] - x)) or (abs(window[-1] - x) == abs(window[0] - x) and window[-1] < window[0]):
                    window.pop(0)
                else:
                    window.pop(-1)
            
        return window