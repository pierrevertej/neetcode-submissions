class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        def compute(startIndex):
            n=len(gas)
            total=0
            for i in range(startIndex, startIndex+n):
                total+=gas[i%n] - cost[i%n]
                if total < 0:
                    return compute((i+1)%n)
            return startIndex
        return compute(0)

