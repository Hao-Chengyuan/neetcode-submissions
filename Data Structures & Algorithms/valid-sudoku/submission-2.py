class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        nums = [i for i in range(1, 10, 1)]

        for i in range(9):
            row = board[i]
            column = [row[i] for row in board]
            print(column)

            row_nums = []
            column_nums = []

            for i in range(9):
                if row[i] != '.':
                    row_nums.append(row[i])

                if column[i] != '.':
                    column_nums.append(column[i])

            row_nums = sorted(row_nums)
            column_nums = sorted(column_nums)
            print(column_nums)

            for j in range(len(row_nums) - 1):
                if row_nums[j] == row_nums[j+1]:
                    return False
            for j in range(len(column_nums) - 1):
                if column_nums[j] == column_nums[j+1]:
                    return False

        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block = [row[c:c+3] for row in board[r:r+3]]
                flat_block = [item for row in block for item in row]

                block_nums = []

                for i in range(9):
                    if flat_block[i] != '.':
                        block_nums.append(flat_block[i])

                block_nums = sorted(block_nums)

                for j in range(len(block_nums) - 1):
                    if block_nums[j] == block_nums[j+1]:
                        return False
                    
        return True