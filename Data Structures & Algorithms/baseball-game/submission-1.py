class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "C": #For operations "C" and "D", there will always be at least one previous score on the record.
                record.pop()
            elif i == "D":
                record.append(record[-1]*2)
            elif i == "+": #For operation "+", there will always be at least two previous scores on the record.
                record.append(record[-1]+record[-2])
            else:
                record.append(int(i))
        # print(record)
        return sum(record) 