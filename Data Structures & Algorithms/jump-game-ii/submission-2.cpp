class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size()<2) return 0;
        int curr=0;
        int range=curr+nums[curr];
        int count=0;
        while (range<nums.size()-1) {
            int exp=curr+1;
            for (int i = curr+2; i<=curr+nums[curr]; ++i) {
                if (nums[i]+i>=nums[exp]+exp) {
                    exp=i;
                }
            }
            curr=exp;
            range=curr+nums[curr];
            ++count;
        } return count+1;
    }
};
