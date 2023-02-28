# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l = -1
        r = 10000
        out_of_range = (1 << 31) - 1
        answ = -1
        while r - l > 1:
            x = (l + r) // 2
            if reader.get(x) == out_of_range or reader.get(x) > target:
                r = x
            elif reader.get(x) < target:
                l = x
            else:
                answ = x
                break
        return answ
