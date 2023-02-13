class Solution {
public:
    int countOdds(int low, int high) {
        return ((high - low + 1) % 2 == 0 ? (high - low + 1) / 2 : (low % 2 ? (high - low + 1) / 2 + 1 : (high - low + 1) / 2));
    }
};
