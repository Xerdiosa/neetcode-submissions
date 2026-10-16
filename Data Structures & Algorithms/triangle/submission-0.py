class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        sol = [triangle[0]]
        for i in range(1,len(triangle)):
            row = []
            print(sol)
            for j in range(len(triangle[i])):
                if j == 0:
                    row.append(triangle[i][j]+sol[i-1][0])
                elif j == len(triangle[i])-1:
                    row.append(triangle[i][j]+sol[i-1][j-1])
                else:
                    m = 0
                    if sol[i-1][j]>sol[i-1][j-1]:
                        m = sol[i-1][j-1]
                    else:
                        m = sol[i-1][j]
                    row.append(triangle[i][j]+m)
            sol.append(row)
        minimum = "undefined"
        for i in range(len(sol[-1])):
            if minimum == "undefined":
                minimum=sol[-1][i]
                continue
            if minimum > sol[-1][i]:
                minimum = sol[-1][i]
        return minimum
        
        