class Solution {
public:
    void quickSort(std::vector<int>& v, int l, int r){
    int i = l;
    int j = r;
    int x = v[(l + r) / 2];
    while(i < j){
        while (v[i] < x){
            ++i;
        }
        while (v[j] > x){
            --j;
        }
        if (i <= j){
            std::swap(v[i], v[j]);
            ++i;
            --j;
        }
    }
    if (i < r){
        quickSort(v, i, r);
    }
    if (l < j){
        quickSort(v, l, j);
    }
}

    vector<int> sortArray(vector<int>& nums) {
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }
};
