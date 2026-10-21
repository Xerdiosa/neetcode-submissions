class TimeMap:

    def __init__(self):
        self.keys=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        if timestamp<self.keys[key][0][0]:
            return ""
        return self.__search(self.keys[key], timestamp)
    def __search(self, nums, target) -> int:
        left = 0
        right = len(nums)-1
        ans=""
        while left <= right:
            mid = (left+right)//2
            if nums[mid][0] == target:
                return nums[mid][1]
            elif nums[mid][0] > target:
                right = mid-1
            else:
                ans=nums[mid][1]
                left=mid+1
        return ans
