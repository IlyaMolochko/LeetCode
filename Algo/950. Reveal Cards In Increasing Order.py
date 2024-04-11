class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque()
        for i in range(n):
            q.append(i)
        deck.sort()
        answ = [0] * n
        for c in deck:
            answ[q.popleft()] = c
            if q:
                q.append(q.popleft())
        return answ
