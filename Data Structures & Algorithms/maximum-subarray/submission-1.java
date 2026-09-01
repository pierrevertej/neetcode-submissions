class Solution {
    public int maxSubArray(int[] nums) {
        int ans=nums[0];
        int before=nums[0];
        for (int i = 1; i<nums.length; i++) {
            int curr=Math.max(before+nums[i],nums[i]);
            ans=Math.max(ans,curr);
            before=curr;
        }
        return ans;
    }
}
