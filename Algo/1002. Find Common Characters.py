class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        for i in range(1, len(words)):
            c = c & Counter(words[i])
        answ = []
        for i in c:
            while c[i] > 0:
                answ.append(i)
                c[i] -= 1
        return answ
