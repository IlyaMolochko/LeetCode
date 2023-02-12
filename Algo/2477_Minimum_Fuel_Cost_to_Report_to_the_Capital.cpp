class Solution {
    int64_t answ;
public:
    int64_t dfs(int u, int p, vector<vector<int>> &g, int seats) {
        int64_t cnt = 1;
        for (auto &v : g[u]) {
            if (v != p) {
                cnt += dfs(v, u, g, seats);
            }
        }
        if (u != 0) {
            answ += static_cast<int64_t>((double)cnt / seats) + (cnt % seats != 0);
        }
        return cnt;
    }

    long long minimumFuelCost(vector<vector<int>>& roads, int seats) {
        vector<vector<int>> g(roads.size() + 1);
        for (auto &r : roads) {
            g[r[0]].push_back(r[1]);
            g[r[1]].push_back(r[0]);
        }
        answ = 0;
        dfs(0, -1, g, seats);
        return answ;
    }
};
