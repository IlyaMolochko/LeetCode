class Solution {
public:
    bool check(vector<int>& piles, int k, int h) {
        int64_t cnt = 0;
        for (auto p : piles) {
            cnt += static_cast<int64_t>(p / k) + static_cast<int64_t>(p % k > 0);
        }
        return cnt <= h;
    }
    
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = 0;
        for (auto p : piles) {
            r = max(r, p);
        }
        int answ = 1000'000'000;
        int x;
        while (l <= r) {
            x = (l + r) / 2;
            if (check(piles, x, h)) {
                answ = x;
                r = x - 1;
            } else {
                l = x + 1;
            }
        }
        return answ;
    }
};
