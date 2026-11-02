class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        atlanticVisited = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
        def pacificHelper(x,y,prev):
            if x<0 or y<0 or x>=len(heights) or y>=len(heights[0]):
                return
            if pacificVisited[x][y]:
                return
            if prev>heights[x][y]:
                return
            pacificVisited[x][y] = True
            pacificHelper(x+1,y,heights[x][y])
            pacificHelper(x-1,y,heights[x][y])
            pacificHelper(x,y+1,heights[x][y])
            pacificHelper(x,y-1,heights[x][y])
        def atlanticHelper(x,y,prev):
            if x<0 or y<0 or x>=len(heights) or y>=len(heights[0]):
                return
            if atlanticVisited[x][y]:
                return
            if prev>heights[x][y]:
                return
            atlanticVisited[x][y] = True
            atlanticHelper(x+1,y,heights[x][y])
            atlanticHelper(x-1,y,heights[x][y])
            atlanticHelper(x,y+1,heights[x][y])
            atlanticHelper(x,y-1,heights[x][y])        
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if x==0 or y==0:
                    pacificHelper(x,y,0)
                if x==len(heights)-1 or y==len(heights[0])-1:
                    atlanticHelper(x,y,0)
        ans = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if pacificVisited[x][y] and atlanticVisited[x][y]:
                    ans.append([x,y])
        return ans
