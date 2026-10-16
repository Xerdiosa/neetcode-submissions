class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up=0
        down=len(matrix)
        left=0
        right=len(matrix[0])
        ans=[]
        step=0
        while True:
            step=0
            # print(up,down,left,right)
            if up!=down:
                for i in range(left,right):
                    ans.append(matrix[up][i])
                    # print("right")
                    step+=1
                up+=1
            # print(up,down,left,right)
            if left!=right:
                for i in range(up,down):
                    ans.append(matrix[i][right-1])
                    # print("down")
                    step+=1
                right-=1
            # print(up,down,left,right)
            if up!=down:
                for i in range(right-1, left-1, -1):
                    ans.append(matrix[down-1][i])
                    # print("left")
                    step+=1
                down-=1
            # print(up,down,left,right)
            if left!=right:
                for i in range(down-1, up-1, -1):
                    ans.append(matrix[i][left])
                    # print("up")
                    step+=1
                left+=1
            if step==0:
                break
        return ans