class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                transposed[y][x]=matrix[x][y]
        return transposed