/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;
    
    Node() {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }
    
    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

class Solution {
public:
    Node* solve(vector<vector<int>>& grid, int i, int j, int len) {
        if (len == 1) {
            return new Node(grid[i][j], true);
        }

        auto topLeft = solve(grid, i, j, len / 2);
        auto topRight = solve(grid, i, j + len / 2, len / 2);
        auto bottomLeft = solve(grid, i + len / 2, j, len / 2);
        auto bottomRight = solve(grid, i + len / 2, j + len / 2, len / 2);
        if (topLeft->isLeaf and topRight->isLeaf and bottomLeft->isLeaf and bottomRight->isLeaf and topLeft->val == topRight->val and topLeft->val == bottomLeft->val and topLeft->val == bottomRight->val) {
            return new Node(topLeft->val, true);
        }

        return new Node(false, false, topLeft, topRight, bottomLeft, bottomRight);
    }

    Node* construct(vector<vector<int>>& grid) {
        return solve(grid, 0, 0, grid.size());
    }
};
