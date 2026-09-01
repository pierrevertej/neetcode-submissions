class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size()==0) return true;
        int curr=0;
        int range=curr+nums[curr];
        while (range<nums.size()-1) {
            if (nums[curr]==0) return false;
            int exp=curr+1;
            for (int i = curr+2; i<=curr+nums[curr]; ++i) {
                if (nums[i]+i>=nums[exp]+exp) {
                    exp=i;
                }
            }
            curr=exp;
            range=curr+nums[curr];
        } return true;
    }
};
