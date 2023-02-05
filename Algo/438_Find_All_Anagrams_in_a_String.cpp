class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> hsh(26), hs(26);
        vector<int> chars;
        if (p.size() > s.size()) {
            return {};
        }
        for (auto c : p) {
            if (hsh[c - 'a'] == 0) {
                chars.push_back(c - 'a');
            }
            ++hsh[c - 'a'];
        }
        int n = p.size();
        vector<int> answ;
        for (int i = 0; i < s.size(); ++i) {
            ++hs[s[i] - 'a'];
            if (i - n + 1 > 0) {
                --hs[s[i - n] - 'a'];
            }
            if (i - n + 1 >= 0) {
                bool f = true;
                for (auto j : chars) {
                    if (hsh[j] != hs[j]) {
                        f = false;
                        break;
                    }
                }
                if (f) {
                    answ.push_back(i - n + 1);
                }
            }
        }
        return answ;
    }
};

