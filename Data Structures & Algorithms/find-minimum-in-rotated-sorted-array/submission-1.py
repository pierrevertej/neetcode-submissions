class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=int((low+high)/2)
            if res<=nums[mid]:
                low=mid+1
            else:
                res=nums[mid]
                high=mid-1
        return res