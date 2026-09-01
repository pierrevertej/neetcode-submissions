class Solution {
public:
    bool canJump(vector<int>& nums) {
        int last=nums.size()-1;
        for (int i=nums.size()-2; i>=0; --i) {
            if (nums[i]>=last-i) {
                last=i;
            }
        }
        if (last==0) return true;
        return false;
    }
};
