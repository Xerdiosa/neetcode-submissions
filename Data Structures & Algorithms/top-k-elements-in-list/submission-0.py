class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = dict()
        appearances = [set() for i in range(1,len(nums)+2)]
        for i in nums:
            if i in dct:
                freq = dct[i]
                appearances[freq].remove(i)
                appearances[freq+1].add(i)
                dct[i] = freq+1
            else:
                appearances[1].add(i)
                dct[i] = 1
        ret = []
        for i in appearances[::-1]:
            for j in i:
                ret.append(j)
                if len(ret)==k:
                    return ret
        #unreachable

