class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        vector<int> answ;
        int pos = num.size() - 1;
        int rest = 0;
        while (k > 0 or pos >= 0) {
            int val = rest;
            if (pos >= 0) {
                val += num[pos];
                --pos;
            }
            if (k > 0) {
                val += k % 10;
                k /= 10;
            }            
            rest = (val >= 10 ? 1 : 0);
            answ.push_back(val % 10);
            
        }
        if (rest > 0) {
            answ.push_back(rest);
        }
        reverse(answ.begin(), answ.end());
        return answ;
    }
};
