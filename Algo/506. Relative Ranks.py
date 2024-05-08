class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        mx = max(score)
        score_to_index = [0] * (mx + 1)
        for i in range(n):
            score_to_index[score[i]] = i + 1
        ms = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = ["0"] * n
        place = 1
        for i in range(mx, -1, -1):
            if score_to_index[i] != 0:
                idx = score_to_index[i] - 1
                if place < 4:
                    rank[idx] = ms[place - 1]
                else:
                    rank[idx] = str(place)
                place += 1
        return rank
