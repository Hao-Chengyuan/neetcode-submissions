class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            idx = (l + r) // 2
            row = idx // n
            col = idx % n
            if target < matrix[row][col]:
                r = idx - 1
            elif target > matrix[row][col]:
                l = idx + 1
            else:
                return True
        return False