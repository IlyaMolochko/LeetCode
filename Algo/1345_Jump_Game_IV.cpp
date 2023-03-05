struct st{
    int i;
    int dist;
};

class Solution {
public:
    bool valid(int i, vector<int>& arr) {
        return i >= 0 and i < arr.size();
    }
    
    int minJumps(vector<int>& arr) {
        if (arr.size() == 1) {
            return 0;
        }
        unordered_map<int, queue<int>> mp;
        vector<bool> visited(arr.size(), false);
        visited[0] = true;
        queue<st> q;
        q.push({0, 0});
        
        for (int i = 0; i < arr.size(); ++i) {
            mp[arr[i]].push(i);
        }
        int answ = 0;
        while (!q.empty()) {
            auto top = q.front();
            q.pop();
            while (!mp[arr[top.i]].empty()) {
                int i = mp[arr[top.i]].front();
                mp[arr[top.i]].pop();
                if (i == arr.size() - 1) {
                    return top.dist + 1;
                }
                if (!visited[i]) {
                    q.push({i, top.dist + 1});
                    visited[i] = true;
                }
            }
        
            if (top.i + 1 == arr.size() - 1) {
                    return top.dist + 1;
            }
            if (valid(top.i + 1, arr) and !visited[top.i + 1]) {
                q.push({top.i + 1, top.dist + 1});
                visited[top.i + 1] = true;
            }
            if (valid(top.i - 1, arr) and !visited[top.i - 1]) {
                q.push({top.i - 1, top.dist + 1});
                visited[top.i - 1] = true;
            }
        }
        return answ;
    }
};
