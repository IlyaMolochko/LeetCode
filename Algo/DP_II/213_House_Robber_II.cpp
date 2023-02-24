class Solution {
public:
    int get_answ(vector<int> &nums, int add) {
        vector<int> dp(nums.size());
        dp[add] = nums[add];
        dp[add + 1] = nums[add + 1]; 
        int answ = max(dp[add], dp[add + 1]);
        for (int i = add + 2; i + (add == 0) < nums.size(); ++i) {
            dp[i] = max(dp[i - 2] + nums[i], (i > 2 ? dp[i - 3] + nums[i] : 0));
            answ = max(answ, dp[i]);
        }
        return answ;
    }
    
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        } else if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        }
        
        int answ = get_answ(nums, 0);
        answ = max(answ, get_answ(nums, 1));
        return answ;
    }
};
