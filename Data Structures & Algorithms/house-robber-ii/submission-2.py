class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def robs(noms):
            memo=[]
            def robh(ints):
                ans=0
                if len(ints) <= len(memo) and len(memo)>1:
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
            return robh(noms)
        return max(robs(nums[:len(nums)-1]),robs(nums[1:]))