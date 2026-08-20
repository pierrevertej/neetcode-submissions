class Solution:
    ans=1000
    def findMin(self, nums: List[int]) -> int:
        global ans
        
        low=0
        high=len(nums)-1
        if low>high:
            return self.ans
        self.ans=min(self.ans,nums[0])
        mid=int((low+high)/2)
        if self.ans<=nums[mid]:
            return self.findMin(nums[mid+1:])
        else:
            self.ans=nums[mid]
            return self.findMin(nums[:mid])