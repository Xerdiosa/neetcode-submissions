class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        mn = max(nums)
        prime_candidate=[True for i in range(mn+1)]
        for i in range(2,len(prime_candidate)):
            if prime_candidate[i]==False:
                continue
            tmp = i+i
            while tmp<=mn:
                prime_candidate[tmp]=False
                tmp+=i
        primes = []
        for i in range(2,len(prime_candidate)):
            if prime_candidate[i]:
                primes.append(i)

        def factorize(n):
            factor = []
            for prime in primes:
                if prime>n:
                    break
                if n%prime==0:
                    factor.append(prime)
                    while n%prime==0:
                        n=n//prime
            return factor
        factormap = dict()

        ds = [i for i in range(len(nums))]
        def union(idx1,idx2):
            ds[find(idx1)]=find(idx2)

        def find(num):
            toCompress = []
            while ds[num]!=num:
                toCompress.append(num)
                num=ds[num]
            for i in toCompress:
                ds[i]=num
            return num

        for i in range(len(nums)):
            factor = factorize(nums[i])
            for f in factor:
                if f in factormap:
                    union(i,factormap[f])
                else:
                    factormap[f]=i
        
        king = find(0)
        for i in range(1,len(nums)):
            if find(i)!=king:
                return False
        return True
