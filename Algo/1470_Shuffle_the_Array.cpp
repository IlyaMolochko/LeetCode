class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> answ(2 * n);
        for (int i = 0; i < n; ++i) {
            answ[2 * i] = nums[i];
            answ[2 * i + 1] = nums[i + n];
        }
        return answ;
    }
};

