class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int ans=1;
        vector<int> lengths;
        lengths.resize(nums.size(), 1);
        for (int i=1;i<nums.size();++i) {
            for (int j=0; j<i; ++j) {
                if (nums[i]>nums[j]) {
                    lengths[i]=max(lengths[i], lengths[j]+1);
                    ans=max(ans,lengths[i]);
                }
            }
        }
        return ans;
    }
};
