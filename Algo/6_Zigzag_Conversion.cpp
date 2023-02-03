class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        vector<string> z(numRows);
        int n = s.size();
        --numRows;
        for (int i = 0; i < s.size(); ++i) {
            z[abs((i + numRows) % (2 * numRows) - numRows)] += s[i];
        }
        string answ;
        for (auto &i : z) {
            answ += i;
        }
        return answ;
    }
};

