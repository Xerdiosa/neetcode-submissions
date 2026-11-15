class MyStack:
    from collections import deque
    def __init__(self):
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> int:
        tmp = deque()
        while len(self.d)>1:
            tmp.append(self.d.popleft())
        ans = self.d.popleft()
        self.d = tmp
        return ans

    def top(self) -> int:
        tmp = deque()
        while len(self.d)>1:
            tmp.append(self.d.popleft())
        ans = self.d.popleft()
        tmp.append(ans)
        self.d = tmp
        return ans

    def empty(self) -> bool:
        return len(self.d)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()