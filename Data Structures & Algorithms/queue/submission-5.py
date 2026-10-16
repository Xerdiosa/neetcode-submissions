class Deque:
    def __init__(self):
        self.Left = None
        self.Right = None


    def isEmpty(self) -> bool:
        return self.Left is None
        

    def append(self, value: int) -> None:
        if self.isEmpty():
            self.Left = Node(value)
            self.Right = self.Left
        else:
            tmp = Node(value)
            tmp.left = self.Right
            self.Right.right = tmp
            self.Right = tmp
        

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.Left = Node(value)
            self.Right = self.Left
        else:
            tmp = Node(value)
            tmp.right = self.Left
            self.Left.left = tmp
            self.Left = tmp        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.Right.left is None:
            rt = self.Right.val
            self.Left = None
            self.Right = None
            return rt
        else:
            rt = self.Right.val
            self.Right = self.Right.left
            self.Right.right = None
            return rt

        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.Left.right is None:
            rt = self.Left.val
            self.Left = None
            self.Right = None
            return rt
        else:
            rt = self.Left.val
            self.Left = self.Left.right
            self.Left.left = None
            return rt

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        
