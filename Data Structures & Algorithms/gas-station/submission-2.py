class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        current=0
        tank=0
        n=len(gas)
        while True:
            for i in range(n):
                tank+=gas[current] - cost[current]
                current=(current+1)%n
                if tank < 0:
                    break
            if tank >= 0:
                return current
            else:
                tank = 0
