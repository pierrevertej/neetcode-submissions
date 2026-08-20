class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        end=0
        n = len(gas)
        total = gas[0] - cost[0]
        while start!=((end+1)%n):
            if total < 0:
                start = (start-1)%n
                total += gas[start] - cost[start]
            else:
                end+=1
                total += gas[end] - cost[end]
        if total < 0:
            return -1
        else: 
            return start
