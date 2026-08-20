class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        n=len(gas)
        startIdx=0
        tank=0
        for idx in range(n):
            tank+=gas[idx]-cost[idx]
            if tank<0:
                startIdx=idx+1
                tank=0
        return startIdx