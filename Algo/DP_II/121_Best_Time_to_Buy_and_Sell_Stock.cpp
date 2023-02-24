class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mn = prices[0];
        int answ = 0;
        for (int i = 1; i < prices.size(); ++i) {
            answ = max(answ, prices[i] - mn);
            if (prices[i] < mn) {
                mn = prices[i];
            }
        }
        return answ;
    }
};
