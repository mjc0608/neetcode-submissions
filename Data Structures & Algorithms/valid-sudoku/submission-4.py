class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 3):
            for j in range(0, 3):
                mask = 0
                for ii in range(0, 3):
                    for jj in range(0, 3):
                        if board[i*3+ii][j*3+jj] == ".":
                            continue
                        off = (1 << int(board[i*3+ii][j*3+jj]))
                        if mask & off != 0:
                            return False
                        mask |= off

        for i in range(0, 9):
            mask = 0
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                off = 1 << int(board[i][j])
                if mask & off != 0:
                    return False
                mask |= off

        for j in range(0, 9):
            mask = 0
            print()
            for i in range(0, 9):
                if board[i][j] == ".":
                    continue
                off = 1 << int(board[i][j])
                if mask & off != 0:
                    return False
                mask |= off

        return True