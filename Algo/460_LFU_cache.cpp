struct item{
    int value;
    int freq;
};

class LFUCache {
    int capacity;
    int min_freq;
    unordered_map<int, item> mp;
    unordered_map<int, list<int>> freq;
    unordered_map<int, list<int>::iterator> pos;
public:
    LFUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        if (mp.count(key) == 0) {
            return -1;
        }
        freq[mp[key].freq].erase(pos[key]);
        ++mp[key].freq;
        freq[mp[key].freq].push_back(key);
        pos[key] = prev(freq[mp[key].freq].end());
        if (freq[min_freq].empty()) {
            ++min_freq;
        }
        return mp[key].value;
    }
    
    void put(int key, int value) {
        if (capacity <= 0) {
            return;
        }
        if (get(key) != -1) {
            mp[key].value = value;
            return;
        }
        if (mp.size() == capacity) {
            int k = freq[min_freq].front();
            freq[min_freq].pop_front();
            pos.erase(k);
            mp.erase(k);
        }
        mp[key] = {value, 1};
        min_freq = 1;
        freq[min_freq].push_back(key);
        pos[key] = prev(freq[min_freq].end());
    }
};
