class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        flowers = 0
        while i < len(flowerbed):
            while i < len(flowerbed) and flowerbed[i] == 1:
                i += 1
            cnt = 0
            while i < len(flowerbed) and flowerbed[i] == 0:
                i += 1
                cnt += 1
            if cnt == len(flowerbed):
                flowers += (cnt + 1) // 2
            elif i == cnt or i == len(flowerbed):
                flowers += cnt // 2
            else:
                flowers += (cnt - 1) // 2
        return flowers >= n
