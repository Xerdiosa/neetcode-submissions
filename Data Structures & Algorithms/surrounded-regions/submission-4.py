class Solution:
    def solve(self, board: List[List[str]]) -> None:
        import sys
        sys.setrecursionlimit(10**6)
        maxy = len(board[0])
        maxx = len(board)
        visited = [[False for _ in range(maxy)] for _ in range(maxx)]
        def hasEdge(x:int,y:int):
            if x<0 or y<0 or x>=maxx or y>=maxy:
                return True
            if visited[x][y]:
                return False
            visited[x][y] = True
            if board[x][y] == "X":
                return False
            return  hasEdge(x-1,y) | hasEdge(x+1,y) | hasEdge(x,y-1) | hasEdge(x,y+1)
        
        def fill(x:int,y:int):
            if x<0 or y<0 or x>=maxx or y>=maxy:
                return
            if board[x][y] == "X":
                return
            board[x][y]="X"
            fill(x-1,y) 
            fill(x+1,y) 
            fill(x,y-1) 
            fill(x,y+1)

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O" and not visited[x][y] and not hasEdge(x,y):
                    fill(x,y)

            
