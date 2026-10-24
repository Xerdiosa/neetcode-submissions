class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftEdge = [-1 for _ in range(len(heights))]
        rightEdge = [len(heights) for _ in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)>0:
                leftEdge[i]=stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if len(stack)>0:
                rightEdge[i]=stack[-1]
            stack.append(i)
        # print(leftEdge)    
        # print(rightEdge)
        ans = 0
        for i in range(len(heights)):
            ans=max((rightEdge[i]-leftEdge[i]-1)*heights[i],ans)
        return ans