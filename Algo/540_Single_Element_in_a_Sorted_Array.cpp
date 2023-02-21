class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l = 0, r = static_cast<int>(nums.size()) - 2;
        int x;
        while (l <= r) {
            x = (l + r) / 2;
            if (nums[x] == nums[x^1]){
                l = x + 1;
            } else {
                r = x - 1;
            }
        }
        return nums[l];
    }
};
