class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr_len = 9

        # Validate rows
        for i in range(arr_len):
            num_set = set()
            for j in range(arr_len):
                cell = board[i][j]
                if cell != ".":
                    if cell in num_set:
                        return False
                    num_set.add(cell)

        # Validate columns
        for i in range(arr_len):
            num_set = set()
            for j in range(arr_len):
                cell = board[j][i]
                if cell != ".":
                    if cell in num_set:
                        return False
                    num_set.add(cell)

        for box_row in range(0, arr_len, 3):
            for box_col in range(0, arr_len, 3):
                num_set = set()
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row+i][box_col+j]
                        if cell != ".":
                            if cell in num_set:
                                return False
                            num_set.add(cell)


        return True
            