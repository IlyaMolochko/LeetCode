class Solution {
public:
    int tribonacci(int n) {
        int64_t a = 0, b = 1, c = 1, tmp;
        if (n == 0) {
            return 0;
        } else if (n <= 2) {
            return 1;
        }
        for (int i = 3; i <= n; ++i) {
            tmp = a + b + c;
            a = b;
            b = c;
            c = tmp;
        }
        return tmp;
    }
};
