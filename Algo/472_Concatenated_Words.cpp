struct TrieNode {
    TrieNode *parent;
    vector<TrieNode *> children;
    string_view x;
    int terminal;

    TrieNode() {
        parent = nullptr;
        children.assign(26, nullptr);
        terminal = -1;
    }

    TrieNode(TrieNode *node, string_view sv, int num) {
        parent = node;
        children.assign(26, nullptr);
        terminal = num;
        x = sv;
    }
};

struct Trie {
    TrieNode *root;

    Trie() {
        root = new TrieNode();
        root->parent = root;
    }

    void build(vector<string> &words) {
        for (int k = 0; k < words.size(); ++k) {
            TrieNode *node = root;
            int i = 0;
            int j = 0;
            TrieNode *child = nullptr;
            while (i < words[k].size() and node->children[words[k][i] - 'a'] != nullptr) {
                j = 0;
                child = node->children[words[k][i] - 'a'];
                while (i < words[k].size()
                       and j < child->x.size()
                       and child->x[j] == words[k][i]) {
                    ++i;
                    ++j;
                }
                if (i == words[k].size()) {
                    break;
                } else if (j == child->x.size()) {
                    node = child;
                } else {
                    break;
                }
            }
            if (i != words[k].size() and child != nullptr and j != child->x.size()) {
                string_view sv = child->x.substr(j);
                child->x = child->x.substr(0, j);
                auto *first = new TrieNode(child, sv, child->terminal);
                string_view sv1(words[k]);
                sv1 = sv1.substr(i);
                auto *second = new TrieNode(child, sv1, k);
                swap(child->children, first->children);
                child->children[first->x[0] - 'a'] = first;
                child->children[second->x[0] - 'a'] = second;
                child->terminal = -1;
            } else if (i != words[k].size()) {
                string_view sv(words[k]);
                sv = sv.substr(i);
                node->children[words[k][i] - 'a'] = new TrieNode(node, sv, k);
            } else if (i == words[k].size()) {
                if (j != child->x.size()) {
                    string_view sv = child->x.substr(j);
                    child->x = child->x.substr(0, j);
                    auto *new_node = new TrieNode(child, sv, child->terminal);
                    swap(child->children, new_node->children);
                    child->children[new_node->x[0] - 'a'] = new_node;
                    new_node->terminal = child->terminal;
                    child->terminal = k;
                } else if (j == child->x.size() and child->terminal == -1) {
                    child->terminal = k;
                }
            }
        }
    }

    int check(string_view word, int k, vector<pair<int, int>> &dp) {
        TrieNode *node = root;
        int i = 0;
        int j = 0;
        TrieNode *child = nullptr;
        while (i < word.size() and node->children[word[i] - 'a'] != nullptr) {
            j = 0;
            child = node->children[word[i] - 'a'];
            while (i < word.size()
                   and j < child->x.size()
                   and child->x[j] == word[i]) {
                ++i;
                ++j;
            }
            if (i == word.size()) {
                break;
            } else if (j == child->x.size()) {
                if (child->terminal != -1 and dp[k].first > dp[k + i].first + 1) {
                    dp[k].first = dp[k + i].first + 1;
                    dp[k].second = child->terminal;
                }
                node = child;
            } else {
                break;
            }
        }
        if (i != word.size() or child == nullptr or j != child->x.size()) {
            return -1;
        } else {
            return child->terminal;
        }
    }
};

class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        Trie trie;
        trie.build(words);
        vector<string> answ;
        for (auto &s : words) {
            vector<pair<int, int>> dp(s.size() + 1, {10001, -1});
            dp.back() = {0, - 1};
            string_view sv(s);
            for (int i = s.size() - 1; i >= 0; --i) {
                int j = min(s.size() - i, s.size() - 1);
                int res = trie.check(sv.substr(i, j), i, dp);
                if (res != -1) {
                    if (dp[i].first > dp[i + j].first + 1) {
                        dp[i].first = dp[i + j].first + 1;
                        dp[i].second = res;
                    }
                }
            }
            if (dp[0].second != -1) {
                answ.push_back(s);
            }
        }
        return answ;
    }
};
