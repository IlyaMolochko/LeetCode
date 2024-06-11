class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dct = defaultdict(int)
        for i in range(len(arr2)):
            dct[arr2[i]] = i
        return sorted(arr1, key=lambda x: dct[x] if x in dct else x * 1000 + 1000)
