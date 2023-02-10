struct st{
    int i;
    int j;
};

class Solution {
public:
    bool valid(int i, int j, int n, int m) {
        return i >= 0 and i < n and j >= 0 and j < m;
    }    
    
    int maxDistance(vector<vector<int>>& grid) {
        vector<pair<int, int>> d = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        queue<st> q;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == 1) {
                    q.push({i, j});
                }
            }
        }
        int dist = 1;
        int answ = grid.size() * grid[0].size() + 1;
        while (!q.empty()) {
            int n = q.size();
            for (int t = 0; t < n; ++t) {
                auto top = q.front();
                int i = top.i;
                int j = top.j;
                q.pop();
                for (auto &[dx, dy] : d) {
                    if (valid(i + dx, j + dy, grid.size(), grid[0].size()) and grid[i + dx][j + dy] == 0) {
                        grid[i + dx][j + dy] = 1;
                        answ = dist;
                        q.push({i + dx, j + dy});
                    }
                }
            }
            ++dist;
        }
        return (answ == grid.size() * grid[0].size() + 1 ? -1 : answ);
    }
};

