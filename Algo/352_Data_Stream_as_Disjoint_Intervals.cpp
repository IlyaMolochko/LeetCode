class SummaryRanges {
    set<int> nums;
public:
    SummaryRanges() {
        
    }
    
    void addNum(int value) {
        nums.insert(value);
    }
    
    vector<vector<int>> getIntervals() {
        if (nums.empty()) {
            return {};
        }
        vector<vector<int>> answ;
        int left = -1;
        int right = -1;
        for (auto num : nums) {
            if (left < 0) {
                left = num;
                right = num;
            } else if (right + 1 == num) {
                right = num;
            } else {
                answ.push_back({left, right});
                left = num;
                right = num;
            }
        }
        answ.push_back({left, right});
        return answ;
    }
};
