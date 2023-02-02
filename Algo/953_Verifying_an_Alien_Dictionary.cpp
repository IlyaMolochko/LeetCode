class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        vector<int> mp(26, 100);
        for (int i = 0; i < order.size(); ++i){
            mp[order[i] - 'a'] = i;
        }
        bool answ = true;
        vector<string> v(words.size());
        for (int i = 0; i < words.size(); ++i){
            for (auto c : words[i]){
                v[i].push_back(mp[c - 'a']);
            }
        }
        for (int i = 1; i < v.size() and answ; ++i){
            answ &= (v[i - 1] <= v[i]);
        }
        return answ;
    }
};

