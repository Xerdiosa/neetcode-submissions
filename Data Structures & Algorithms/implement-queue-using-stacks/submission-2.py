class MyQueue:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        tmp = []
        while len(self.s)>1:
            tmp.append(self.s.pop())
        ans = self.s[0]
        tmp2 = []
        while len(tmp)>0:
            tmp2.append(tmp.pop())
        self.s=tmp2
        return ans

    def peek(self) -> int:
        tmp = []
        while len(self.s)>1:
            tmp.append(self.s.pop())
        ans = self.s[0]
        tmp.append(self.s.pop())
        tmp2=[]
        while len(tmp)>0:
            tmp2.append(tmp.pop())
        self.s=tmp2
        return ans

    def empty(self) -> bool:
        return len(self.s)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()