struct item{
    int p;
    int r;
};

struct disjointSet{
    vector<item> sets;

    disjointSet(int n) {
        sets.reserve(n);
        for (int i = 0; i < n; ++i) {
            sets.push_back({i, 0});
        }
    }

    int find(int i) {
        return sets[i].p = (sets[i].p == i ? i : find(sets[i].p));
    }

    void union_sets(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            if (a > b) {
                sets[b].p = a;
            } else if (a == b) {
                sets[b].p = a;
                ++sets[a].r;
            } else {
                sets[a].p = b;
            }
        }
    }
};

class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        disjointSet ds(n + 1);
        int answ = numeric_limits<int>::max();
        for (auto &road : roads) {
            ds.union_sets(road[0], road[1]);
        }
        for (auto &road: roads) {
            if (ds.find(1) == ds.find(road[0])) {
                answ = min(answ, road[2]);
            }
        }
        return answ;
    }
};
