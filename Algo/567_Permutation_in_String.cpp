class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int> dct1(26), dct2(26);
        for (auto c : s1) {
            ++dct1[c - 'a'];
        }
        bool answ = false;
        for (int l = 0, i = 0; i < s2.size() and !answ; ++i) {
            ++dct2[s2[i] - 'a'];
            while (dct2[s2[i]  - 'a'] > dct1[s2[i]  - 'a'] and l <= i) {
                --dct2[s2[l] - 'a'];
                ++l;
            }
            answ = (i - l + 1 == s1.size());
        }
        return answ;
    }
};

