class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans = {{}};
        vector<vector<int>> temp = {};
        for (auto val : nums) {
            for (auto subset : ans) {
                vector<int> copy = subset;
                copy.push_back(val);
                temp.push_back(copy);
            }
            for (auto subset : temp) {
                ans.push_back(subset);
            } temp = {};
        } return ans;
    }
};
