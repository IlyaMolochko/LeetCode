class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        int mn = numeric_limits<int>::max();
        set<int> s;
        for (auto &i : nums){
            if (i % 2){
                s.insert(-2 * i);
                mn = min(mn, 2 * i);
            } else {
                s.insert(-i);
                mn = min(mn, i);
            }
        }
        int res = numeric_limits<int>::max();
        while(*s.begin() % 2 == 0){
            res = min(*s.begin() * (-1) - mn, res);
            mn = min(*s.begin() / -2, mn);
            s.insert(*s.begin() / 2);
            s.erase(s.begin());
        }
        return min(res, *s.begin() * (-1) - mn);
    }
};
