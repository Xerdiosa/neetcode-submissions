class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dct = dict()
        for i in hand:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
        for i in sorted(dct.keys()):
            if i not in dct or dct[i]==0:
                continue
            toreduce = dct[i]
            dct[i]=0
            for j in range(1, groupSize):
                if i+j not in dct or dct[i+j]<toreduce:
                    return False
                else:
                    dct[i+j]-=toreduce
        return True
            