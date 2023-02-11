struct st{
    int i;
    int c;
    int d;
};

bool operator==(const st &s1, const st &s2) {
    return s1.i == s2.i and s1.c == s2.c;
}

struct st_hash {
    std::size_t operator () (const st &s) const {
        return (static_cast<int64_t>(s.i) << 31) ^ s.c;
    }
};

class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& redEdges, vector<vector<int>>& blueEdges) {
        vector<vector<vector<int>>> edges(2, vector<vector<int>> (n));
        for (auto &edge : redEdges) {            
            edges[0][edge[0]].push_back(edge[1]);
        }
        for (auto &edge : blueEdges) {
            edges[1][edge[0]].push_back(edge[1]);          
        }
        vector<int> d(n, -1);
        d[0] = 0;
        queue<st> q;
        q.push({0, 0, 0});
        q.push({0, 1, 0});
        unordered_set<st, st_hash> s;
        s.insert({0, 0, 0});
        s.insert({0, 1, 0});
        int cnt = 1;
        while (!q.empty() and cnt < n) {
            auto sz = q.size();
            for (int t = 0; t < sz; ++t) {
                auto top = q.front();
                q.pop();
                int c = (top.c + 1) % 2;
                for (int i = 0; i < edges[c][top.i].size(); ++i) {
                    if (d[edges[c][top.i][i]] == -1) {
                        d[edges[c][top.i][i]] = top.d + 1;
                        ++cnt;
                    }
                    if (s.count({edges[c][top.i][i], c, 0}) == 0) {
                        q.push({edges[c][top.i][i], c, top.d + 1});
                        s.insert({edges[c][top.i][i], c, 0});
                    }
                }
            }            
        }
        return d;
    }
};

