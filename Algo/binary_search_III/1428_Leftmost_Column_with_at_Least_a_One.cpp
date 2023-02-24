# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        answ = cols
        for i in range(rows):
            l = -1
            r = cols
            while r - l > 1:
                x = (l + r) // 2
                if binaryMatrix.get(i, x) == 1:
                    r = x
                else:
                    l = x
            answ = min(answ, r)
        return answ if answ != cols else -1
