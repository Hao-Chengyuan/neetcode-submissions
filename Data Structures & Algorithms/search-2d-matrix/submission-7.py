class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n))
        m, n = len(matrix), len(matrix[0])
        row_idx = 0
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        i, j = 0, m - 1
        while i < j:
            if target > matrix[i][-1] and target <= matrix[j][-1]:
                i += 1
            elif target < matrix[j][0] and target >= matrix[i][0]:
                j -= 1
            else:
                i += 1
                j -= 1
            row_idx = i
        l, r = 0, n - 1
        while l <= r:
            if matrix[row_idx][l] < target:
                l += 1
            elif matrix[row_idx][r] > target:
                r -= 1
            else:
                return True
        return False