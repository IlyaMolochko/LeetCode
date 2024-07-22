class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        ids = sorted(range(n), key= lambda i: heights[i], reverse=True)
        answ = [names[i] for i in ids]
        return answ
