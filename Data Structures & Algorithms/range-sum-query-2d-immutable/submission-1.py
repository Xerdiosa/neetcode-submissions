class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ps = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                self.ps[x][y]=matrix[x][y]+self.__query(x-1,y)+self.__query(x,y-1)-self.__query(x-1,y-1)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.__query(row2,col2)+self.__query(row1-1,col1-1)-self.__query(row1-1,col2)-self.__query(row2,col1-1)

    def __query(self, x:int, y:int) -> int:
        if x<0 or y<0 or x>=len(self.ps) or y>=len(self.ps[0]):
            return 0
        return self.ps[x][y]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)