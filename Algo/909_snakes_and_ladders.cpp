class Solution {
public:
    pair<int, int> get_pos(int m, int n) {
        --m;
        int x = n - m / n - 1;
        int y = ((n - x) % 2 == 0 ? n - m % n - 1: m % n);
        return {x, y};
    }

    int snakesAndLadders(vector<vector<int>>& board) {
        int n = board.size();
        queue<int> q;
        unordered_set<int> st;
        pair<int, int> p = get_pos(1, n);
        if (board[p.first][p.second] == -1) {
            st.insert(1);
            q.push(1);
        } else {
            st.insert(board[p.first][p.second]);
            q.push(board[p.first][p.second]);
        }        
        int cnt = 0;
        int answ = -1;
        int m = n * n;
        while (!q.empty()) {
            auto size = q.size();
            ++cnt;
            for (int k = 0; k < size; ++k) {
                auto top = q.front();
                q.pop();
                for (int i = top + 1; i <= min(m, top + 6); ++i) {
                    p = get_pos(i, n);
                    
                    if (board[p.first][p.second] == -1 and st.count(i) == 0) {
                        st.insert(i);
                        q.push(i);
                        if (i == m) {
                            return cnt;
                        }
                    } else if (board[p.first][p.second] != -1 and st.count(board[p.first][p.second]) == 0) {
                        st.insert(board[p.first][p.second]);
                        q.push(board[p.first][p.second]);
                        if (board[p.first][p.second] == m) {
                            return cnt;
                        }
                    }
                }
            }
        }
        return answ;
    }
};
