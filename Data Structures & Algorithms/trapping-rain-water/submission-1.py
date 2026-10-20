class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2:
            return 0
        ans = 0
        l = 0
        r = len(height)-1
        prev = min(l,r)
        prevpos = "l"
        if height[l]>height[r]:
            prev=min(height[r],height[l])
            prevpos="r"
            r=r-1
        else:
            prev=min(height[r],height[l])
            prevpos="l"
            l=l+1
        while l<=r:
            if prevpos=="l":
                water=max(prev-height[l],0)
                # if water>0:
                    # print(f"pos l l{l}r{r}, height: {water}.{prev}")
                ans+=water
            else:
                water=max(prev-height[r],0)
                # if water>0:
                    # print(f"pos r l{l}r{r}, height: {water}.{prev}")
                ans+=water                
            if height[l]>height[r]:
                prev=min(max(prev,height[r]),max(prev,height[l]))
                prevpos="r"
                r=r-1
            else:
                prev=min(max(prev,height[r]),max(prev,height[l]))
                prevpos="l"
                l=l+1
        return ans