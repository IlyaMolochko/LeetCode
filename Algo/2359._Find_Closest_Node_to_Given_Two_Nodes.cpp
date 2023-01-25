class Solution {
public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int u1 = node1;
        int u2 = node2;
        if (u1 == u2) {
            return u1;
        }
        unordered_map<int, int> st1, st2;
        st1[u1] = 0;
        st2[u2] = 0;
        int cnt = 0;
        int answ = -1;
        int d = edges.size() + 1;
        while (u1 != -1 or u2 != -1) {
            ++cnt;
            if (u1 != -1 and edges[u1] != -1 and st1.count(edges[u1]) == 0) {
                if (st2.count(edges[u1])) {
                    if (max(st2[edges[u1]], cnt) < d) {
                        answ = edges[u1];
                        d = cnt;
                    } else if (max(st2[edges[u1]], cnt) == d) {
                        answ = min(edges[u1], answ);
                    }
                }
                st1[edges[u1]] = cnt;
                u1 = edges[u1];
            } else {
                u1 = -1;
            }
            if (u2 != -1 and edges[u2] != -1 and st2.count(edges[u2]) == 0) {
                if (st1.count(edges[u2])) {
                    if (max(st1[edges[u2]], cnt) < d) {
                        answ = edges[u2];
                        d = cnt;
                    } else if (max(st1[edges[u2]], cnt) == d) {
                        answ = min(edges[u2], answ);
                    }
                }
                st2[edges[u2]] = cnt;
                u2 = edges[u2];
            } else {
                u2 = -1;
            }
        }
        return answ;
    }
};
