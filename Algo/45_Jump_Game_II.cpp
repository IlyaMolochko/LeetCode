class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> d(nums.size(), 10000000);
        d[0] = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i){
            for (int j = 0; j <= nums[i]; ++j){
                d[min(n - 1, i + j)] = min(d[i] + 1, d[min(n - 1, i + j)]);
            }            
        }
        return d.back();
    }
};
