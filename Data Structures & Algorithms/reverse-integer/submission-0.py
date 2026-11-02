class Solution:
    def reverse(self, x: int) -> int:
        negative = x<0
        x=abs(x)
        limit = list(str(2**31))
        if not negative:
            limit[9]="7"
        print(limit)
        xstring = str(x)[::-1]
        if len(xstring)<10:
            return int(xstring)* (-1 if negative else 1)
        for i in range(len(xstring)):
            if limit[i]<xstring[i]:
                return 0
            if limit[i]>xstring[i]:
                break
        return int(xstring)* (-1 if negative else 1)
        