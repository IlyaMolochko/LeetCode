class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int l = 0;
        int r = 0;
        int answ = 0;
        unordered_map<int, int> mp;
        int cnt = 0;
        while (r < fruits.size()) {
            if (mp.count(fruits[r]) == 0 or mp[fruits[r]] == 0) {
                ++cnt;
            }
            ++mp[fruits[r]];
            while (l < r and cnt > 2) {
                --mp[fruits[l]];
                if (mp[fruits[l]] == 0) {
                    --cnt;
                }
                ++l;
            }
            answ = max(answ, r - l + 1);
            ++r;            
        }
        return answ;
    }
};

