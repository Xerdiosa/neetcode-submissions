class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len(matrix[0]))-1
        maxright = (len(matrix)*len(matrix[0]))-1
        def access(idx):
            if idx > maxright:
                raise IndexError(f"index {idx} out of bound of {right}")
            x = idx//len(matrix[0])
            y = idx%len(matrix[0])
            print(x,y)
            if x >= len(matrix) or y>=len(matrix[0]):
                raise IndexError(f"index {x},{y}(from idx {idx}) out of bound of {matrix}")

            return matrix[x][y]            
        while left <= right:
            mid = (left+right)//2
            if access(mid) == target:
                return True
            elif access(mid) > target:
                right = mid-1
            else:
                left=mid+1
        return False