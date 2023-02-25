# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def sol(self, reader: 'ArrayReader', l: int, r: int):
        if r - l + 1 > 1 and (r - l + 1) % 2 == 1:
            x = (l + r) // 2
            res = reader.compareSub(l, x - 1, x + 1, r)
            if res == 0:
                return x
            elif res == 1:
                return self.sol(reader, l, x - 1)
            else:
                return self.sol(reader, x + 1, r)
        elif r - l + 1 > 1:
            x = (l + r) // 2
            res = reader.compareSub(l, x, x + 1, r)
            if res == 1:
                return self.sol(reader, l, x)
            else:
                return self.sol(reader, x + 1, r)
        else:
            return l

    def getIndex(self, reader: 'ArrayReader') -> int:
        return self.sol(reader, 0, reader.length() - 1)
