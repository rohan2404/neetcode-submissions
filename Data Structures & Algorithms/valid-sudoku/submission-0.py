class Solution:
    def isNumber(self, char: str) -> bool:
        try:
            x = int(char)
            return True
        except:
            return False
    def checkRow(self, row: List[str]) -> bool:
        numNumbers = 0
        seen = set()
        for x in row:
            if self.isNumber(x):
                numNumbers += 1
                seen.add(x)
        return (len(seen) == numNumbers)
    def transpose(self, board: List[List[str]]) -> List[List[str]]:
        out = [['.' for _ in range(len(board))] for _ in range(len(board[0]))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                out[row][col] = board[col][row]
        return out
    def unpackGrid(self, grid: List[List[str]]) -> List[str]:
        out = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                out.append(grid[row][col])
        return out
    def getGrid(self, i: int, j: int, board: List[List[str]], n: int = 3) -> List[List[str]]:
        grid = [['.' for _ in range(n)] for _ in range(n)]
        for row in range(i, i+n):
            for col in range(j, j+n):
                grid[row-i][col-j] = board[row][col]
        return grid
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows/cols for duplicates
        boardT = self.transpose(board)
        for row in range(len(board)):
            if self.checkRow(board[row]) and self.checkRow(boardT[row]):
                continue
            else:
                return False
        
        # check 3x3 grids for duplicates
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                grid = self.getGrid(i,j,board)
                unpacked = self.unpackGrid(grid)
                if not self.checkRow(unpacked):
                    return False
        return True