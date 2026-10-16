import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] #max heap
        self.right = [] #min heap
    def addNum(self, num: int) -> None:
        #empty
        if len(self.left) == 0 and len(self.right) == 0:
            self.left.append(num)
            return 

        #1 data
        if len(self.right) == 0:
            if self.left[0] > num:
                tmp = self.left[0]
                self.left = [num]
                self.right.append(tmp)
                return
            else:
                self.right.append(num)
                return
        
        #next data, put either in left or right
        if self.left[0]>=num:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)
        #this might make left and right unbalanced
       
        if len(self.left) == len(self.right) or len(self.left)-1 == len(self.right):
            return #balanced
        elif len(self.left)-2==len(self.right):
            popped=heapq.heappop_max(self.left)
            heapq.heappush(self.right,popped)
        else:
            popped=heapq.heappop(self.right)
            heapq.heappush_max(self.left,popped)          



    def findMedian(self) -> float:
        # print(self.left,self.right)
        if len(self.left) == 0 and len(self.right) == 0:
            return 0.0
        if len(self.left) == len(self.right):
            return (self.left[0]+self.right[0])/2
        return self.left[0]
        