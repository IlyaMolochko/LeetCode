class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        answ = 0
        score = 0
        while l <= r and (score > 0 or power >= tokens[l]):
            while l <= r and power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            answ = max(answ, score)
            if l <= r and score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
        return answ
