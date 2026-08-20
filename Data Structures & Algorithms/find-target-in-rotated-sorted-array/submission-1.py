class Solution:
    def search(self, nums: List[int], target: int) -> int:
        basis=nums[int((len(nums)-1)/2)]
        bigger=target>basis
        def bst(low,high):
            if low>high:
                return bst2(0,len(nums)-1)
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            if bigger:
                if nums[mid]<target and nums[mid]>=basis:
                    return bst(mid+1,high)
                return bst(low,mid-1)
            if nums[mid]>target and nums[mid]<=basis:
                return bst(low,mid-1)
            return bst(mid+1,high)

        def bst2(low,high):
            if low>high:
                return -1
            mid=int((low+high)/2)
            if nums[mid]==target:
                return mid
            if bigger:
                if nums[mid]<target and nums[mid]>basis:
                    return bst2(mid+1,high)
                return bst2(low,mid-1)
            if nums[mid]>target and nums[mid]<basis:
                return bst2(low,mid-1)
            return bst2(mid+1,high)
        return bst(0,len(nums)-1)