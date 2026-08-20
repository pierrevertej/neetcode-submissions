class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=nums[0]
        def bst(low,high,ans):
            if low>high:
                return ans
            mid=int((low+high)/2)
            if ans<=nums[mid]:
                return bst(mid+1,high,ans)
            else:
                ans=nums[mid]
                return bst(low,mid-1,ans)
        return bst(0,len(nums)-1,ans)