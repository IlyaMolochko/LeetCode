class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = -1;
        int r = nums.size();
        int x;
        int i = -1;
        while (l + 1 < r) {
            int x = (l + r) / 2;
            if (nums[x] < target) {
                l = x;
            } else if (nums[x] >= target) {
                r = x;
            }
        }
        return r;
    }
};
