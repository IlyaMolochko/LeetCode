class Solution {
public:
    string addBinary(string a, string b) {
        string answ(max(a.size(), b.size()) + 1, '0');
        int i = a.size() - 1, j = b.size() - 1;
        int idx = answ.size() - 1;
        int rest = 0;
        while (i >= 0 and j >= 0) {
            if (a[i] == '1' and b[j] == '1') {
                answ[idx] = (rest == 0 ? '0' : '1');
                rest = 1;
            } else if (a[i] == '1' or b[j] == '1') {
                answ[idx] = (rest == 0 ? '1' : '0');
            } else {
                answ[idx] = (rest == 0 ? '0' : '1');
                rest = 0;
            }
            --i;
            --j;
            --idx;
        }
        while (i >= 0) {
            if (a[i] == '1') {
                answ[idx] = (rest == 0 ? '1' : '0');
            } else {
                answ[idx] = (rest == 0 ? '0' : '1');
                rest = 0;
            }
            --i;
            --idx;
        }
        while (j >= 0) {
            if (b[j] == '1') {
                answ[idx] = (rest == 0 ? '1' : '0');
            } else {
                answ[idx] = (rest == 0 ? '0' : '1');
                rest = 0;
            }
            --j;
            --idx;
        }
        if (rest != 0) {
            answ[idx] = '1';
        } else {
            ++idx;
        }
        return answ.substr(idx);
    }
};

