class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hor = [set() for _ in range(9)]
        ver = [set() for _ in range(9)]
        grid = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9): 
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in ver[j]:
                    return False
                if board[i][j] in hor[i]:
                    return False
                if board[i][j] in grid[i//3][j//3]:
                    return False
                hor[i].add(board[i][j])
                ver[j].add(board[i][j])
                grid[i//3][j//3].add(board[i][j])
        return True