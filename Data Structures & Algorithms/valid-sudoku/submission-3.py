class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        # row
        for row_idx in range(9):
            num_set = set()
            for col_idx in range(9):
                ch = board[row_idx][col_idx]

                if ch in num_set and ch != ".":
                    return False
                num_set.add(ch)


        # column
        for col_idx in range(9):
            num_set = set()
            for row_idx in range(9):
                ch = board[row_idx][col_idx]

                if ch in num_set and ch != ".":
                    return False
                num_set.add(ch)

        # matrix
        row_idx,col_idx = 0,0
        for row_idx in range(0, 9, 3):
            for col_idx in range(0, 9, 3):
                num_set = set()
                for i in range(row_idx, row_idx + 3):
                    for j in range(col_idx, col_idx + 3):
                        ch = board[i][j]

                        if ch in num_set and ch != ".":
                            return False
                        num_set.add(ch)

        return True