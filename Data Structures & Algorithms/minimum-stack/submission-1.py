class MinStack:

    def __init__(self):
        self.lst = []
        self.pm = []

    def push(self, val: int) -> None:
        if len(self.pm)==0:
            self.pm.append(val)
        else:
            if val<self.pm[-1]:
                self.pm.append(val)
            else:
                self.pm.append(self.pm[-1])
        self.lst.append(val)

    def pop(self) -> None:
        self.lst.pop()
        self.pm.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.pm[-1]
