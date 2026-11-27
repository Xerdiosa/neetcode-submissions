class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        candidate = 0
        fuel = 0
        for i in range(len(gas)):
            fuel = fuel+gas[i%len(gas)]-cost[i%len(gas)]
            if fuel<0:
                fuel=0
                candidate = i%len(gas)+1
                
        return candidate