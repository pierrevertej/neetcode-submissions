class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[]
        def robh(ints):
            ans=0
            if len(ints) <= len(memo):
                return memo[len(ints)-1]
            if len(ints)==1:
                ans=ints[0]
            if len(ints)==2:
                ans=max(ints[0],ints[1])
            if len(ints)>2:
                ans=max(robh(ints[:len(ints)-2])+ints[-1],robh(ints[:len(ints)-1]))
            if len(ints)==len(memo)+1:
                memo.append(ans)
            return ans
        return robh(nums)