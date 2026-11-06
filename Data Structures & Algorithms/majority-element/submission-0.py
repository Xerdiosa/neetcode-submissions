class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmpmajor = nums[0]
        occ = 1
        for i in nums[1:]:
            if i==tmpmajor:
                occ+=1
            else:
                occ-=1
                if occ==0:
                    tmpmajor=i
                    occ=1
        return tmpmajor
