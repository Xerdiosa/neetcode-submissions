class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        if len(self.stack)==0:
            self.stack.append((price,1))
            return 1
        ans = 1
        while len(self.stack)>0 and self.stack[-1][0]<=price:
            ans+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,ans))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)