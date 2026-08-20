class Solution:
    def rob(self, nums: List[int]) -> int:
        memor=[]
        memol=[]
        def robr(ints):
            ans=0
            if len(ints) <= len(memor) and ints:
                return memor[len(ints)-1]
            if len(ints)==1:
                ans=ints[0]
            if len(ints)==2:
                ans=max(ints[0],ints[1])
            if len(ints)>2:
                ans=max(robr(ints[:len(ints)-2])+ints[-1],robr(ints[:len(ints)-1]))
            if len(ints)==len(memor)+1:
                memor.append(ans)
            return ans
        def robl(ints):
            ans=0
            if len(ints) <= len(memol) and ints:
                return memol[len(ints)-1]
            if len(ints)==1:
                ans=ints[0]
            if len(ints)==2:
                ans=max(ints[0],ints[1])
            if len(ints)>2:
                ans=max(robl(ints[:len(ints)-2])+ints[-1],robl(ints[:len(ints)-1]))
            if len(ints)==len(memol)+1:
                memol.append(ans)
            return ans
        if len(nums)==1:
            return nums[0]
        return max(robl(nums[:len(nums)-1]),robr(nums[1:len(nums)]))