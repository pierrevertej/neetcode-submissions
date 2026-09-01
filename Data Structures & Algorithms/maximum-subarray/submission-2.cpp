class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans=nums[0];
        int before=nums[0];
        for (int i=1; i<nums.size();++i) {
            int curr=max(before+nums[i], nums[i]);
            ans=max(curr, ans);
            before=curr;
        }
        return ans;
    }
};
