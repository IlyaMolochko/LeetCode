class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        while numBottles >= numExchange:
            k = numBottles // numExchange
            cnt += k * numExchange
            numBottles -= k * numExchange
            numBottles += k
        return cnt + numBottles
