class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<unordered_set<string>> mp(26);
        for (auto &s : ideas) {
            mp[s[0] - 'a'].insert(s.substr(1));
        }
        int64_t answ = 0;
        for (int i = 0; i < 25; ++i) {
            for (int j = i + 1; j < 26; ++j) {
                int cnt = 0;
                for (auto &s : mp[i]) {
                    if (mp[j].count(s)) {
                        ++cnt;
                    }
                }
                answ += 2ll * (mp[i].size() - cnt) * (mp[j].size() - cnt);
            }
        }
        return answ;
    }
};

