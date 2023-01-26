struct item{
    int i;
    int d;
};

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int, int> mp;
        queue<item> q;
        q.push({src, 0});
        mp[src] = 0;
        int d = 100000000;
        int answ = -1;
        vector<vector<pair<int, int>>> g(n, vector<pair<int, int>>());
        for (auto &f : flights) {
            g[f[0]].push_back({f[1], f[2]});
        }
        for (int t = 0; t <= k; ++t) {
            auto size = q.size();
            for (int i = 0; i < size; ++i) {
                auto top = q.front();
                q.pop();
                for (int j = 0; j < g[top.i].size(); ++j) {
                    if (mp.count(g[top.i][j].first) == 0 or mp[g[top.i][j].first] > g[top.i][j].second + top.d) {
                        mp[g[top.i][j].first] = g[top.i][j].second + top.d;
                        q.push({g[top.i][j].first, g[top.i][j].second + top.d});
                    }
                }
                
            }
        }
        return mp.count(dst) == 0 ? -1 : mp[dst];
    }
};

