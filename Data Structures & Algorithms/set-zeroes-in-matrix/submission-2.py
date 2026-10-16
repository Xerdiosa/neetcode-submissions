class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        up=False
        # down=False
        left=False
        # right=False

        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                up=True
            # if matrix[-1][i]==0:
            #     down=True
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                left=True
            # if matrix[i][-1]==0:
            #     right=True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        

        for i in range(1,len(matrix[0])):
            if matrix[0][i]==0:
                for j in range(len(matrix)):
                    matrix[j][i]=0
        for i in range(1,len(matrix)):
            if matrix[i][0]==0:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0


        if up:
            for i in range(len(matrix[0])):
                matrix[0][i]=0
        # if down:
        #     for i in range(len(matrix[0])):
        #         matrix[-1][i]=0
        if left:
            for i in range(len(matrix)):
                matrix[i][0]=0
        # if right:
        #     for i in range(len(matrix)):
        #         matrix[i][-1]=0        

        