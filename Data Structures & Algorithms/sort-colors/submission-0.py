class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for i in nums:
            if i==0:
                red+=1
            elif i==1:
                white+=1
            elif i==2:
                blue+=1
        idx=0
        while red>0:
            nums[idx]=0
            idx+=1
            red-=1
        while white>0:
            nums[idx]=1
            idx+=1
            white-=1
        while blue>0:
            nums[idx]=2
            idx+=1
            blue-=1
