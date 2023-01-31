class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        vector<pair<int, int>> v;
        int n = scores.size();
        v.reserve(n);
        vector<int> dp(n);
        for (int i = 0; i < n; ++i) {
            v.push_back({ages[i], scores[i]});
        }
        sort(v.begin(), v.end());
        for (int i = 0; i < n; ++i) {
            dp[i] = v[i].second;
        }
        int answ = dp[0];
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (v[i].second >= v[j].second) {
                    dp[i] = max(dp[i], v[i].second + dp[j]);
                }
            }
            answ = max(dp[i], answ);
        }
        return answ;
    }
};

