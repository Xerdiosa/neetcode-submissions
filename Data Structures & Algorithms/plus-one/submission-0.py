class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]=digits[-1]+1
        havecarry = digits[-1]>=10
        digits[-1]=digits[-1]%10
        for i in range(len(digits)-2,-1,-1):
            if havecarry:
                digits[i]=digits[i]+1
                havecarry = digits[i]>=10
                digits[i]=digits[i]%10
        if havecarry:
            digits.insert(0,1)
        return digits