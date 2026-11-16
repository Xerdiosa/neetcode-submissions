class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        A=65
        while columnNumber>0:
            remainder = (columnNumber-1)%26
            ans.append(chr(A+remainder))
            columnNumber=(columnNumber-1)//26
        return "".join(ans[::-1])