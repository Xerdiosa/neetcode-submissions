class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        tmp = 1
        ans = 1
        needBigger = None
        prev = arr[0]
        for i in arr[1:]:
            if needBigger is None:
                if prev>i:
                    needBigger=True
                    prev=i
                    tmp+=1
                    ans=max(ans,tmp)
                elif prev<i:
                    needBigger=False
                    prev=i
                    tmp+=1
                    ans=max(ans,tmp)
                else:
                    needBigger=None
                    prev=i
                    tmp=1
                    ans=max(ans,tmp)
            elif needBigger:
                if i>prev:
                    needBigger=False
                    prev=i
                    tmp+=1
                    ans=max(ans,tmp)
                elif i<prev:
                    needBigger=True
                    prev=i
                    tmp=2
                    ans=max(ans,tmp)
                else:
                    needBigger=None
                    prev=i
                    tmp=1
                    ans=max(ans,tmp)
            else:
                if i<prev:
                    needBigger=True
                    prev=i
                    tmp+=1
                    ans=max(ans,tmp)
                elif i>prev:
                    needBigger=False
                    prev=i
                    tmp=2
                    ans=max(ans,tmp)
                else:
                    needBigger=None
                    prev=i
                    tmp=1
                    ans=max(ans,tmp)
        return ans